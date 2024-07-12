import json
from pyecharts.charts import Map
from pyecharts.options import *

f = open("related_data/可视化案例数据/地图数据/疫情.txt", "r", encoding="UTF-8")
data = f.read()
f.close()


# 转字典
data_dict = json.loads(data)
# 取出省份数据
henan_data_list = data_dict['areaTree'][0]['children'][3]['children']
# 组装每个省份和确诊人数为元组，将各个省的数据都封装在列表内
city_data_list = []
for city_data in henan_data_list:
    # 省份名称 新版pyecharts必须写清楚省市
    city_name = city_data["name"] + "市"
    # 确诊人数
    city_confirm = city_data["total"]["confirm"]
    city_data_list.append((city_name, city_confirm))
print(city_data_list)
# 手动添加济源市的数据
city_data_list.append(("济源市", 5))

# 创建地图对象
# add() 图例 数据列表 地图类型
map = Map()
map.add("河南省各市确诊人数", city_data_list, "河南")

map.set_global_opts(
    # title_opts 地图标题
    title_opts=TitleOpts(title="河南省疫情地图"),
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
map.render("related_data/074_河南省疫情地图.html")