# ubuntu × windows デュアルブートの設定

---

<b>ざっくりまとめると...</b>

windows のPCに [ubuntu](https://www.ubuntulinux.jp/ubuntu) をインストールする方法がわかります．(きっと)

---

<b>目次</b>

[:contents]


---



<!-- more -->



## 前提

### スペック

| | |
|:---:|:---:|
| 型番 | 富士通 LIFEBOOK WU1/M |
| CPU | Intel Core i5-4200U |
| メモリ | 10.0GB |

* windows 8.1 (無印)

### 今回入れるOS

* ubuntu 16.04.4 LTS

### 必要なもの

* マウスとキーボード (タブレットPCは要注意)
* 空っぽの(4GB以上)USBフラッシュメモリー (またはDVD)
* リカバリディスク(失敗したときに必要)

## 下準備

<b>この先を読み始める前に，必ずPCのバックアップを行ってください．</b>

まず，windowsで必要な設定を行います．

### 高速スタートアップの無効化

無効化することで，ubuntu側からwindows側のファイルを見ることができます．

<figure class="figure-image figure-image-fotolife" title="[コントロールパネル] -&gt; [システムとセキュリティ] を開きます">[f:id:kuri_megane:20180625154351p:plain]<figcaption>[コントロールパネル] -&gt; [システムとセキュリティ] を開きます</figcaption></figure>

<figure class="figure-image figure-image-fotolife" title="[電源オプション] -&gt; [電源ボタンの動作の変更] に進みます">[f:id:kuri_megane:20180625154607p:plain]<figcaption>[電源オプション] -&gt; [電源ボタンの動作の変更] に進みます</figcaption></figure>

<figure class="figure-image figure-image-fotolife" title="[現在利用可能ではない設定を変更します]をクリックします">[f:id:kuri_megane:20180625154841p:plain]<figcaption>[現在利用可能ではない設定を変更します]をクリックします</figcaption></figure>

<figure class="figure-image figure-image-fotolife" title="[高速スタートアップを有効にします]のチェックを外します">[f:id:kuri_megane:20180625155748p:plain]<figcaption>[高速スタートアップを有効にします]のチェックを外します</figcaption></figure>

<figure class="figure-image figure-image-fotolife" title="チェックを外したら[変更の保存]をクリックして閉じます">[f:id:kuri_megane:20180625155922p:plain]<figcaption>チェックを外したら[変更の保存]をクリックして閉じます</figcaption></figure>

### ubuntuをインストールする領域の確保

ここでは Dドライブ の [パーティション](https://www.pc-master.jp/words/partition.html) を変えてインストールする領域を確保します．

<figure class="figure-image figure-image-fotolife" title="[スタートボタン]を右クリックし[ディスクの管理]を選択します">[f:id:kuri_megane:20180625160016p:plain]<figcaption>[スタートボタン]を右クリックし[ディスクの管理]を選択します</figcaption></figure>

<figure class="figure-image figure-image-fotolife" title="[(D:)]を右クリックし，[ボリュームの縮小]を選択します">[f:id:kuri_megane:20180625160710p:plain]<figcaption>[(D:)]を右クリックし，[ボリュームの縮小]を選択します</figcaption></figure>

<figure class="figure-image figure-image-fotolife" title="[縮小する領域のサイズ]でubuntuにどれくらい割り当てたいか入力します">[f:id:kuri_megane:20180625160844p:plain]<figcaption>[縮小する領域のサイズ]でubuntuにどれくらい割り当てたいか入力します</figcaption></figure>

今回は200GBとします．単位がMBですので， 200×1024=204800 と入力します． 実際のubuntuの領域はこれより約8GB程度少なくできます((これは [スワップ領域](http://tech.nikkeibp.co.jp/it/article/Keyword/20071207/289047/) というものができるからです．ubuntu 18.04では必要なくなりました．))．

<figure class="figure-image figure-image-fotolife" title="このようになっていれば◎">[f:id:kuri_megane:20180625161358p:plain]<figcaption>このようになっていれば◎</figcaption></figure>

### LiveUSB LiveDVDの作成

ubuntuのインストールに必要なデータをダウンロードします．

* 日本語が良い方 -> 
[https://www.ubuntulinux.jp/download/ja-remix:title]

* 英語が良い方 -> 
[https://www.ubuntu.com/download/desktop:embed:cite]

ここから， ISO ファイルをインストールしてください．今回は，日本語版をダウンロードします．

次に，外部メディアを焼くソフトをインストールします．今回は，LiveUSB とします((LiveDVDの作り方は

[http://applecom.blog.jp/archives/5918485.html:embed:cite]

などを参考にしてください．))．

空のUSBフラッシュメモリをPCに差し，<b>必要のない別のメディアはすべて外します．</b>

[https://unetbootin.github.io/:title] より，UNetbootin をダウンロードし，実行してください．

<figure class="figure-image figure-image-fotolife" title="[ディスクイメージ]でダウンロードしたISOファイルを選択します">[f:id:kuri_megane:20180625162645p:plain]<figcaption>[ディスクイメージ]でダウンロードしたISOファイルを選択します</figcaption></figure>

<figure class="figure-image figure-image-fotolife" title="[タイプ]を[USBドライブ]に，[ドライブ]で差したUSBメモリを選択します">[f:id:kuri_megane:20180625162703p:plain]<figcaption>[タイプ]を[USBドライブ]に，[ドライブ]で差したUSBメモリを選択します</figcaption></figure>


このあとは画面の指示に従って，焼く作業を続けてください．

## インストール

### LiveUSBから起動する

事前に [ブートメニュー](https://www.pc-master.jp/words/boot.html) の呼び出し方を調べます．

* ブートメニューの開き方 -> 
[http://faq3.dospara.co.jp/faq/show/6289?category_id=1&site_domain=default:embed:cite]

焼いたLiveUSBがPCに差さっていることを確認し，PCを再起動します．再起動を開始したら，調べたキーを押してブートメニューを開きます．

うまく開くとこのような画面がでます．今回試した富士通製PCはF12キーでした．

<figure class="figure-image figure-image-fotolife" title="USBメモリを矢印キーで選択します">[f:id:kuri_megane:20180625164007j:plain]<figcaption>USBメモリを矢印キーで選択します</figcaption></figure>

直後にすかさず，

<figure class="figure-image figure-image-fotolife" title="[Try Ubuntu without installing] を選択します">[f:id:kuri_megane:20180625164354j:plain]<figcaption>[Try Ubuntu without installing] を選択します</figcaption></figure>

### ubuntu をインストールする

起動すると次のような画面がでます．

<figure class="figure-image figure-image-fotolife" title="かっこいいと思います">[f:id:kuri_megane:20180625164548p:plain]<figcaption>かっこいいと思います</figcaption></figure>

インターネットが使用可能な場合は，ここで繋がっていることを確認します．
<figure class="figure-image figure-image-fotolife" title="Wi-Fi の方は右上のマークを押して接続設定をします">[f:id:kuri_megane:20180625164746p:plain]<figcaption>Wi-Fi の方は右上のマークを押して接続設定をします</figcaption></figure>

インストールを開始します．
<figure class="figure-image figure-image-fotolife" title="[Ubuntu16.04LTSのインストール]から始めます">[f:id:kuri_megane:20180625170224p:plain]<figcaption>[Ubuntu16.04LTSのインストール]から始めます</figcaption></figure>

<figure class="figure-image figure-image-fotolife" title="左側から[日本語]を選択し，[続ける]を押します">[f:id:kuri_megane:20180625170326p:plain]<figcaption>左側から[日本語]を選択し，[続ける]を押します</figcaption></figure>

<figure class="figure-image figure-image-fotolife" title="インターネットに繋がっている場合には，アップデートとサードパーティソフトウェアをインストールします">[f:id:kuri_megane:20180625170424p:plain]<figcaption>インターネットに繋がっている場合には，アップデートとサードパーティソフトウェアをインストールします</figcaption></figure>

<figure class="figure-image figure-image-fotolife" title="[UbuntuをWindows...とは別にインストール]を選択します">[f:id:kuri_megane:20180625170607p:plain]<figcaption>[UbuntuをWindows...とは別にインストール]を選択します</figcaption></figure>
ここでwindowsがインストールされているにも関わらず，この項目がない場合には，無理に進めず，windowsが起動できることを確認してください．

<figure class="figure-image figure-image-fotolife" title="[続ける]をクリックします">[f:id:kuri_megane:20180625170813p:plain]<figcaption>[続ける]をクリックします</figcaption></figure>

<figure class="figure-image figure-image-fotolife" title="Tokyoであることを確認し，[続ける]をクリックします">[f:id:kuri_megane:20180625170909p:plain]<figcaption>Tokyoであることを確認し，[続ける]をクリックします</figcaption></figure>

<figure class="figure-image figure-image-fotolife" title="一般的なキーボード配列のPCは，左が[日本語]，右も[日本語]で良いと思います">[f:id:kuri_megane:20180625171008p:plain]<figcaption>一般的なキーボード配列のPCは，左が[日本語]，右も[日本語]で良いと思います</figcaption></figure>

<figure class="figure-image figure-image-fotolife" title="それぞれ英語で設定します">[f:id:kuri_megane:20180625171139p:plain]<figcaption>それぞれ英語で設定します</figcaption></figure>

<figure class="figure-image figure-image-fotolife" title="ここまで来たら待ちます">[f:id:kuri_megane:20180625171215p:plain]<figcaption>ここまで来たら待ちます</figcaption></figure>

<figure class="figure-image figure-image-fotolife" title="無事この画面が出たら終わりです">[f:id:kuri_megane:20180625171300p:plain]<figcaption>無事この画面が出たら終わりです</figcaption></figure>

画面の指示に従って，USBメモリを取り外してください．お疲れ様でした！

## 最後に

次は初期設定をしましょう. 


