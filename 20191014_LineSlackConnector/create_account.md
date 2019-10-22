# なぜ連携させるのか

こんなことがありませんか?

1. いつかはslackをメインで使いたいが，メンバがまだslackに慣れておらず，コミュニケーションの壁を取り払いたい
2. 会社の人のグループLINEから休みの日も通知が来るのが嫌

全く違う例ですが，どちらも連携させれば．．．

# 連携への3つのステップ

記事は3つに分かれています．

1. アカウント準備編 (本記事)
2. LINE -> Slack の連携
3. Slack -> LINE の連携

# 1. アカウント準備編 開発に必要なアカウントを用意する

サーバとしてherokuを使うため，heroku CLI も入れます．

---

<b>ざっくりまとめると...</b>

* Line Bot のアカウントを取得します
* Slack Bots のアカウントを取得します
* heroku CLI を導入します


---

<b>目次</b>

[:contents]

---



<!-- more -->


## Line Bot

### プロバイダとBotアカウントの作成

LineのBotアカウントを作成します．


[https://developers.line.biz/:embed:cite]


からアカウント作成を始めましょう．

[f:id:kuri_megane:20191023000122p:plain]

ログインを求められたらLINEアカウントでログインします．

[f:id:kuri_megane:20191023000152p:plain]

初めて LINE Bot を作成する場合，次とは違う画面に遷移するかもしれません．

まず「プロバイダー」を作成するため，プロバイダ名を入力します．
今回は「テスト」と入力しました．

[f:id:kuri_megane:20191023001403p:plain]

中央の Messaging API を選択します．

[f:id:kuri_megane:20191023002407p:plain]

Bot アカウントの設定を進めます．必須の項目をすべて入力します．

[f:id:kuri_megane:20191023002545p:plain]


入力が完了し，各種同意画面で同意するとアカウントが作成されます．

[f:id:kuri_megane:20191023002739p:plain]

基本情報画面では，次の情報をメモしてください．

* Channel ID
* Channel Secret
* アクセストークン (ロングターム) ※再発行ボタンを押して取得

また，Webhook通信を有効化してください．

[f:id:kuri_megane:20191023002853p:plain]

[f:id:kuri_megane:20191023003147p:plain]

[f:id:kuri_megane:20191023003155p:plain]

ここまでできたら LINE Bot の作成は一旦終了です．


## Slack Bots

Botアカウントを作成します．

次のページを参考に作成します．


[https://slack.com/intl/ja-jp/help/articles/115005265703-%E3%83%AF%E3%83%BC%E3%82%AF%E3%82%B9%E3%83%9A%E3%83%BC%E3%82%B9%E3%81%A7%E5%88%A9%E7%94%A8%E3%81%99%E3%82%8B%E3%83%9C%E3%83%83%E3%83%88%E3%81%AE%E4%BD%9C%E6%88%90:embed:cite]


### App の作成

今回はいくつかあるBotの種類のうちAppで行うこととします．

次のページからAppを作成します．

[https://api.slack.com/apps/new:embed:cite]


Appの名前と導入したいワークスペースを選択します．

[f:id:kuri_megane:20191023003539p:plain]


### Incomming Webhook の有効化

Incomming Webhook は LINE -> Slack の連携で必要になります．

まずはじめに，Incomming Webhook を選択し，設定を行います．

[f:id:kuri_megane:20191023003747p:plain]

有効化します．

[f:id:kuri_megane:20191023003827p:plain]

Webhook URL を新規作成します．

[f:id:kuri_megane:20191023003902p:plain]

権限の認証を求められるので，投稿先を選択し，承認します．

無事に作成できたらURLをメモしてください．

[f:id:kuri_megane:20191023003944p:plain]


### Bots の有効化

Bots は Slack -> LINE の連携で必要になります．

[f:id:kuri_megane:20191023004012p:plain]

Bots を新規作成します．

[f:id:kuri_megane:20191023004219p:plain]

表示名とユーザー名を入力します．

[f:id:kuri_megane:20191023004250p:plain]

権限の認証を求められるので，承認します．

[f:id:kuri_megane:20191023004326p:plain]

Botsを無事に作成できたら，OAuthトークンをメモしてください．

[f:id:kuri_megane:20191023004506p:plain]

ここまでできたら Slack Bots の作成は終了です．

## heroku CLI の導入

### heroku アカウントの作成

新規登録の場合，次のページを参考に


[https://www.pytry3g.com/entry/hello-heroku:embed:cite]


アカウントを登録してください．この記事では割愛します．

[https://signup.heroku.com/jp:embed:cite]


### CLI のインストール

次のサイトより，開発環境にあった CLI をインストールします．

[https://devcenter.heroku.com/articles/heroku-cli#download-and-install:embed:cite]

### CLI からログインする

自分のアカウントを使えるよう CLI から heroku にログインします．


[https://devcenter.heroku.com/articles/heroku-cli#getting-started:embed:cite]


```Bash
$ heroku login
```

# 最後に

次は， 2. LINE -> Slack の連携を行います．

