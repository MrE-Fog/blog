# OpenCV × Python × Optical Flow で物体追跡してみる

[f:id:kuri_megane:20180627182829p:plain]

正確には特徴点というものを追跡するもので，物体だと認識して追跡しているわけではないです．

---

<b>ざっくりまとめると</b>

* [Optical Flow (オプティカルフロー)](http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_video/py_lucas_kanade/py_lucas_kanade.html) を検出するソースコードを紹介したいと思います．

---

<b>目次</b>

[:contents]

---


<!-- more -->


## 前提

* ubutu 17.10
* python 3.6.5 (miniconda 4.5.3上の)
* opencv 3.1.0 ( [menpo](https://anaconda.org/menpo/opencv3) )

* opencv は何らかのサンプルプログラムで正しくインストールされていることを確認してください．
* 試したい動画 debug.avi がカレントディレクトリにあることとします．

## OpenCVの動作確認コード

[https://github.com/kuri-megane/blog/blob/master/20180628_OpenCV%20%C3%97%20Python%20%C3%97%20%E3%82%AA%E3%83%97%E3%83%86%E3%82%A3%E3%82%AB%E3%83%AB%E3%83%95%E3%83%AD%E3%83%BC%20(Optical%20Flow)%20%E3%81%A7%E7%89%A9%E4%BD%93%E8%BF%BD%E8%B7%A1/test_video_capture.py:embed:cite]


## サンプル動画



[https://github.com/kuri-megane/blog/blob/master/20180628_OpenCV%20%C3%97%20Python%20%C3%97%20%E3%82%AA%E3%83%97%E3%83%86%E3%82%A3%E3%82%AB%E3%83%AB%E3%83%95%E3%83%AD%E3%83%BC%20(Optical%20Flow)%20%E3%81%A7%E7%89%A9%E4%BD%93%E8%BF%BD%E8%B7%A1/debug.avi:embed:cite]





## ソースコード

このソースコードを説明します．


[https://gist.github.com/660a4946d3ad12a635649fa3ef4cb774:embed#20180628\_OpenCV × Python × オプティカルフロー (Optical Flow ...]

[sample_object_tracking.py](https://gist.github.com/kuri-megane/660a4946d3ad12a635649fa3ef4cb774) ((参考で紹介しているGithubにもコードがあります))




## 流れ

基本的には次の3点をWhileループで繰り返しながら行います．

1. 画像を読み込む
2. 特徴点を抽出する
3. 対応点を検出する
4. 点を選別する
5. 結果を描く



## 1. 画像を読み込む

```python

import cv2

# 読み込む動画の設定
cap = cv2.VideoCapture("debug.avi")

while True:

    # フレームの読み込み
    ret, frame = cap.read()
    
    # 結果画像の表示
    cv2.imshow("frame", frame)
    k = cv2.waitKey(30) & 0xff

    # qキーが押されたら終了
    if k == ord('q'):
        break

```

* cv2.VideoCapture() cf. ```https://docs.opencv.org/3.4.1/d8/dfe/classcv_1_1VideoCapture.html```


うまくいくと，動画が表示されると思います．
パスが間違えていたりすると，次のようなエラーが出ます．

```python

OpenCV Error: Assertion failed (size.width>0 && size.height>0) in imshow, file /home/travis/miniconda/conda-bld/conda_1486587069159/work/opencv-3.1.0/modules/highgui/src/window.cpp, line 281
Traceback (most recent call last):
  File "sample_of.py", line 13, in <module>
    cv2.imshow("frame", frame)
cv2.error: /home/travis/miniconda/conda-bld/conda_1486587069159/work/opencv-3.1.0/modules/highgui/src/window.cpp:281: error: (-215) size.width>0 && size.height>0 in function imshow

```

次のコード，

```python

k = cv2.waitKey(30) & 0xff

```

がないとウィンドウ自体が表示されません．

## 2. 特徴点を抽出する

```python

# Shi-Tomasiのコーナー検出パラメータ
# P.511,477
feature_params = dict(
    maxCorners=255,             # 保持するコーナー数, int
    qualityLevel=0.3,           # 最良値(最大固有値の割合?), double
    minDistance=7,              # この距離内のコーナーを棄却, double
    blockSize=7,                # 使用する近傍領域のサイズ, int
    useHarrisDetector=False,    # FalseならShi-Tomashi法
    # k=0.04,                     # Harris法の測度に使用
)

# 読み込んだフレームの特徴点を探す
# P.477
prev_points = cv2.goodFeaturesToTrack(
    image=first_gray,       # 入力画像
    mask=None,              # mask=0のコーナーを無視
    **feature_params
)

```

* cv2.goodFeaturesToTrack() cf. ```https://docs.opencv.org/3.4.1/dd/d1a/group__imgproc__feature.html#ga1d6bb77486c8f92d79c8793ad995d541```


prev_points は次のようになっているかと思います．

```python

[[[405. 166.]]

 [[414. 161.]]

 [[708. 278.]] ...

 [[108. 179.]]]

```

## 3. 対応点を検出する

```python

# Lucas-Kanade法のパラメータ
# P.489
lk_params = dict(
    winSize=(15, 15),           # 検索ウィンドウのサイズ
    maxLevel=2,                 # 追加するピラミッド層数

    # 検索を終了する条件
    criteria=(
        cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,
        10,
        0.03
    ),

    # 推測値や固有値の使用
    flags=cv2.OPTFLOW_LK_GET_MIN_EIGENVALS,
)

# オプティカルフロー(正確には対応点)の検出
# P.489
# next_points: 検出した対応点, numpy.ndarray
# status: 各点において，見つかれば1(True), 見つからなければ0(False), numpy.ndarray
# err: 検出した点の誤差, numpy.ndarray
next_points, status, err = cv2.calcOpticalFlowPyrLK(
    prevImg=old_gray,           # 前の画像(t-1)
    nextImg=frame_gray,         # 次の画像(t)
    prevPts=prev_points,        # 始点2次元ベクトル, 特徴点やそれに準ずる点
    nextPts=None,               # 結果の2次元ベクトル
    **lk_params
)

```

* cv2.calcOpticalFlowPyrLK() cf. ```https://docs.opencv.org/3.4.1/dc/d6b/group__video__track.html#ga473e4b886d0bcc6b65831eb88ed93323```


next_pointsは次のようになっているかと思います．

```python

[[[402.84473  165.7132  ]]

 [[411.91354  160.71782 ]]

 [[708.5796   278.81006 ]]...

 [[103.10566  179.05269 ]]]

```

statusは次のようになっているかと思います．

```python

[[1]
 [1]
 [1]
 ...
 [1]]

```


## 4. 点の選別

対応点が必ずしも見つかるわけではないため，calcOpticalFlowPyrLK の status の値を見て，選別します．

```python

good_new = next_points[status == 1]
good_old = prev_points[status == 1]

```

next_points,prev_points はいずれも多次元配列であることに注意が必要です．
また，数フレームおきに特徴点を検出しなおさないと，対応点が無くなるのでエラーになります．

## 5. 結果を描く

ランダムな色をリストで生成し，結果描画レイヤーを用意して，ひたすら重ね書きしていきます．重ね書きした後に，フレーム画像と合わせています．

```python

# フローを描く
for rank, (prev_p, next_p) in enumerate(zip(good_old, good_new)):

    # x,y座標の取り出し
    # prev_x, prev_y: numpy.float32
    # next_x, next_y: numpy.float32
    prev_x, prev_y = prev_p.ravel()
    next_x, next_y = next_p.ravel()

    # フローの線を描く
    flow_layer = cv2.line(
        img=flow_layer,                 # 描く画像
        pt1=(prev_x, prev_y),           # 線を引く始点
        pt2=(next_x, next_y),           # 線を引く終点
        color=color[rank].tolist(),     # 描く色
        thickness=2,                    # 線の太さ
        # lineType=0,                   # 線の種類，無くても良い
        # shift=0,                      # 無くても良い
    )
    # フローの特徴点を描く
    flow_layer = cv2.circle(
        img=flow_layer,                 # 描く画像
        center=(prev_x, prev_y),        # 円の中心
        radius=5,                       # 円の半径
        color=color[rank].tolist(),     # 描く色
        thickness=1                     # 円の線の太さ
    )

# 元の画像に重ねる
result_img = cv2.add(frame, flow_layer)

```

* cv2.line() cf. ```https://docs.opencv.org/3.4.1/d6/d6e/group__imgproc__draw.html#ga7078a9fae8c7e7d13d24dac2520ae4a2```


* cv2.circle() cf. ```https://docs.opencv.org/3.4.1/d6/d6e/group__imgproc__draw.html#gaf10604b069374903dbd0f0488cb43670```


* cv2.add() cf. ```https://docs.opencv.org/3.4.1/d2/de8/group__core__array.html#ga10ac1bfb180e2cfda1701d06c24fdbd6```



* good_old と good_new を zip() で一緒に回して，さらに enumerate() でインデックス番号を取得しています．


## 結果画像

うまくいくと次のように表示されるかと思います．

<figure class="figure-image figure-image-fotolife" title="丸と線でフローが書かれています．">[f:id:kuri_megane:20180627182829p:plain]<figcaption>丸と線でフローが書かれています．</figcaption></figure>

## 参考資料

* 詳解OpenCV3
[https://www.oreilly.co.jp/books/9784873118376/:embed:cite]

* OpenCV 3.4.1 公式リファレンス
[https://docs.opencv.org/3.4.1/:title]

* numpy 1.14.0 公式リファレンス
[https://docs.scipy.org/doc/numpy-1.14.0/reference/:title]

## ソースコード

この記事で紹介しているソースコードはこちら


[https://github.com/kuri-megane/blog/tree/master/20180628_OpenCV%20%C3%97%20Python%20%C3%97%20%E3%82%AA%E3%83%97%E3%83%86%E3%82%A3%E3%82%AB%E3%83%AB%E3%83%95%E3%83%AD%E3%83%BC%20(Optical%20Flow)%20%E3%81%A7%E7%89%A9%E4%BD%93%E8%BF%BD%E8%B7%A1:embed:cite]


## 更新履歴
- 2018/10/09 にソースコードとサンプル動画を追加しました．