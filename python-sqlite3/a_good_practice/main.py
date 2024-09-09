from human import Human
import sqlite3

"""
进行简单的封装，并使用with上下文管理器
with会自动commit和close
"""

def main():
    create_human_table()

    insert_human(Human(1,'张三',20))
    insert_human(Human(2,'李四',21))
    
    get_human_by_id(1)
    get_human_by_id(2)
    
conn = sqlite3.connect(":memory:")
c = conn.cursor()

def create_human_table():
    with conn:
        c.execute(
            """CREATE TABLE human (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER
            )"""
        )

def insert_human(human: Human):
    with conn:
        c.execute(
            "INSERT INTO human VALUES (:id, :name, :age)",
            {"id": human.id, "name": human.name, "age": human.age},
        )


def get_human_by_id(id):
    with conn:
        c.execute("SELECT * FROM human WHERE id=:id", {"id": id})
        print(c.fetchone())

if __name__ == "__main__":
    main()