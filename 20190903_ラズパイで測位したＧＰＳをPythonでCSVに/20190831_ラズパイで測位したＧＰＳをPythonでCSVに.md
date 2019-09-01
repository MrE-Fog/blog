ラズパイで測位したGPSをCSVに記録するPythonプログラムを書きました．

---

<b>ざっくりまとめると...</b>

* ラズパイにPythonで測位したGPSデータをCSVで出力します


---

[:contents]

---



<!-- more -->

## 前準備

- GPSモジュールの準備とラズパイとの接続は[こちら](https://kuri-megane.hatenablog.jp/draft/6kRctr6IM8JukwCPvobqvPvB8po)

## Python環境構築

今回はPythonのライブラリ管理をPipenvにすることとしました．

まずpipとPipenvのインストールします．

```
$ sudo apt install python-pip
$ pip install pipenv
```

次に，環境の作成を作成します．

```
$ pipenv --python 3
```

作成した仮想環境へ入る場合は次のコマンドを叩きます．

```
$ pipenv shell
```


## 必要なライブラリの準備

- pyserial

Pythonでシリアル通信をするためのライブラリです．

```
$ pipenv install pyserial
```

-  micropyGPSのダウンロード

pyserialだけでもPythonでログを取ることはできますが，取扱しやすくするためデータ解析ライブラリを入れます．
Githubからファイルを引っ張ってきて配置するだけで良いです．

```
$ git clone https://github.com/inmcm/micropyGPS.git
```

## プログラムの作成

まず標準出力へ測位の結果を出してみます．

```python
import os
import threading
import time

import serial

from micropy_gps import micropyGPS
from output_csv import write_position

gps = micropyGPS.MicropyGPS()

# 出力のフォーマットは度数とする
gps.coord_format = 'dd'

def run_gps(): 
    """
    GPSモジュールを読み、GPSオブジェクトを更新する
    :return: None
    """ 

    s = serial.Serial('/dev/serial0', 9600, timeout=10)

    # 最初の1行は中途半端なデーターが読めることがあるので、捨てる
    s.readline()

    while True:

        # GPSデーターを読み、文字列に変換する
        sentence = s.readline().decode('utf-8')  

        # 先頭が'$'でなければ捨てる
        if sentence[0] != '$': 
            continue

        # 読んだ文字列を解析してGPSオブジェクトにデーターを追加、更新する
        for x in sentence: 
            gps.update(x)


# 上の関数を実行するスレッドを生成
gps_thread = threading.Thread(target=run_gps, args=())

gps_thread.daemon = True

# スレッドを起動
gps_thread.start()  

while True:

    # ちゃんとしたデーターがある程度たまったら出力する
    if gps.clean_sentences > 20:
        h = gps.timestamp[0] if gps.timestamp[0] < 24 else gps.timestamp[0] - 24
        print('%2d:%02d:%04.1f' % (h, gps.timestamp[1], gps.timestamp[2]))
        print('緯度経度: %2.8f, %2.8f' % (gps.latitude[0], gps.longitude[0]))
        print('海抜: %f' % gps.altitude)
        print('スピード: %f' % gps.speed[2])
        print('測位利用衛星: %s' % gps.satellites_used)
        print('衛星番号: (仰角, 方位角, SN比)')
        for k, v in gps.satellite_data.items():
            print('%d: %s' % (k, v))
        print('')

    # 1秒に1回実行するように
    time.sleep(1.0)
```

実行の仕方

```
$ python logger.py
```


これを実行すると次のように出力されます．

<figure class="figure-image figure-image-fotolife" title="logger.py 実行の出力">[f:id:kuri_megane:20190901222730p:plain]<figcaption>logger.py 実行の出力</figcaption></figure>

### CSVへ出力

上記のプログラムを少しいじって次のように変えます．

logger.py

```python
import os
import threading
import time

import serial

from micropy_gps import micropyGPS
from output_csv import write_position

gps = micropyGPS.MicropyGPS()

# 出力のフォーマットは度数とする
gps.coord_format = 'dd'


def run_gps():
    """
    GPSモジュールを読み、GPSオブジェクトを更新する
    :return: None
    """

    # GPSモジュールを読み込む設定
    s = serial.Serial('/dev/serial0', 9600, timeout=10)

    # 最初の1行は中途半端なデーターが読めることがあるので、捨てる
    s.readline()
    while True:

        # GPSデーターを読み、文字列に変換する
        sentence = s.readline().decode('utf-8')

        # 先頭が'$'でなければ捨てる
        if sentence[0] != '$':
            continue

        # 読んだ文字列を解析してGPSオブジェクトにデーターを追加、更新する
        for x in sentence:
            gps.update(x)


# 上の関数を実行するスレッドを生成
gps_thread = threading.Thread(target=run_gps, args=())

gps_thread.daemon = True

# スレッドを起動
gps_thread.start()

# 結果ファイル作成 dataディレクトリを配下に設置
output_dir = "./data"
os.makedirs(output_dir, exist_ok=True)

while True:

    # ちゃんとしたデーターがある程度たまったら出力する
    if gps.clean_sentences > 20:

        h = gps.timestamp[0] if gps.timestamp[0] < 24 else gps.timestamp[0] - 24
        print('%2d:%02d:%04.1f' % (h, gps.timestamp[1], gps.timestamp[2]))
        print('緯度経度: %2.8f, %2.8f' % (gps.latitude[0], gps.longitude[0]))
        print('海抜: %f' % gps.altitude)
        print('スピード: %f' % gps.speed[2])
        print('測位利用衛星: %s' % gps.satellites_used)
        print('衛星番号: (仰角, 方位角, SN比)')
        for k, v in gps.satellite_data.items():
            print('%d: %s' % (k, v))
        print('')

        # 時刻の変換
        time_str = (
                '20%02d/%02d/%02d %02d:%02d:%02d' %
                (
                    gps.date[2], gps.date[1], gps.date[0],
                    h, gps.timestamp[1], gps.timestamp[2]
                )
        )

        write_position(
            path="./data/log.csv",
            rec_time=time_str,
            lat=gps.latitude[0],
            lon=gps.longitude[0],
            alt=gps.altitude,
            speed=gps.speed[2],
            satellites_used=gps.satellites_used
        )

    # 1秒に1回実行するように
    time.sleep(1.0)
```

output_csv.py

```python
import csv


def write_position(path, rec_time, lon, lat, alt, speed, satellites_used):
    """
    csvに測位結果を書き込みます．
    :param path: 書き込み先
    :type path: str
    :param rec_time: 測位時刻 YYYYMMDD HH:mm:ss
    :type rec_time: str
    :param lon: 経度 世界測地系 度数
    :type lon: float
    :param lat: 緯度 世界測地系 度数
    :type lat: float
    :param alt: 海抜 メートル
    :type alt: float
    :param speed: スピード
    :type speed: float
    :param satellites_used: 測位衛星番号
    :type satellites_used: list
    """

    # 衛星番号の整形
    satellites_str = '-'.join([str(s) for s in satellites_used])

    # 書き込み
    with open(file=path, mode='a') as f:
        writer = csv.writer(f)
        writer.writerow(
            [rec_time, lon, lat, alt, speed, satellites_str]
        )
```

実行の仕方

```
$ python logger.py
```

さきほどの標準出力とは別にCSVファイルが `./data/` 配下にできると思います．

```csv
2019/08/15 22:58:29,139.xxxxxx,35.yyyyy,40.1,18-7-11-8-16-1-26-194-195-22-193-27
2019/08/15 22:58:30,139.xxxxxx,35.yyyyy,40.1,18-7-11-8-16-1-26-194-195-22-193-27
2019/08/15 22:58:31,139.xxxxxx,35.yyyyy,40.1,18-7-11-8-16-1-26-194-195-22-193-27
2019/08/15 22:58:32,139.xxxxxx,35.yyyyy,40.1,18-7-11-8-16-1-26-194-195-22-193-27
2019/08/15 22:58:33,139.xxxxxx,35.yyyyy,40.1,18-7-11-8-16-1-26-194-195-22-193-27
```
(前から順に，測位時刻，経度，緯度，高度，速度，測位した衛星番号 です．)

### 自動実行の設定

シェルスクリプトの作成

自動実行する際は，次のシェルスクリプトを書きます．

start_logger.sh 

```sh
#!/bin/bash

# 測位が開始されるのに少し時間がかかるため1分待つ
sleep 1m

cd {プログラムのルートディレクトリへのパス / Pipfileがあるパス} # いらないかも...?

# パスの登録
PATH=/usr/local/bin:$PATH

# 作成したpipenvでPythonを実行
$HOME/.local/bin/pipenv run python {プログラムのルートディレクトリへのパス / Pipfileがあるパス}/logger.py >> {プログラムのルートディレクトリへのパス / Pipfileがあるパス}/data/stdout.txt 2>&1
```

私の場合は次のようにしました．

```sh
#!/bin/bash

sleep 1m
cd $HOME/evaluate-gps-qzss
PATH=/usr/local/bin:$PATH
$HOME/.local/bin/pipenv run python $HOME/evaluate-gps-qzss/logger.py >> $HOME/evaluate-gps-qzss/data/stdout.txt 2>&1
```

crontabへの登録

ラズパイが起動したら自動的に記録を開始してほしいので，crontabに登録します．

```
$ crontab -e
```

次のように追加します．


```txt
@reboot {シェルスクリプトを置いたパス}/start_logger.sh > {出力先のパス} 2>&1
```

私の場合は次のようにしました．

```txt
@reboot /home/pi/evaluate-gps-qzss/start_logger.sh > /home/pi/evaluate-gps-qzss/data/cron_start_logger.log 2>&1
```


## 最後に

この記事で紹介したソースコードはGithubで公開しています．
[--> こちら](https://github.com/kuri-megane/evaluate-gps-qzss)

今回の記事には続きがあります --> [みちびきを含めて測位した結果とそうでない測位結果，違いはでるのか?]()

## 参考記事

[https://qiita.com/AmbientData/items/fff54c8ac8ec95aeeee6:embed:cite]


[https://qiita.com/y-tsutsu/items/54c10e0b2c6b565c887a:embed:cite]


[https://github.com/inmcm/micropyGPS:embed:cite]


[https://qiita.com/aki-takano/items/3a3c5fca3c185173eda1:embed:cite]


[http://ytyaru.hatenablog.com/entry/2016/12/25/100000:embed:cite]

