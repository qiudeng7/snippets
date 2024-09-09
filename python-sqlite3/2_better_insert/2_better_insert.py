"""
在execute中使用两种placeholder，'?' 和 ':dict_key'
使用这两种placeholder可以避免sql注入。
"""

import sqlite3
from human import Human

# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect("test.db")
cursor = conn.cursor()

wang = Human(3,'王五',22)
zhao = Human(4,'赵六',23)


# 这里会按顺序填充问号
cursor.execute("INSERT INTO human VALUES(?,?,?)", (wang.id, wang.name, wang.age))
# 这里是按字典的键填充
cursor.execute(
    "INSERT INTO human VALUES(:id, :name, :age)", {"id": zhao.id, "name": zhao.name, "age": zhao.age}
)


# select
cursor.execute("SELECT * FROM human WHERE name=? ;",(wang.name,))
print(cursor.fetchall())

cursor.execute("SELECT * FROM human WHERE name=:name ;",{"name":zhao.name})
print(cursor.fetchall())


# commit的作用是把当前事务中的所有操作保存到硬盘。
conn.commit()
conn.close()
