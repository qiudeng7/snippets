import pymysql
from config import *

class Database:
    def __init__(self):
        params = {
            'host':RELATION_DB_HOST,
            'port':int(RELATION_DB_PORT),
            'user':RELATION_DB_USER,
            'password':RELATION_DB_PASSWD,
            'database':RELATION_DB_NAME,
            'charset':"utf8mb4",
            'cursorclass':pymysql.cursors.DictCursor,
        }

        # 连接数据库
        print(params)
        self.connection = pymysql.connect(**params)
        
        # 打印版本
        print(self.execute("select VERSION()"))
        
    def execute(self,sql):
        # 创建游标对象
        with self.connection.cursor() as cursor:
            # 执行语句
            cursor.execute(sql)
            # 返回mysql的输出
            return cursor.fetchall()