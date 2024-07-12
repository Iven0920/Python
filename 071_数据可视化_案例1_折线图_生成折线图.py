# www.ab173.com https://www.json.cn/jsononline/ json数据格式化
# * 这个更好用https://www.bejson.com/
import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts

# todo 美国
f_us = open("related_data/可视化案例数据/折线图数据/美国.txt", "r", encoding="UTF-8")
us_data = f_us.read()
# 去除不属于json格式的错误部分
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
us_data = us_data[:-2]
# json转字典
us_dict = json.loads(us_data)

# 取趋势字典
us_trend_data = us_dict['data'][0]['trend']

# 获取日期数据 只取2020年的数据 下标314 但不包括314
us_x_data = us_trend_data['updateDate'][:314]

# 获取确诊数据 只取2020年的数据 下标314 但不包括314
us_y_data = us_trend_data['list'][0]['data'][:314]

# todo 日本
jp_us = open("related_data/可视化案例数据/折线图数据/日本.txt", "r", encoding="UTF-8")
jp_data = jp_us.read()
# 去除不属于json格式的错误部分
jp_data = jp_data.replace("jsonp_1629350871167_29498(", "")
jp_data = jp_data[:-2]
# json转字典
jp_dict = json.loads(jp_data)

# 取趋势字典
jp_trend_data = jp_dict['data'][0]['trend']

# 获取日期数据 只取2020年的数据 下标314 但不包括314
jp_x_data = jp_trend_data['updateDate'][:314]

# 获取确诊数据 只取2020年的数据 下标314 但不包括314
jp_y_data = jp_trend_data['list'][0]['data'][:314]

# todo 印度
in_us = open("related_data/可视化案例数据/折线图数据/印度.txt", "r", encoding="UTF-8")
in_data = in_us.read()
# 去除不属于json格式的错误部分
in_data = in_data.replace("jsonp_1629350745930_63180(", "")
in_data = in_data[:-2]
# json转字典
in_dict = json.loads(in_data)

# 取趋势字典
in_trend_data = in_dict['data'][0]['trend']

# 获取日期数据 只取2020年的数据 下标314 但不包括314
in_x_data = in_trend_data['updateDate'][:314]

# 获取确诊数据 只取2020年的数据 下标314 但不包括314
in_y_data = in_trend_data['list'][0]['data'][:314]

# todo 生成图表
line = Line()
line.add_xaxis(us_x_data)
# label_opts 设置不显示y轴数字
line.add_yaxis("美国确诊人数", us_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本确诊人数", jp_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数", in_y_data, label_opts=LabelOpts(is_show=False))

line.set_global_opts(
    title_opts=TitleOpts(title='2020年美日印三国确诊人数对比折线图', pos_left='center', pos_bottom='1%'),
)
line.render("related_data/071_生成折线图.html")