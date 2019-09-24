# 生产器函数，只要有yield关键字
def gen_func():
    yield 1
    yield 2


# 惰性求值，延迟求值提供了可能

def fib(n):
    # 斐波拉契 0  1 1 2 3 5 8
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib1(index):
    re_list = []
    n, a, b = 0, 0, 1
    while n < index:
        re_list.append(b)
        a, b = b, a + b
        n += 1
    return re_list


def gen_fib(index):
    re_list = []
    n, a, b = 0, 0, 1
    while n < index:
        yield b
        a, b = b, a + b
        n += 1


print(fib(10))
print(fib1(10))
print([i for i in gen_fib(10)])


def func():
    return 1


if __name__ == '__main__':
    # 生成器对象，python编译字节码的时候就产生了
    gen = gen_func()  # 返回生成器对象(可迭代)
    for v in gen:
        print(v)
    re = func()
