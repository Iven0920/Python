"""
和文件相关的类
"""
# todo 导入模块中名字带有数字或空格使用内置函数__import__
# __import__(name, globals, locals, fromlist, level)
# 只有name是必选参数，其他都是可选参数，一般情况下直接使用name参数即可。
# fromlist指明需要导入的子模块名，level指定导入方式（相对导入或者绝对导入， 默认两者都支持）

# data_define =  __import__("090_数据分析案例_data_define")
data_define = __import__("090_数据分析案例_data_define", fromlist="Record")
import json

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
            record = data_define.Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
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
            record = data_define.Record(data_dict['date'], data_dict['order_id'], int(data_dict['money']), data_dict['province'])
            record_list.append(record)
        
        f.close()
        
        # 返回数据列表
        return record_list

if __name__ == '__main__':
    text_file_reader = TextFileReader("related_data/2011年1月销售数据.txt")
    list1 = text_file_reader.read_data()
    json_file_reader = JsonFileReader("related_data/2011年2月销售数据JSON.txt")
    list2 = json_file_reader.read_data()
    
    # __str__方法输出数据
    for l in list1:
        print(l)
    for l in list2:
        print(l)