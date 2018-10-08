# Name

[20180628_OpenCV × Python × オプティカルフロー (Optical Flow) で物体追跡](https://kuri-megane.hatenablog.jp/entry/2018/06/28/100000) のサンプルコード

# Requirement

- ubuntu 16.04 / 18.04
- anaconda 3

# Tree

The directory structure of the program is as follows. 

プログラムのディレクトリ構造は下記を参考にしてください．

```
self-position-estimation- conf
├── 20180628_OpenCV × Python × オプティカルフロー (Optical Flow) で物体追跡.md
├── README.md (このファイル/This file)
├── debug.avi (サンプル動画/sample video)
├── environment_ubuntu.yml (conda environment file)
├── result.png (サンプル画像/sample image)
├── sample_object_tracking.py
└── test_video_capture.py
```

# Install

## install anaconda

ex. (例)

```bash
$ wget https://repo.anaconda.com/archive/Anaconda3-5.2.0-Linux-x86_64.sh
$ chmod 755 ./Anaconda3-5.2.0-Linux-x86_64.sh
$ ./Anaconda3-5.2.0-Linux-x86_64.sh
```

Plese set path during installsion.

If you need more information, plese reade https://docs.anaconda.com/anaconda/install/linux . 

インストール中にパスを設定するか聞かれますので，その際には設定するように選択してください．

詳しくは，https://docs.anaconda.com/anaconda/install/linux を参考にしてください．

## conda environment

`environment_ubuntu.yml` is a conda environment file．

You will create conda environment by using `$ conda env create -f environment_ubuntu.yml` .
If you need more information, please reade https://conda.io/docs/index.html ．

`environment_ubuntu.yml` が環境構築ファイルです．

`$ conda env create -f environment_ubuntu.yml` で作ることができるでしょう．
詳しくは，https://conda.io/docs/index.html を参考にしてください

# Version

- 2018/10/09 kuri megane edit
