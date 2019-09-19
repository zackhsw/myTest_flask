# array (效率高), 或使用deque
# 相当于c语言的数组
import array
# array 和list的一个重要区别，array只能存放指定的数据类型
my_array = array.array("i")  # i是指定的数据类型
my_array.append(1)
print(my_array)