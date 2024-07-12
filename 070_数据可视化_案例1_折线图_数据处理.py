# www.ab173.com https://www.json.cn/jsononline/ json数据格式化
# * 这个更好用https://www.bejson.com/
import json

f_us = open("related_data/可视化案例数据/折线图数据/美国.txt", "r", encoding="UTF-8")
us_data = f_us.read()
# 去除不属于json格式的错误部分
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
us_data = us_data[:-2]
# json转字典
us_dict = json.loads(us_data)
print(us_dict)
print(type(us_dict))

# 取趋势字典
trend_data = us_dict['data'][0]['trend']
print(trend_data)
print(type(trend_data))

# 获取日期数据 只取2020年的数据 下标314 但不包括314
x_data = trend_data['updateDate'][:314]
print(x_data)

# 获取确诊数据 只取2020年的数据 下标314 但不包括314
y_data = trend_data['list'][0]['data'][:314]
print(y_data)