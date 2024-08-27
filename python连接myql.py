import pymysql

# 连接数据库
connection = pymysql.connect(host='127.0.0.1',
                             port=3306,
                              user='root',
                              password='123',
                              database='boss',
                              charset='utf8mb4',
                              cursorclass=pymysql.cursors.DictCursor)

# 创建游标对象
with connection.cursor() as cursor:
    # 执行语句
    cursor.execute("select count(*) from boss")
    # 获取mysql的输出
    print(cursor.fetchall())

# 关闭连接
connection.close()