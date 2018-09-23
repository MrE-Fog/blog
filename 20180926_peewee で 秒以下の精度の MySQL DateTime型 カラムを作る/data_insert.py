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