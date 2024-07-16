import json
from pymysql import Connection

class Record:
    def __init__(self, date, order_id, money, province):
        self.date = date
        self.order_id = order_id
        self.money = money
        self.province = province
    
    def __str__(self):
        return f"{self.date}, {self.order_id}, {self.money}, {self.province}"

class FileReader:
    # 但这里不能正常注释Record类 最好还是纯英文文件
    # def read_data(self) -> list[Record]:
    def read_data(self) -> list:
        """读取文件数据 读的数据转为Record对象 并封装在list内返回即可"""
        pass

class TextFileReader(FileReader):
    def __init__(self, path):
        self.path = path
    
    # 复写
    # def read_data(self) -> list[Record]:
    def read_data(self) -> list:
        f = open(self.path, "r", encoding="UTF-8")
        
        record_list = []

        for line in f.readlines():
            # 消除换行符
            line = line.strip()
            data_list = line.split(",")
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)
        
        f.close()

        # 返回数据列表
        return record_list

class JsonFileReader(FileReader):
    def __init__(self, path):
        self.path = path
    
    # 复写
    # def read_data(self) -> list[Record]:
    def read_data(self) -> list:
        f = open(self.path, "r", encoding="UTF-8")
        
        record_list = []

        for line in f.readlines():
            # 消除换行符 这里可要可不要
            # line = line.strip()
            data_dict = json.loads(line)
            record = Record(data_dict['date'], data_dict['order_id'], int(data_dict['money']), data_dict['province'])
            record_list.append(record)
        
        f.close()
        
        # 返回数据列表
        return record_list

text_file_reader = TextFileReader("related_data/2011年1月销售数据.txt")
json_file_reader = JsonFileReader("related_data/2011年2月销售数据JSON.txt")

jan_data: list[Record] = text_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()
# 合并为一个list储存
all_data : list[Record] = jan_data + feb_data

# todo SQL操作
conn = Connection(
    host="localhost",
    port=3306,
    password="123456",
    user='root',
    autocommit=True
)

cursor = conn.cursor()
conn.select_db("py_sql")
for record in all_data:
    # * 三种长字符串换行显示
    # 1.第一行末尾加\
    sql = f"insert into orders(order_date, order_id, money, province) \
    values('{record.date}', '{record.order_id}', {record.money}, '{record.province}')"
    # 2.三个"
    sql = f'''insert into orders(order_date, order_id, money, province) \
    values("{record.date}", "{record.order_id}", {record.money}, "{record.province}")'''
    # 3.三个'
    sql = f"""insert into orders(order_date, order_id, money, province) \
    values('{record.date}', '{record.order_id}', {record.money}, '{record.province}')"""
    # print(sql)
    cursor.execute(sql)
conn.close()

# 课后作业
f = open("related_data/098_2011年2月销售数据JSON.txt", "a", encoding="UTF-8")

conn = Connection(
    host="localhost",
    port=3306,
    password="123456",
    user='root',
    autocommit=True
)
cursor = conn.cursor()
conn.select_db("py_sql")
cursor.execute("select * from orders")
# 返回一个元组
results = cursor.fetchall()
# print(results)

# 作业所示的文件并不是正式的json格式 所以以字典转str格式写入
# data_list = []
for data in results:
    # 从SQL里拿出的日期是datetime.date类型 
    year_month = str(data[0])[:7]
    if year_month == "2011-02":
            order_date = str(data[0])
            order_id = data[1]
            money = data[2]
            province = data[3]

            data_dict = {}
            data_dict['date'] = order_date
            data_dict['order_id'] = order_id
            data_dict['money'] = money
            data_dict['province'] = province
            
            str_data_dict = str(data_dict) + "\n"
            f.write(str_data_dict)
            # data_list.append(data_dict)

# json_list = json.dumps(data_list, ensure_ascii=False)
# f.write(json_list)

f.flush()
f.close()
conn.close()