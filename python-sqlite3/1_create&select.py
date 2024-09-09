import sqlite3

# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('test.db')

cursor = conn.cursor()

# 关于sqlite的存储类型和数据类型 https://www.sqlite.org/datatype3.html

cursor.execute("""CREATE TABLE human(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

cursor.execute("INSERT INTO human VALUES(1, '张三', 20)")
cursor.execute("INSERT INTO human VALUES(2, '李四', 21)")

cursor.execute("SELECT * FROM human;")
print(cursor.fetchall())

# 提交事务
conn.commit()
conn.close()