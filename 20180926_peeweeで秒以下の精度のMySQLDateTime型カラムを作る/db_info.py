import peewee

# todo: 接続情報を記入
HOST = ""
DATABASE = ""
USER = ""
PASSWD = ""

# データベース接続
db = peewee.MySQLDatabase(
    host=HOST,
    database=DATABASE,
    user=USER,
    password=PASSWD
)
