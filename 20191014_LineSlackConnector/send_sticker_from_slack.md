# この記事で紹介すること

この記事では，Slack から LINE Bot で LINE のスタンプを送信します．

サーバー は heroku を使用します．

# できあがるとこんな感じ




---

<b>目次</b>

[:contents]

---


<!-- more -->

# LINE & Slack 連携基礎編

この記事には次の記事の続きです．
LINE と Slack の連携について詳しく知りたいときは，これらの記事を参考にしてください．

1. [アカウント準備編](https://kuri-megane.hatenablog.jp/entry/2019/10/28/190000)
2. [LINE -> Slack の連携編](https://kuri-megane.hatenablog.jp/entry/2019/10/29/190000)
3. [Slack -> LINE の連携編](https://kuri-megane.hatenablog.jp/entry/2019/10/30/190000)



# ソースコード

以下で紹介するソースコードはGithubで公開しています．


[https://github.com/kuri-megane/line-slack-connector-slack2line/tree/release/blog:embed:cite]



## ディレクトリ構成

次のようになっています．

```
slack2line
├── Procfile
├── plugins
│   ├── __init__.py
│   └── send_line.py
├── requirements.txt
├── run.py
├── runtime.txt
└── slackbot_settings.py
```

## 環境構築

pip や pipenv などで次を使えるよう準備してください．

```text
line-bot-sdk
slackbot
```

以下は ubuntu/debian, pip3 の例を紹介します．

```bash
$ sudo apt install python3-pip
$ pip3 install line-bot-sdk
$ pip3 install slackbot
```

## 処理の概要


スタンプを送信するコードは次のようにしました．

Slack から 

```
sticker 送信先 送信するスタンプのpackage_id 送信するスタンプのsticker_id
```

と入力すると送信されます．

値のバリエーションはif文でスペース区切りの文字列の数を確認しています．

```python
@respond_to('sticker (.*)')
def send_sticker_mention_func(message, _):
    """
    LINE スタンプを送信します．
    """

    # slackに投稿されたメッセージのパース
    text = message.body['text']
    parse_msg = text.split(' ')

    # 形式に合っていれば
    if len(parse_msg) == 4:
        _, to, package_id, sticker_id = parse_msg

        # lineに送る
        line_bot_api.push_message(
            to=to,
            messages=StickerSendMessage(
                package_id=package_id,
                sticker_id=sticker_id
            )
        )
```

## ソースコードの作成


その他のソースコードは次のとおりです．

- run.py : Slack Bots を起動します．

```python
from slackbot.bot import Bot


def main():
    bot = Bot()
    bot.run()


if __name__ == "__main__":
    main()
```

- slackbot_settings.py 

Slack Bots の設定を決めます．

認証情報の取得では，環境変数に [1.アカウント準備編](https://kuri-megane.hatenablog.jp/entry/2019/10/28/190000) でメモした値を設定する必要があります．

```python
import os

# トークンを指定
API_TOKEN = os.environ["SLACK_API_TOKEN"]

# このbot宛の標準の応答メッセージ
DEFAULT_REPLY = "このbotにはメッセージを送ることはできません"

# プラグインスクリプトのリスト
PLUGINS = ['plugins']
```

- plugins/send_line.py 

具体的な動作を実装します．

```python
import os

from linebot import LineBotApi
from linebot.models import TextSendMessage
from slackbot.bot import listen_to
from slackbot.bot import respond_to

CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)


@respond_to('sticker (.*)')
def send_sticker_mention_func(message, _):
    """
    LINE スタンプを送信します．
    """

    # slackに投稿されたメッセージのパース
    text = message.body['text']
    parse_msg = text.split(' ')

    # 形式に合っていれば
    if len(parse_msg) == 4:
        _, to, package_id, sticker_id = parse_msg

        # lineに送る
        line_bot_api.push_message(
            to=to,
            messages=StickerSendMessage(
                package_id=package_id,
                sticker_id=sticker_id
            )
        )
        
        # メッセージにスタンプをつける
        message.react('+1')
```



herokuで動かすために更にコードを追加します．

- Procfile

``` 
pbot: python run.py
```

- requirements.txt

```
line-bot-sdk
slackbot
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

ここでは，アプリ名を slack2line としてデプロイしています．

```bash
$ heroku create slack2line
Creating ⬢ slack2line... done
https://slack2line.herokuapp.com/ | https://git.heroku.com/slack2line.git

$ git push heroku master
$ heroku config:set LINE_CHANNEL_ACCESS_TOKEN=[LINE Bot のアクセストークン (ロングターム)] --app slack2line
$ heroku config:set SLACK_API_TOKEN=[slack bots の Bot User OAuth Access Token] --app slack2line
$ heroku ps:scale pbot=1 --app slack2line
```


## 使い方

事前にLINEの投稿先のIDを知っている必要があります．

[2. LINE -> Slack の連携編](https://kuri-megane.hatenablog.jp/entry/2019/10/29/190000) を参考にグループIDまたはトークルームIDを取得します．

```
sticker [送信先] [送信するスタンプのpackage_id] [送信するスタンプのsticker_id]
```

とすると指定した先にスタンプを送信することができます．




## トラブルシューティング

うまく動かないときは，

```bash
$ heroku logs --tail --app line2slack
```

で確認してみてください．

また，アプリのURL (上の例では https://slack2line.herokuapp.com/ ) にアクセスできるかも確認してみてください．

## herokuの無料枠上限に注意

この例ではサーバをずっと動かし続けているため，無料枠の 450h/1ヶ月 (?) or 1000h/1ヶ月 (?) に達する可能性があります．

# 最後に

これらを応用するとSlackとLINEの連携だけでなく，それ以外からのメッセージ投稿ができるはず！

この記事ではLINEスタンプの送信のみを紹介しましたが，メッセージの送信は [Slack -> LINE の連携編](https://kuri-megane.hatenablog.jp/entry/2019/10/30/190000) を参考にしてください．

# 参考記事

[https://qiita.com/_kazuya/items/78961aef30c192a8bd96:embed:cite]

[https://developers.line.biz/ja/docs/messaging-api/:embed:cite]

[https://qiita.com/mizuki_takahashi/items/3f77c2e5b6142563ce66:embed:cite]

[https://qiita.com/sukesuke/items/1ac92251def87357fdf6#%E3%82%B3%E3%83%9E%E3%83%B3%E3%83%89%E5%BD%A2%E5%BC%8F%E3%81%AE%E6%96%87%E5%AD%97%E5%88%97%E3%82%92%E5%8F%97%E3%81%91%E5%8F%96%E3%82%8B:embed:cite]

[https://qiita.com/namutaka/items/233a83100c94af033575:embed:cite]
