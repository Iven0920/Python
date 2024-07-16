from pymysql import Connection

conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123456"
)

# 游标对象
cursor = conn.cursor()
conn.select_db("world")
# 插入数据
cursor.execute("insert into student values(10001, 'Iven', 23, '男')")
# * 插入数据必须要commit确认
conn.commit()
cursor.close()

# 若不想手动确认，可以在构建连接对象时，添加一个参数
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    autocommit=True
)

cursor = conn.cursor()
conn.select_db("world")
# 自动插入数据
cursor.execute("insert into student values(10002, 'Iven', 23, '男')")
conn.close()