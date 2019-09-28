def gen_func():
    # 1.可以产出值，2.可以接收值（调用方法传递进来的值）
    try:
        yield "http://www.baidu.com"
    except GeneratorExit:
        pass

    yield 2
    yield 3
    return "ending"

if __name__ == '__main__':
    gen = gen_func()
    print(next(gen))
    # gen.close()
    next(gen)  # 抛出异常 StopIteration
