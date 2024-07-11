# 异常bug：程序运行的过程中出现了错误
f = open("/abc.txt", "r", encoding="UTF-8")
# 发生异常: FileNotFoundError
# [Errno 2] No such file or directory: '/abc.txt'
#   File "D:\桌面\Coding\Python\060_了解异常.py", line 2, in <module>
#     f = open("/abc.txt", "r", encoding="UTF-8")
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# FileNotFoundError: [Errno 2] No such file or directory: '/abc.txt'