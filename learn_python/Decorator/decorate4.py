import functools
from decorate3 import clock
# python中三个内置的装饰方法的函数分别是property、classmethod、staticmethod
# 还有functools.wraps()也比较常见
# 标准库（functools）比较重要的装饰器是lru_cache和singledispatch

@clock
def fibonacci_1(n):
    if n < 2:
        return n
    return fibonacci_1(n-2) + fibonacci_1(n-1)


@functools.lru_cache()
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

# 从这个例子可以看出，装饰器functools.lru_cache可以缓存接受过的输入值，
# 然后再次输入的时候直接使用，以优化性能，在迭代的时候应该会有很大的作用
# 但是这里有个问题，如果这个函数即便输出同样的参数，可是是一种动态计算过程，
# 也就是说会受到之前输入值的影响时，就不能使用，否则不知道会出什么样的错误

# 另外，functools.lru_cache(maxsize=128, typed=False)可以接收两个参数，
# 前面代表的是缓存的数量，当超过时，会自动删除旧数据，必须是2的幂
# typed是指是否以数据类型做区分，比如说整数分为一类，浮点数分为一类


if __name__ == '__main__':
    print(fibonacci_1(6))
    print('------------')
    print(fibonacci(6))
