from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType

bar1 = Bar()
bar1.add_xaxis(["中国", "美国", "英国"])
bar1.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"))
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["中国", "美国", "英国"])
bar2.add_yaxis("GDP", [50, 10, 50], label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(["中国", "美国", "英国"],)
bar3.add_yaxis("GDP", [90, 40, 70], label_opts=LabelOpts(position="right"))
bar3.reversal_axis()

# 创建时间线 timeline对象 
# 设置时间线主题
timeline = Timeline({"theme": ThemeType.DARK})
timeline.add(bar1, "点1")
timeline.add(bar2, "点2")
timeline.add(bar3, "点3")

# 自动播放 add_schema()
timeline.add_schema(
    # 自动播放时间间隔 单位毫秒
    play_interval=1000,
    # 是否在自动播放时候, 显示时间线
    is_timeline_show=True,
    # 是否自动播放
    is_auto_play=True,
    # 是否循环自动播放
    is_loop_play=True
)

timeline.render("related_data/076_基础时间线柱状图.html")