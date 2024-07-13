from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts, TitleOpts, InitOpts
from pyecharts.globals import ThemeType

# todo 补充：列表的sort方法
# 列表.sort(key=排序函数, reverse=T/F
my_list = [["a", 33], ["b", 55], ["c", 88]]

# 第一种 def自定义函数
def choose_sort_key(element):
    return element[1]

my_list.sort(key=choose_sort_key, reverse=True)
# print(my_list)

# 第二种 lambda匿名函数
my_list.sort(key=lambda element: element[1], reverse=True)
# print(my_list)

# todo 数据处理
# csv编码格式 简体中文 GB2312
f = open("related_data/可视化案例数据/动态柱状图数据/1960-2019全球GDP数据.csv", "r", encoding="GB2312")
# 返回一个列表 每一行为一个元素
data_lines = f.readlines()
f.close()
# 删除表头行
data_lines.pop(0)

# 数据转换字典 格式：{年份：[[国家,gdp], [国家, gdp], ......], 年份：[[国家,gdp], [国家, gdp], ......],年份：[[国家,gdp], [国家, gdp], ......]}
data_dict = {}
for line in data_lines:
    year = int(line.split(',')[0])
    country = line.split(',')[1]
    # 科学计数法全部显示 转float类型
    gdp = float(line.split(',')[2])
    # 想要给年份的列表值用append前 列表必须有定义[] 才能继续添加新元素
    # my_dict = {}
    # my_dict['Iven']
    # 判断字典里有没有指定的Key值
    try:
        data_dict[int(year)].append([country, gdp])
    except KeyError:
        data_dict[int(year)] = []
        data_dict[int(year)].append([country, gdp])
# print(data_dict)

# todo 绘图
# 创建时间线对象 主题选择 两种方法
timeline = Timeline({"theme":ThemeType.CHALK})
# timeline = Timeline(init_opts=InitOpts(theme=ThemeType.CHALK))
# 排序年份 防止字典读取混乱
sorted_year_list = sorted(data_dict.keys())
# print(sorted_year_list)

for year in sorted_year_list:
    data_dict[year].sort(key=lambda element:element[1], reverse=True)
    year_data = data_dict[year][:8]
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0]) # 国家
        y_data.append(round(country_gdp[1] / 100000000, 1)) # gdp round()函数四舍五入只小数点后一位
    
    bar = Bar()
    # 为了让gdp最大的放在最上面 翻转年份和数据
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)",y_data, label_opts=LabelOpts(position="right"))
    bar.reversal_axis()
    bar.set_global_opts(
        # 图像标题
        title_opts=TitleOpts(title=f"{year}年全球前8GDP")
    )
    timeline.add(bar, str(year))

timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)
timeline.render("related_data/077_1960-2019全球GDP前8国家.html")