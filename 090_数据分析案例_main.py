"""
1. 设计一个类 完成数据的封装
2. 设计一个抽象类 定义文件读取的相关功能 用子类实现具体功能
3. 读取文件，生产数据对象
4. 数据计算
5. PyEcharts绘图
"""
from pyecharts.charts import Bar
from pyecharts.options import TitleOpts, LabelOpts, InitOpts
from pyecharts.globals import ThemeType
file_define = __import__("090_数据分析案例_file_define") 
data_define = __import__("090_数据分析案例_data_define")

text_file_reader = file_define.TextFileReader("related_data/2011年1月销售数据.txt")
json_file_reader = file_define.JsonFileReader("related_data/2011年2月销售数据JSON.txt")

jan_data: list = text_file_reader.read_data()
feb_data: list = json_file_reader.read_data()
# 合并为一个list储存
all_data = jan_data + feb_data

# 数据计算
data_dict = {}
for record in all_data:
    if record.date in data_dict.keys():
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money
# print(data_dict)

# 绘图 两种主题选择方式
bar = Bar(init_opts=InitOpts(theme=ThemeType.DARK))
# bar = Bar({"theme":ThemeType.LIGHT})

bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("销售额", list(data_dict.values()), label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts = TitleOpts(title="每日销售额")
)
bar.render("related_data/090_数据分析案例_每日销售额柱状图.html")