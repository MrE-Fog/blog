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