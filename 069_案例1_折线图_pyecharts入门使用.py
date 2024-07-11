from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts
# Line() 创建一个折线图对象
line = Line()
# add_xaxis() 添加x轴的数据
line.add_xaxis(["中国", "美国", "英国"])
# add_yaxis() 添加y轴的数据
line.add_yaxis("GDP", [30, 20, 10])
# 全局配置选项 set_global_opts() 官网查看更多配置选项
line.set_global_opts(
    # 标题 title标题名 pos_left居中 pos_bottom靠近底部1%
    title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_bottom="1%"),
    # 图例 是否展示
    legend_opts=LegendOpts(is_show=True),
    # 工具箱 是否展示
    toolbox_opts=ToolboxOpts(is_show=True),
    # 视觉映射 是否展示
    visualmap_opts=VisualMapOpts(is_show=True)

)
# render() 将代码生成为图像
line.render()

# 全局配置 set_global_opts()
# 标题 图例 工具箱 