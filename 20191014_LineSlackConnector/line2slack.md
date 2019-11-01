# なぜ連携させるのか

こんなことがありませんか?

1. いつかはslackをメインで使いたいが，メンバがまだslackに慣れておらず，コミュニケーションの壁を取り払いたい
2. 会社の人のグループLINEから休みの日も通知が来るのが嫌

全く違う例ですが，どちらも連携させれば．．．

# 連携への3つのステップ

記事は3つに分かれています．

1. [アカウント準備編](https://kuri-megane.hatenablog.jp/entry/2019/10/28/190000)
2. LINE -> Slack の連携編 <b>(本記事)</b>
3. [Slack -> LINE の連携編](https://kuri-megane.hatenablog.jp/entry/2019/10/30/190000)

# 2. LINE -> Slack 連携

この記事ではLINEに投稿されたメッセージをSlackに転送できるようにします．

サーバーは heroku を使用します．

---

<b>目次</b>

[:contents]

---


<!-- more -->

## ソースコード

以下で紹介するソースコードはGithubで公開しています．

[https://github.com/kuri-megane/line-slack-connector-line2slack/tree/release/blog:embed:cite]



## ディレクトリ構成

次のようになっています．

```
line2slack
├── Procfile
├── main.py
├── requirements.txt
└── runtime.txt
```

## 環境構築

pip や pipenv などで次を使えるよう準備してください．

```text
Flask
line-bot-sdk
freeze
slackweb
```

以下は ubuntu/debian, pip3 の例を紹介します．

```bash
$ sudo apt install python3-pip
$ pip3 install Flask
$ pip3 install line-bot-sdk
$ pip3 install freeze
$ pip3 install slackweb
```

## ソースコードの作成

- main.py 

```python
import os

import requests
import slackweb
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage

app = Flask(__name__)

# 認証情報の取得
CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
CHANNEL_SECRET = os.environ["LINE_CHANNEL_SECRET"]
WEB_HOOK_LINKS = os.environ["SLACK_WEB_HOOKS_URL"]

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle web hook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


def get_event_info(event):
    """
    トーク情報の取得
    :param event: LINE メッセージイベント
    :return: ユーザID, ユーザ表示名, 送信元トークルームの種別, ルームID
    :rtype: str, str, str, str
    """

    # LINEユーザー名の取得
    user_id = event.source.user_id
    try:
        user_name = line_bot_api.get_profile(user_id).display_name
    except LineBotApiError as e:
        user_name = "Unknown"

    # トーク情報の取得
    if event.source.type == "user":
        msg_type = "個別"
        room_id = None
        return user_id, user_name, msg_type, room_id

    if event.source.type == "group":
        msg_type = "グループ"
        room_id = event.source.group_id
        return user_id, user_name, msg_type, room_id

    if event.source.type == "room":
        msg_type = "複数トーク"
        room_id = event.source.room_id
        return user_id, user_name, msg_type, room_id


@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    """
    Text Message の処理
    """

    slack_info = slackweb.Slack(url=WEB_HOOK_LINKS)

    # トーク情報の取得
    user_id, user_name, msg_type, room_id = get_event_info(event)

    # slack側に投稿するメッセージの加工
    send_msg = "[bot-line] {user_name}さん\n".format(user_name=user_name) \
               + "{msg}\n".format(msg=event.message.text) \
               + "---\n" \
               + "送信元: {msg_type} ( {room_id} )\n".format(msg_type=msg_type, room_id=room_id) \
               + "送信者: {user_name} ( {user_id} )".format(user_name=user_name, user_id=user_id)

    # メッセージの送信
    slack_info.notify(text=send_msg)


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

```

認証情報の取得では，環境変数に [1.アカウント準備編](https://kuri-megane.hatenablog.jp/entry/2019/10/28/190000) でメモした値を設定する必要があります．

get_event_info() では送信されたトークの情報を取得しています．

トークの種類は，

* Botとの1対1トークの「個別」
* グループトーク
* グループではない複数人でのトークグループを「複数トーク」

としています．


herokuで動かすために更にコードを追加します．

- Procfile

``` 
web: python main.py
```

- requirements.txt

```
Flask
line-bot-sdk
freeze
slackweb
```

- runtime.txt

```
python-3.6.8
```

## Gitに追加する

heroku にデプロイするため，Gitレポジトリを作成しコミットしておきます．
以下はその例です．

```bash
$ git init
$ git add . 
$ git commit -m "first commit"
```

## heroku にデプロイ

heroku にアプリを作成し，環境変数を設定します．

heroku CLI を使うので，アカウントの準備ができていない場合は [1.アカウント準備編](https://kuri-megane.hatenablog.jp/entry/2019/10/28/190000) を参考にしてください．

ここでは，アプリ名を line2slack としてデプロイしています．

```bash
$ heroku create line2slack
Creating ⬢ line2slack... done
https://line2slack.herokuapp.com/ | https://git.heroku.com/line2slack.git

$ git push heroku master
$ heroku config:set LINE_CHANNEL_ACCESS_TOKEN=[LINE Bot のアクセストークン (ロングターム)] --app line2slack
$ heroku config:set LINE_CHANNEL_SECRET=[LINE Bot の Channel Secret] --app line2slack
$ heroku config:set SLACK_WEB_HOOKS_URL=[Slack Bots の Incomming Webhook URL] --app line2slack
```

## LINE に heroku のデプロイ先を登録する

作成されたアプリのURLをメモします．
上の例では，https://line2slack.herokuapp.com/ ですので，登録するURLは line2slack.herokuapp.com/callback となります．

[f:id:kuri_megane:20191023162652p:plain]


## 動け！

ここまで来ると，LINEに投稿したメッセージが動くと思います．

[f:id:kuri_megane:20191023224144g:plain]


## 応答メッセージをカスタマイズする & Bot のグループトーク参加を可にする

上の例だといちいち返事が来てしまうので，LINE Bot の設定画面から変更します．

また，グループトークに招待する場合も同じ画面から設定を行います．

[f:id:kuri_megane:20191023164114p:plain]


## トラブルシューティング

うまく動かないときは，

```bash
$ heroku logs --tail --app line2slack
```

で確認してみてください．

また，アプリのURL (上の例では https://line2slack.herokuapp.com/ ) にアクセスできるかも確認してみてください．

# 最後に

次は， [3. Slack -> LINE の連携](https://kuri-megane.hatenablog.jp/entry/2019/10/30/190000) を行います．


# 参考記事

[https://qiita.com/_kazuya/items/78961aef30c192a8bd96:embed:cite]

[https://developers.line.biz/ja/docs/messaging-api/:embed:cite]

[https://qiita.com/namutaka/items/233a83100c94af033575:embed:cite]

