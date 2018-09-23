# Google Cloud Next in Tokyo '18 参加レポート

[f:id:kuri_megane:20180923021510j:plain]

2018年9月19日~20日に行われた [Google Cloud Next in Tokyo '18](https://cloud.withgoogle.com/next18/tokyo) についてざっくり，本当に非常にざっくりとまとめています．

記事は主にスライドをディジタルカメラで撮影した写真をもとに紹介します．
Google Cloud Platform (GCP) に関する知識はほとんどなく，間違いがあるかもしれません．
その際にはコメントいただければと思います．

## ざっくりまとめると...

2日間の基調講演で新しく発表されたのは次の4点でした．

* 株式会社ファーストリテイリングとの協業を発表(基調講演1日目)
* 新機能「ワークインサイト」，「セキュリティセンター」を発表(基調講演1日目)
* 新機能とアップデート「Cloud Memorystore for Redis 」，「Container Registry 脆弱性スキャン」，「Cloud Source Repositories」を発表(基調講演2日目)
* 日本電気株式会社，NECネッツエスアイ株式会社がサービスパートナーに(基調講演2日目)

記事は非常に長いですので，次の目次から見たい部分に飛ばれることをおすすめします．

---

[:contents]

---


## 1日目

### 基調講演 " Bringing the Cloud to You "

cf. [イベント公式ページ](https://cloud.withgoogle.com/next18/tokyo/my-schedule/session/229874)

基調講演の様子は，youtubeにて日本語と英語の両方が公開されています．

<iframe width="560" height="315" src="https://www.youtube.com/embed/p7dclQSaDbo" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>



##### 株式会社ファーストリテイリングとの協業

ファーストリテイリング社の進める有明プロジェクトとして，需要予測などの面から協業をすることが発表されました．

[f:id:kuri_megane:20180923004357j:plain]

素早い決断のための情報整理とトップの人がディジタルコミュニケーションを進んで行うというファーストリテイリング社社長の柳井氏の言葉が印象に残りました．

cf. [@IT ニュース記事](http://www.atmarkit.co.jp/ait/articles/1809/20/news043.html)

##### 新機能の発表

GCPの新機能として，「ワークインサイト」と「セキュリティセンター」が発表されました．

[f:id:kuri_megane:20180923004502j:plain]

cf. [Google Cloud Japan 公式ブログ](https://cloud-ja.googleblog.com/2018/09/gain-deeper-organizational-insights-and-take-action-with-new-g-suite-features.html)

##### GCP活用事例の紹介

GCPの活用事例が3つ紹介されました．

- Sansan株式会社

自社サービスである名刺のディジタル化に Cloud Vison API を導入することでOCRプロセスのコストが減ったそうです．

[f:id:kuri_megane:20180923004534j:plain]

- 丸紅情報システム株式会社

コールセンター向けサービスに Cloud Speech APIを導入することで会話記録のディジタル化が可能になったそうです．
cf. [クラウド Watch ニュース記事](https://cloud.watch.impress.co.jp/docs/news/1141388.html)

[f:id:kuri_megane:20180923004621j:plain]



- 株式会社プレイド

BigQuery，BigTable を導入することで膨大なデータでも素早い分析が可能になったそうです．

[f:id:kuri_megane:20180923004642j:plain]



---

### GCP で支えるエネルギーデータ活用の新ビジネス、住宅向け IoT サービス基盤 "エナジーゲートウェイ" (1日目ブレイクアウトセクション)

[f:id:kuri_megane:20180923005331j:plain]

cf. [イベント公式ページ](https://cloud.withgoogle.com/next18/tokyo/sessions/session/223266)

このセクションでは，株式会社エナジーゲートウェイ(+東京電力パワーグリッド株式会社) のサービスにおいて，電気消費量のデータ保存に BigTable を採用し，フル活用するための工夫が紹介されました．

##### BigTableとは

[f:id:kuri_megane:20180923005317j:plain]

[f:id:kuri_megane:20180923005350j:plain]

[f:id:kuri_megane:20180923005402j:plain]

((スライドの順番が実際に詳細された順番とは異なる可能性があります．))



##### BigTable をフル活用するための工夫

[f:id:kuri_megane:20180923005444j:plain]

KeyにMACアドレスを採用しているそうですが，MACアドレスはランダムではないため，一度に同じストレージにアクセスすることがないようMACアドレスを逆向きにした文字列をKeyにすることでフル活用が可能になったそうです．



---

## Google Home アプリをサーバーレスで実現 ! ピカチュウトーク開発の裏側をご紹介 (1日目ブレイクアウトセクション)

[f:id:kuri_megane:20180923005715j:plain]

cf. [イベント公式ページ](https://cloud.withgoogle.com/next18/tokyo/sessions/session/223221)

このセクションでは，株式会社ポケモンの Google Home アプリ開発の裏側について紹介されました．

[f:id:kuri_megane:20180923005729j:plain]

[f:id:kuri_megane:20180923005740j:plain]

[f:id:kuri_megane:20180923005751j:plain]

[f:id:kuri_megane:20180923005815j:plain]

[f:id:kuri_megane:20180923005826j:plain]


((スライドの順番が実際に詳細された順番とは異なる可能性があります．))

Dialog Flow などを使うことで，サーバを用意せずに運用することが可能になったそうです．
月2万件のアクセスがあっても運用コストが数千円(?)とは驚きです．


---


## 専門知識なしで、TensorFlow と深層強化学習を学ぼう (1日目ブレイクアウトセクション)

[f:id:kuri_megane:20180923010007j:plain]

cf. [イベント公式ページ](https://cloud.withgoogle.com/next18/tokyo/sessions/session/223408)

こちらのセクションでは，機械学習に関する基本的な知識のおさらいの後，TensorFlowを使ったデモが行われました．

##### 基本的な知識の振り返り

[f:id:kuri_megane:20180923010243j:plain]

[f:id:kuri_megane:20180923010325j:plain]

[f:id:kuri_megane:20180923010403j:plain]

[f:id:kuri_megane:20180923010441j:plain]


大学時代の授業の知識をもとに辛うじて話についていくことができました．

##### ゲーム「Pong」

[f:id:kuri_megane:20180923010551j:plain]

[f:id:kuri_megane:20180923010619j:plain]

[f:id:kuri_megane:20180923010902j:plain]

[f:id:kuri_megane:20180923010937j:plain]

[f:id:kuri_megane:20180923010959j:plain]

[f:id:kuri_megane:20180923011019j:plain]

[f:id:kuri_megane:20180923011046j:plain]

[f:id:kuri_megane:20180923011105j:plain]

[f:id:kuri_megane:20180923011239j:plain]

卓球のようなゲームをコンピュータと機械学習させたAIが対戦し，AIがどのように学習したのか結果が紹介されました．

##### 導入事例

[f:id:kuri_megane:20180923011144j:plain]

[f:id:kuri_megane:20180923011303j:plain]

[f:id:kuri_megane:20180923011317j:plain]

[f:id:kuri_megane:20180923011339j:plain]

[f:id:kuri_megane:20180923011357j:plain]

[f:id:kuri_megane:20180923011557j:plain]

((スライドの順番が実際に詳細された順番とは異なる可能性があります．))

AlphaGo は一般ニュースでも大きく取り上げられ，記憶に新しいですね．


---


# 2日目

## 基調講演 " Bringing the Cloud to You "

cf. [イベント公式ページ](https://cloud.withgoogle.com/next18/tokyo/sessions/session/229874)

cf. [Google Cloud Platform Japan Blog](https://cloudplatform-jp.googleblog.com/2018/09/next-tokyo-2-announcement.html)

基調講演の様子は，youtubeにて日本語と英語の両方が公開されています．

<iframe width="560" height="315" src="https://www.youtube.com/embed/RxdWzSolL9s" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

##### セキュリティツール「Cloud Armor」によるDDoS攻撃ブロックのデモ

[f:id:kuri_megane:20180923011650j:plain]

[f:id:kuri_megane:20180923011731j:plain]


##### GCP活用事例の紹介

株式会社コロプラの活用事例が紹介されました．

[f:id:kuri_megane:20180923011841j:plain]

##### サーバ管理の削減 (Google Cloud 導入のメリット)

他社クラウドやオンプレミスを用いた作業などの膨大化を解決する方法について，Kubernetes (コンテナ化) と Istio (サービス間の通信など)，Cloud Services Plattform (CSP, フルマネージドプラットフォーム) が紹介されました．

[f:id:kuri_megane:20180923012023j:plain]

[f:id:kuri_megane:20180923012128j:plain]

[f:id:kuri_megane:20180923012139j:plain]

[f:id:kuri_megane:20180923012103j:plain]

また，Kubernetes をオンプレミスのデータセンターで管理する Google Kubernetes Engine On-Prem (GKE) のデモが行われました．

[f:id:kuri_megane:20180923012245j:plain]


##### サーバーレスによる運用や開発コストの削減

オープンソース サーバーレス プラットフォーム(Knative) の紹介と GKE Serverless add-on，Serverless Containers on Cloud Functions のデモが行われました．

[f:id:kuri_megane:20180923012408j:plain]

[f:id:kuri_megane:20180923012445j:plain]

[f:id:kuri_megane:20180923012517j:plain]

##### 新機能・アップデートの発表

GCPの新機能とアップデートとして「Cloud Memorystore for Redis 」，「Container Registry 脆弱性スキャン」，「Cloud Source Repositories」がデモを交えながら発表されました．

[f:id:kuri_megane:20180923012731j:plain]

[f:id:kuri_megane:20180923012755j:plain]

[f:id:kuri_megane:20180923012824j:plain]

[f:id:kuri_megane:20180923012851j:plain]

[f:id:kuri_megane:20180923012927j:plain]

[f:id:kuri_megane:20180923012940j:plain]

[f:id:kuri_megane:20180923012955j:plain]

##### 日本電気株式会社，NECネッツエスアイ株式会社がサービスパートナーに

[f:id:kuri_megane:20180923013049j:plain]


[f:id:kuri_megane:20180923013128j:plain]

最後には，Google Cloud 日本代表 阿部 伸一 氏が夜のPartyのお知らせをしました．


---


## Firebase 入門、低コストで迅速な開発を行うには？ (2日目ブレイクアウトセクション)

[f:id:kuri_megane:20180923013356j:plain]

cf. [イベント公式ページ](https://cloud.withgoogle.com/next18/tokyo/sessions/session/223380)

このセクションでは，株式会社みんコレの神楽坂氏からFirebaseが紹介されました．


---

## Web API の育て方：駅すぱあと Web サービスでの Apigee 適用事例 (2日目ブレイクアウトセクション)

[f:id:kuri_megane:20180923013726j:plain]

cf. [イベント公式ページ](https://cloud.withgoogle.com/next18/tokyo/sessions/session/223315)

このセクションでは，株式会社ヴァル研究所の駅すぱあとの Web API について，ApgeeによるAPI管理の工夫が紹介されました．

##### APIエコノミー

[f:id:kuri_megane:20180923013750j:plain]

[f:id:kuri_megane:20180923013803j:plain]

##### APIの育て方

[f:id:kuri_megane:20180923013925j:plain][f:id:kuri_megane:20180923013942j:plain][f:id:kuri_megane:20180923013950j:plain][f:id:kuri_megane:20180923014001j:plain][f:id:kuri_megane:20180923014009j:plain][f:id:kuri_megane:20180923014016j:plain][f:id:kuri_megane:20180923014050j:plain][f:id:kuri_megane:20180923014058j:plain][f:id:kuri_megane:20180923014114j:plain][f:id:kuri_megane:20180923014218j:plain][f:id:kuri_megane:20180923014223j:plain][f:id:kuri_megane:20180923014236j:plain][f:id:kuri_megane:20180923014244j:plain][f:id:kuri_megane:20180923014248j:plain]


いくつかの工夫が紹介されましたが，特に
* APIの公開仕様は最初にしっかり検討する
* 中核となる機能から公開する
* 最初から全部自動化しようとしない
などが大事だと再認識しました．

---


## Google Maps Platform が実現する新たな位置情報サービス体験 (2日目ブレイクアウトセクション)

[f:id:kuri_megane:20180923014518j:plain]

cf. [イベント公式ページ](https://cloud.withgoogle.com/next18/tokyo/sessions/session/223215)

このセクションでは，Google Maps Platform の宣伝がなされました．開発者向けの紹介ではなかったため，スライドの一部のみ紹介します．

[f:id:kuri_megane:20180923014616j:plain][f:id:kuri_megane:20180923014625j:plain][f:id:kuri_megane:20180923014632j:plain][f:id:kuri_megane:20180923014640j:plain][f:id:kuri_megane:20180923014645j:plain][f:id:kuri_megane:20180923014653j:plain][f:id:kuri_megane:20180923014655j:plain]

---

## 画像認識 API と簡単にカスタム機械学習モデルを作成可能な "Cloud AutoML" (2日目ブレイクアウトセクション)

[f:id:kuri_megane:20180923014824j:plain]

cf. [イベント公式ページ](https://cloud.withgoogle.com/next18/tokyo/sessions/session/223445)

このセクションでは，Cloud AutoML Vision の紹介として，いかに簡単に画像の機械学習ができるかが紹介されました．

[f:id:kuri_megane:20180923014904j:plain][f:id:kuri_megane:20180923014908j:plain][f:id:kuri_megane:20180923014927j:plain]


##### Cloud Vision API
[f:id:kuri_megane:20180923014920j:plain]

[f:id:kuri_megane:20180923014938j:plain][f:id:kuri_megane:20180923014942j:plain][f:id:kuri_megane:20180923014949j:plain][f:id:kuri_megane:20180923014959j:plain][f:id:kuri_megane:20180923015003j:plain]

##### Cloud Video Intelligence
[f:id:kuri_megane:20180923014954j:plain]
[f:id:kuri_megane:20180923015007j:plain]

##### Cloud Auto ML
[f:id:kuri_megane:20180923015010j:plain][f:id:kuri_megane:20180923015016j:plain][f:id:kuri_megane:20180923015025j:plain][f:id:kuri_megane:20180923015029j:plain][f:id:kuri_megane:20180923015035j:plain]

質疑応答では，
* ラベルは100まで，クラスは1000まで追加することができる
* 将来的にはより多くのラベルとクラスの追加に対応すること
* アップされた素材は，Googleや第三者が使用することはないこと
* セグメンテーションは2019年対応予定であること
などが紹介されました．

-----

## Expo GREEN，Expo PURPULE

セクションとは別にGCPのサービスや活用事例，パートナー企業のブースがありました．

##### Tokyo Taxi × Google Map API

[f:id:kuri_megane:20180923015902j:plain][f:id:kuri_megane:20180923015757j:plain][f:id:kuri_megane:20180923015934j:plain][f:id:kuri_megane:20180923015950j:plain][f:id:kuri_megane:20180923020016j:plain][f:id:kuri_megane:20180923020028j:plain][f:id:kuri_megane:20180923020033j:plain]

##### その他
[f:id:kuri_megane:20180923020151j:plain][f:id:kuri_megane:20180923020203j:plain][f:id:kuri_megane:20180923020217j:plain][f:id:kuri_megane:20180923020232j:plain]

[f:id:kuri_megane:20180923020354j:plain][f:id:kuri_megane:20180923020418j:plain][f:id:kuri_megane:20180923020450j:plain][f:id:kuri_megane:20180923020529j:plain]

[f:id:kuri_megane:20180923020504j:plain][f:id:kuri_megane:20180923020601j:plain]


## Night Party

最終日の夜には，Google社員による素敵なバンド演奏やクイズを交えたパーティーが開かれました．

[f:id:kuri_megane:20180923021131j:plain]

* バンド演奏

[f:id:kuri_megane:20180923020754j:plain][f:id:kuri_megane:20180923020842j:plain]

* お料理

[f:id:kuri_megane:20180923020859j:plain]

* クイズ

[f:id:kuri_megane:20180923021025j:plain][f:id:kuri_megane:20180923021051j:plain]


## 最後に

ほとんど写真ばかりの長い記事になってしまいましたが，少しでもイベントの様子をお伝えすることができたらと思います．
GCPが何の略かもわからない状態からの申し込みでしたが，様々な製品を駆使していきたいと考えています．
来年のイベントに申し込む際には興味あるセクションを回れるよう，すぐにセクションの予約をしたいと思います．

[f:id:kuri_megane:20180923021635j:plain]
[f:id:kuri_megane:20180923021645j:plain][f:id:kuri_megane:20180923021701j:plain][f:id:kuri_megane:20180923021744j:plain]
