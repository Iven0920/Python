# 表达式：一条具有明确执行结果的代码语句 1+1 2*2
print("1 * 1的结果是:%d" % (1 * 1))
print(f"1 * 1的结果是:{1 * 1}")
print("字符串在Python的类型名是: %s" % type("字符串"))

# 小练习
name = "努力码代码的Iven"
stock_price = 19.99
stock_code = 1234567
stock_price_daily_growth_factor = 1.2
growth_days = 7
print(f"公司:{name},股票代码:{stock_price},当前股价:{stock_price}")
print("每日增长系数:%.1f. 经过%d天的增长后, 股价达到了: %.2f" % (stock_price_daily_growth_factor, growth_days, stock_price * stock_price_daily_growth_factor **growth_days))