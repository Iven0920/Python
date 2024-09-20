list = [1, 2, 3, 4, 5]
def list_while():
    index = 0
    while index < len(list):
        print(f"取出{list[index]}")
        index += 1
list_while()

def list_for():
    for index in range(len(list)):
        print(f"取出{list[index]}")
    for element in list:
        print(f"取出{element}")
list_for()

# 练习
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
new_list = []
count = 0
while count < len(num_list):
    if num_list[count] % 2 ==0:
        new_list.append(num_list[count])
    count += 1
print(f"新的列表对象中的元素有{new_list}")

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
new_list = []
count = 0
for element in num_list:
    if element % 2 ==0:
        new_list.append(element)
print(f"新的列表对象中的元素有{new_list}")