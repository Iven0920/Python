def print_file_info(file_name):
    f = None
    try:
        f = open(file_name, "r", encoding="UTF-8")
        print(f"原文件的全部内容:\n{f.read()}")
    except FileNotFoundError as e:
        print("文件不存在！")
    finally:
        # * 如果文件打开异常f.close()异常
        # 解决 在外面先定义f为None 后加if判断f类型
        if f:
            f.close()


def append_to_file(file_name, data):
    f = None
    try:
        f = open(file_name, "r", encoding="UTF-8")
        print(f"原文件的全部内容:\n{f.read()}")
    except FileNotFoundError as e:
        print("文件不存在！")
    finally:
        # * 如果文件打开异常f.close()异常
        # 解决 在外面先定义f为None 后加if判断f类型
        if f:
            f.close()

    f = open(file_name, "a", encoding="UTF-8")
    f.write(data)
    f.flush()
    f.close()

    f = open(file_name, "r", encoding="UTF-8")
    f.read()
    print(f"更新后文件的全部内容:\n{f.read()}")