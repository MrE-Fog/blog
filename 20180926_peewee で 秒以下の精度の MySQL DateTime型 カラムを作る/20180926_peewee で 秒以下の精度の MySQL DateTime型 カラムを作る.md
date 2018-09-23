# peewee で 秒以下の精度の MySQL DateTime型 カラムを作る

[f:id:kuri_megane:20180923170121p:plain]

[peewee](http://docs.peewee-orm.com/en/latest/) とは python の [ORマッパー](https://qiita.com/yk-nakamura/items/acd071f16cda844579b9) のひとつです．

---

<b>ざっくりまとめると...</b>

* peewee を使って秒以下の値を含むカラムは作れない
* どうしても peewee を使いたいときは自分でフィールドを定義する
* そうでなければ別の手段を使う(直接SQL叩くなど)


---

<b>目次</b>

[:contents]

---


<!-- more -->


## 前提

- ubuntu: 18.04.1
- Anaconda: 4.5.3
    - Python: 3.6
    - peewee: 3.2.3 (conda-forge)
- maria db: mysql  Ver 15.1 Distrib 10.1.34-MariaDB, for debian-linux-gnu (x86_64) using readline 5.2


## 作りたいテーブル

```
+----+----------------------------+
| id | rectime                    |
+----+----------------------------+
|  1 | 2018-09-23 16:05:41.000000 |
+----+----------------------------+
```

秒より小さい精度の値が入ったデータを入れたいと思います．

## 直接SQLを叩くならば

### OK

```sql
CREATE TABLE  hoge_OK(rectime DATETIME(6));
```

とすることで作成できることから，

```sql
INSERT INTO hoge_OK(rectime) values(current_timestamp);
```

試しにデータを入れれば，

```
MariaDB [hoge]> select * from hoge_OK;
+----------------------------+
| rectime                    |
+----------------------------+
| 2018-09-23 16:05:41.000000 |
+----------------------------+
1 row in set (0.00 sec)
```
となります．


### NG

```sql
CREATE TABLE  hoge_NG(rectime DATETIME);
```

と小数点を指定しないと

```sql
INSERT INTO hoge_NG(rectime) values(current_timestamp);
```

としても，

```
MariaDB [hoge]> select * from hoge_NG;
+---------------------+
| rectime             |
+---------------------+
| 2018-09-23 16:09:27 |
+---------------------+
1 row in set (0.00 sec)
```
となります．

### peewee では

本題です．

peeweeでデータベースを作成する場合，データベース接続情報，スキーマ定義，テーブル作成コードを作成します．

- データベース接続情報(db_info.py)

```python
import peewee

# データベース接続(置き換えが必要です)
db = peewee.MySQLDatabase(
    host=HOST,
    database=DATABASE,
    user=USER,
    password=PASSWD
)
```

- スキーマ定義(db_schema.py)

```python
import peewee
import db_info

class BaseModel(peewee.Model):
    class Meta:

        # データベース接続情報
        database = db_info.db

class hoge_peewee(BaseModel):
    rectime = peewee.DateTimeField(
        db_column="rectime",
        formats=[
            "%Y-%m-%d %H:%M:%S.%f"
        ]
    )
```

- テーブル作成コード(make_table.py)

```python
import logging
import db_info
import db_schema

# ログ出力
logger = logging.getLogger('peewee')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

db_info.db.connect()
db_info.db.create_tables(
    [
        db_schema.hoge_peewee
    ]
)
db_info.db.close()
```

make_table.pyを実行すると次のようになります．

```
$ python make_table.py 
('SHOW TABLES', None)
('CREATE TABLE IF NOT EXISTS `hoge_peewee` (`id` INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY, `rectime` DATETIME NOT NULL)', [])
```

データを入れようと，

- データ挿入コード(data_insert.py)

```python
from datetime import datetime
import peewee
import db_info
import db_schema

now = datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f")
print(now)

with db_info.db.transaction():
    db_schema.hoge_peewee.create(
                rectime=now
            )
```

を実行すると，

```
$ python data_insert.py 
2018/09/23 16:47:13.780898
```

問題なく実行できますが，

```
MariaDB [hoge]> select * from hoge_peewee;
+----+---------------------+
| id | rectime             |
+----+---------------------+
|  1 | 2018-09-23 16:47:13 |
+----+---------------------+
1 row in set (0.00 sec)
```

秒までしか入っていません．

いろいろと調べてみましたが，

- Datetimeフィールドをラップして自前でフィールドを用意する
- テーブル作成のみ別の手段にする

が解決策のようです．

## 最後に

紹介したSQLコードで作成したテーブルであれば，peewee経由でも秒以下の精度のあるデータを挿入できます．

## 参考文献


- 
[http://m-shige1979.hatenablog.com/entry/2017/01/25/080000:embed:cite]


- 
[http://docs.peewee-orm.com/en/latest/index.html:title]


- 
[http://docs.peewee-orm.com/en/latest/peewee/models.html#datetimefield-datefield-and-timefield:title]


## 本記事のソースコード
[https://github.com/kuri-megane/blog/tree/master/20180926_peewee%20%E3%81%A7%20%E7%A7%92%E4%BB%A5%E4%B8%8B%E3%81%AE%E7%B2%BE%E5%BA%A6%E3%81%AE%20MySQL%20DateTime%E5%9E%8B%20%E3%82%AB%E3%83%A9%E3%83%A0%E3%82%92%E4%BD%9C%E3%82%8B:embed:cite]

