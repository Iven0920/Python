from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

map = Map()
data = [
    ("北京市", 99),
    ("湖南省", 199),
    ("上海市", 299),
    ("台湾省", 399),
    ("广东省", 499)
]

# add() 图例 数据列表 地图类型
map.add("测试地图", data, "china")
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        # 是否显示视觉映射
        is_show=True, 
        # 是否允许手动校准范围/是否分段
        is_piecewise=True,
        # 设置颜色区间 最小值 最大值 区域标签 找到RGB16色代码
        pieces=[
            {"min":1, "max":9, "label":"1-9", "color":"#CCFFFF"},
            {"min":10, "max":99, "label":"10-9", "color":"#FF6666"},
            {"min":100, "max":500, "label":"100-500", "color":"#990033"},
        ]
        )
)
map.render("related_data/072_基础地图使用.html")