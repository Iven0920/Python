# pymysql 除了使用图形化工具 也可以用编程语言执行SQL来操作数据库

# todo 创建到MySQL的数据库链接
from pymysql import Connection
conn = Connection(
    host = "localhost",         # 主机名(IP)
    port = 3306,                # 端口
    user = "root",              # 账户
    password = "lgz65653420"    # 密码
)
# 获取服务器连接信息
print(conn.get_server_info())

# todo 创建到MySQL的数据库链接
# 获取游标对象 conn.cursor()
cursor = conn.cursor()
# 选择数据库 use = select_db
conn.select_db("test")
# 执行SQL 用python语言可以不写;
cursor.execute("create table test_pymysql(id int);")
cursor.execute("create table test_pymysql2(id int)")

# todo 执行查询性质的SQL语句
conn.select_db("world")
cursor.execute("select * from student")
# 拿到查询结果 fetchall() 返回了一个嵌套元组
results = cursor.fetchall()
print(results)
for r in results:
    print(r)

# todo 关闭链接
conn.close()