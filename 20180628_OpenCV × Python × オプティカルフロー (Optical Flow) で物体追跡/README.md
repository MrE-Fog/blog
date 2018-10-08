# Name

driving-position-estimation use-optical-flow conf (python ver.)

# Overview

This repo include contents to check action of driving-position-estimation use-optical-flow (python ver. / private) .

このレポジトリは，driving-position-estimation use-optical-flow (python ver. / private) の動作確認に必要なコンテンツが含まれています．

# Requirement

- ubuntu 16.04 / 18.04
- anaconda 3

# Tree

The directory structure of the program is as follows. 

プログラムのディレクトリ構造は下記を参考にしてください．

```
self-position-estimation- conf
├── LICENSE
├── README.md
├── environment_ubuntu.yml  (conda environment file)
├── rectangle.png  (sample image)
└── test_cv2.py (sample OpenCV program)

```

# Install

## install anaconda

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

- 2017/09/03 shishito megane edit
- 2018/07/04 shishito megane edit
