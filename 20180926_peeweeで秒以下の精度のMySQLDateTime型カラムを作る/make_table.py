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