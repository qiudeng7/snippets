import pymysql
from config import *

params = {
    'host':RELATION_DB_HOST,
    'port':RELATION_DB_PORT,
    'user':RELATION_DB_USER,
    'password':RELATION_DB_PASSWD,
    'database':RELATION_DB_NAME,
    'charset':"utf8mb4",
    'cursorclass':pymysql.cursors.DictCursor,
}

# params = {
#     'host':'localhost',
#     'port':3306,
#     'user':'root',
#     'password':'123',
#     'database':'boss',
#     'charset':"utf8mb4",
#     'cursorclass':pymysql.cursors.DictCursor,
# }

# 连接数据库
connection = pymysql.connect(**params)


# 创建游标对象
with connection.cursor() as cursor:
    # 执行语句
    cursor.execute("select count(*) from boss")
    # 获取mysql的输出
    print(cursor.fetchall())

# 关闭连接
connection.close()