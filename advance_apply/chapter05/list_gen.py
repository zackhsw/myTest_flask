# 列表生成式（列表推导式）
# 1.取奇数
odd_list = [i for i in range(12) if i % 2 == 1]


# 2.复杂逻辑
def handle_item(item):
    return item * item


odd_list = [handle_item(i) for i in range(12) if i % 2 == 1]

# 列表生成式性能高于列表操作，注意可读性
print(type(odd_list))
print(odd_list)

# 生成器
odd_genr = (i for i in range(12) if i % 2 == 1)
print(type(odd_genr))
for i in odd_genr:
    print(i)

# 字典推导式
mydict = {"jack": 33, "rose": 32, "andy": 44, "bill": 31}
reversed_dict = {v: k for k, v in mydict.items()}
print(reversed_dict)

# 集合推导式
my_set = {k for k, v in mydict.items()}
print(type(my_set))
print(my_set)