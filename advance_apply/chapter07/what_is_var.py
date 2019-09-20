# python和java的变量本质不一样，
# java 变量相当于盒子，而python变量本质上是个指针 指向int类型或 str类型 ,相当于便利贴
a = 1
a = "abc"
# 1. a贴在1上面
# 2.是先生成一个对象，然后使用a便利贴上 体现了动态语言的特性

a = [1,2]
b = a
print(id(a),id(b)) # 两者对象id一样
print( a is b) # 判断两对象是否一样

a = [1,2,3]
b = [1,2,3]
print(a is b)  # False  是两个对象 故不等
print(a == b)  # True

a = 1
b = 1
# python intern 机制，
print(id(a),id(b))
print(a is b)  # True
print(a == b) # True

class A:
    pass

obj_a = A()
if type(obj_a) is A:  # 判断类型推荐isinstance
    print("yes")