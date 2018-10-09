# peeweeでJOINしたテーブルの値も取得する

[f:id:kuri_megane:20180923170121p:plain]

[peewee](http://docs.peewee-orm.com/en/latest/) とは python の [ORマッパー](https://qiita.com/yk-nakamura/items/acd071f16cda844579b9) のひとつです．

---

<b>ざっくりまとめると</b>

- peeweeでjoinしたテーブルのカラムのデータを取得する方法
- peewee 2.x の場合は ```naive()```
- peewee 3.x の場合は ```objects()```

---

<b>目次</b>

[:contents]

---


<!-- more -->



## テーブル定義

今回はこんなのを使います．
TableB に TableC を結合します．


```python

import peewee

# 接続情報
db = peewee.MySQLDatabase(
    host=HOST,
    database=DATABASE,
    user=USER,
    password=PASSWD
)

class BaseModel(peewee.Model):
    class Meta:
        database = db


# TableA テーブル
class TableA(BaseModel):
    column_0 = peewee.FixedCharField(
        db_column=Column.TableA.column_0,
    )

    class Meta:
        primary_key = peewee.CompositeKey(
            "column_0"
        )

# TableB テーブル (JOINされるテーブル)
class TableB(BaseModel):
    column_0 = peewee.ForeignKeyField(
        model=TableA,
        field="column_0",
        db_column=Column.TableB.column_0,
    )
    column_1 = peewee.FixedCharField(
        db_column=Column.TableB.column_1
    )
    column_2 = peewee.IntegerField(
        db_column=Column.TableB.column_2
    )
    joined_column = peewee.DoubleField(
        db_column=Column.TableB.joined_column
    )

    class Meta:
        primary_key = peewee.CompositeKey(
            "column_0", "column_1", "column_2"
        )


# TableC テーブル (JOINするテーブル)
class TableC(BaseModel):
    column_0 = peewee.ForeignKeyField(
        model=TableA,
        field="column_0",
        db_column=Column.TableC.column_0,
    )
    column_1 = peewee.FixedCharField(
        db_column=Column.TableC.column_1
    )
    column_2 = peewee.IntegerField(
        db_column=Column.TableC.column_2
    )
    join_column = peewee.IntegerField(
        db_column=Column.TableC.join_column
    )

    class Meta:
        primary_key = peewee.CompositeKey(
            "column_0", "column_1", "column_2"
        )

```

peewee では，JOINした方のカラムの値を取得するのにひと工夫必要です．

## peewee 2.x の場合

```python

# 結合条件
join_cond = (
    (TableC.column_2 == TableB.column_2) 
)
# 検索条件
where_cond = (
    (TableC.column_1 == "xxxx") &
    (TableB.column_1 == "xxxx") &
    (TableC.column_0 == "xxxx") &
    (TableB.column_0 == "xxxx")
)
# クエリ発行
query = TableC.select(
    TableC.column_0,
    TableB.column_0,
    TableC.column_1,
    TableB.column_1,
    TableC.column_2,
    TableB.column_2,
    TableB.joined_column,
    TableC.join_column
).join(
    TableB,
    on=join_cond
).naive(
).where(where_cond)

```

```naive()``` で取得します．

公式ドキュメントには次のようにあります．

> **naive()**
> 
> Return type:	SelectQuery
> Flag this query indicating it should only attempt to reconstruct a single model instance for every row returned by the cursor. If multiple tables were queried, the columns returned are patched directly onto the single model instance.
> 
> Generally this method is useful for speeding up the time needed to construct model instances given a database cursor.

> この問合せにフラグを立てると、カーソルによって戻されたすべての行について1つのモデル・インスタンスのみを再構築しようとします。複数のテーブルが照会された場合、返されたカラムは単一のモデルインスタンスに直接パッチされます。 (Google翻訳)


[http://docs.peewee-orm.com/en/2.10.2/peewee/api.html#SelectQuery.naive:title]




## peewee 3.x の場合

```python

# 結合条件
join_cond = (
    (TableC.column_2 == TableB.column_2) 
)
# 検索条件
where_cond = (
    (TableC.column_1 == "xxxx") &
    (TableB.column_1 == "xxxx") &
    (TableC.column_0 == "xxxx") &
    (TableB.column_0 == "xxxx")
)
# クエリ発行
query = TableC.select(
    TableC.column_0,
    TableB.column_0,
    TableC.column_1,
    TableB.column_1,
    TableC.column_2,
    TableB.column_2,
    TableB.joined_column,
    TableC.join_column
).join(
    TableB,
    on=join_cond
).objects(
    constructor=TableB
).where(where_cond)

```

```objects()``` で取得します．

公式ドキュメントには次のようにあります．

> **objects([constructor=None])**
>
> Return rows as arbitrary objects using the given constructor.

> 指定されたコンストラクタを使用して、行を任意のオブジェクトとして返します。 (Google翻訳)


[http://docs.peewee-orm.com/en/latest/peewee/api.html#BaseQuery.objects:title]



## いずれも次のように取得します

```python

for row in query:
  print(row.join_column)

```


## 最後に

このバージョンの差異に気づかず，ずっとハマってました．

これ以外の差異も [Changes in 3.0](http://docs.peewee-orm.com/en/latest/peewee/changes.html) にまとまっています．

取り扱っているバージョンとドキュメントのバージョンが合っているか，確認大事ですね．


## 参考
* 
[http://docs.peewee-orm.com/en/latest/peewee/api.html#BaseQuery.objects]


* 
[http://docs.peewee-orm.com/en/2.10.2/peewee/api.html#SelectQuery.naive]


* 
[https://a-zumi.net/python-peewee-join-column/]


