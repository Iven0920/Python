def str_reverse(s):
    str_re = s[::-1]
    print(f"原字符串为：{s}")
    print(f"反转字符串为：{str_re}")
    return str_re

def substr(s, x , y):
    piece = s[x: y]
    print(f"原字符串为：{s}")
    print(f"字符串切片为：{piece}")
    return piece