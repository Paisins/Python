import time


def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked

@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)

# 参数的问题：为什么要使用*args呢？
# 不加*的情况
# [0.12243450s] snooze(0, ., 1, 2, 3) -> None
# [0.00000128s] factorial(1) -> 1
# [0.00004918s] factorial(2) -> 2
# [0.00007698s] factorial(3) -> 6
# [0.00010007s] factorial(4) -> 24
# [0.00012060s] factorial(5) -> 120
# [0.00014155s] factorial(6) -> 720
# 720
# 带有*的情况
# [0.12260086s] snooze(0.123) -> None
# [0.00000128s] factorial(1) -> 1
# [0.00005388s] factorial(2) -> 2
# [0.00008168s] factorial(3) -> 6
# [0.00010649s] factorial(4) -> 24
# [0.00013257s] factorial(5) -> 120
# [0.00016208s] factorial(6) -> 720
# 720

# 不加*和加*基本一致，但是*代表的是多个变量
# 如果传入多个参数则报错，虽然factorial确实只有一个参数，但是它不是clocked函数的引用吗？
# clocked可以传入多个参数，为什么factorial不可以？

# 另外还有几个问题，装饰器遮盖了被装饰函数的__name__和__doc__属性
# 使用@functools.wraps(func)可以避免这个问题


if __name__ == '__main__':
    snooze(.123)
    print(factorial(6))