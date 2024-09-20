import json
from pyecharts.charts import Map
from pyecharts.options import *

f = open("related_data/可视化案例数据/地图数据/疫情.txt", "r", encoding="UTF-8")
data = f.read()
f.close()

# 转字典
data_dict = json.loads(data)
# 取出省份数据
province_data_list = data_dict['areaTree'][0]['children']
# 组装每个省份和确诊人数为元组，将各个省的数据都封装在列表内
data_list = []
for province_data in province_data_list:
    # 省份名称 新版pyecharts必须写清楚省市
    if province_data["name"] == '北京' or province_data["name"] == '天津' or province_data["name"] == '上海' or province_data["name"] == '重庆':
        province_name = province_data["name"] + "市"
    elif province_data["name"] == '西藏' or province_data["name"] == '内蒙古':
        province_name = province_data["name"] + "自治区"
    elif province_data["name"] == '广西' :
        province_name = province_data["name"] + "壮族自治区"
    elif province_data["name"] == '新疆' :
        province_name = province_data["name"] + "维吾尔自治区"
    elif province_data["name"] == '宁夏' :
        province_name = province_data["name"] + "回族自治区"
    elif province_data["name"] == '香港' or province_data["name"] == '澳门':
        province_name = province_data["name"] + "特别行政区"
    else:
        province_name = province_data["name"] + "省"
    # 确诊人数
    province_confirm = province_data["total"]["confirm"]
    data_list.append((province_name, province_confirm))
print(data_list)

# 创建地图对象
map = Map()
# add() 图例 数据列表 地图类型
map.add("各省份确诊人数", data_list, "china")

map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 99, "label": "1-99人", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "label": "100-999人", "color": "#FFFF99"},
            {"min": 1000, "max": 4999, "label": "1000-4999人", "color": "#FF9966"},
            {"min": 5000, "max": 9999, "label": "5000-9999人", "color": "#FF6666"},
            {"min": 10000, "max": 99999, "label": "10000-99999人", "color": "#CC3333"},
            {"min": 100000, "label": "100000+人", "color": "#990033"},
        ]
    )
)
# 设置文件名
map.render("related_data/073_全国疫情地图.html")