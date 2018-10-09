# OpenCV(anaconda，menpo)で処理できる動画をFFmpegで作る

PythonでOpenCVを使う場合，いくつかのやり方がありますが，anacondaを使う場合には動画の扱いが難しくなります．
紹介するパッケージ [menpo](https://github.com/menpo/conda-opencv3) は既にサポートが終了していますが，[conda-forge](https://anaconda.org/conda-forge/opencv) よりも処理ができる動画の種類が多いようです． 
ここでは，menpoのOpenCVで処理できる動画をFFmpegを使って作成する方法を紹介します．

---

<b>ざっくりまとめると...</b>

* 使用できるコーデックは mjpeg
* 拡張子は avi


---

<b>目次</b>

[:contents]

---


<!-- more -->


## 前提

- ubuntu: 18.04.1
- Anaconda: 4.5.3
    - Python: 3.6
    - opencv: 3.1 (menpo)
- ffmpeg: version 3.4.4-0ubuntu0.18.04.1

記事を読み進めていく上で，動画のコンテナに関する知識があるとわかりやすいと思います．

## Python × OpenCV 

PythonでOpenCVを使う場合，次のやり方が一般的です．

1. 自分でビルド
2. anacondaのパッケージを使う
3. apt-getで入れる 

動画を処理するためには，OpenCVのビルド時にFFmpegのオプションを有効にする必要があり，使えるものは限られています．

しかしながら，これらの手段にはそれぞれ次のような長所と短所があります．

1. 自分でビルド
    - 大変
    - pyenvやanacondaなどではパス通しなどが大変
2. anacondaのパッケージを使う
   - 簡単
   - OpenCVのパッケージはカスタマイズできない
3. apt-getで入れる 
   - 簡単
   - OpenCVのパッケージはカスタマイズできない

anaconda大好きなので，anacondaでも動画処理したいと考えました．

## menpo とは

anacondaのパッケージを公開している組織(?)の一つで，OpenCVに限った話をすると anaconda cloud ではサポートを終了していますが，いまだに第一位のダウンロード数があります．

** **


## 動画処理

ディジタルカメラなどで撮影した動画をそのままOpenCVにかけることはできません．
特にハイビジョン動画などでは [libx264(H.264)](https://ja.wikipedia.org/wiki/X264) が使われていることが多く，OpenCVから利用することは諦めました．

いろいろ試したところ，

* コーデック: [mjpeg (Motion_JPEG)](https://ja.wikipedia.org/wiki/Motion_JPEG)
* 拡張子: [avi](https://ja.wikipedia.org/wiki/Audio_Video_Interleave)

が使えそうだったので，この組み合わせにしました．


## 動画 -> 静止画

動画を作る前に編集を行うことが多いため，まず動画から静止画を切り出します．

```
$ ffmpeg -i input.avi -vcodec png raw_img_%05d.png
```

- -i <file>: 入力動画名
- -vcodec <type>: 出力する画像の形式
    - -vcodec png: png形式
- raw_img_%05d.png: 出力ファイル名，書式指定子で連番数字の桁数を指定

ディジタルカメラなどで撮影した動画の場合，png よりも bmp のほうが容量は大きくなりますがロスが少なくなります．


## 静止画 -> 動画

編集後の静止画を再度動画にします．

```
$ ffmpeg -framerate 30 -start_number 03347 -i raw_img_%05d.png -vcodec mjpeg -qscale 0 -vf scale=640:480 output.avi
```

- -framerate <num>: フレームレートの指定
- -start_number <num>: 後で指定する数字の書式指定子の最初の数
- raw_img_%05d.png: ファイル名，もとのファイル名が`raw_img_00001.png`となっている場合の指定例
- vcodec <type>: コーデックする種類
- qscale 0 : 無損失 ((Please use -q:a or -q:v, -qscale is ambiguous のwarningが出ますが，とりあえずこれでできました))
- vf scale=640:480 : 画像のリサイズ，-1で自動計算(?)
- debug.avi: 出力ファイル名

できる限りロスを少なくしたいため，このようにしました．

## 最後に

どなたかOpenCVの機能をフルで使えるパッケージを…

## 参考資料

- https://www.ffmpeg.org/ffmpeg.html
- https://qiita.com/hirorock/items/2c500c2d46981d8087d9