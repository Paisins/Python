# 单分派泛函数
from functools import singledispatch
import numbers

@singledispatch
def condition(obj):
    print(f'<pre>{obj}</pre>')


@condition.register(str)
def _(text):
    print(f'<str>{text}</str>')


@condition.register(numbers.Integral)
def _(n):  # 此处函数名可修改
    print(f'<int>{n}</int>')

# 好处和缺点都很明显，好处是各种情况分类清楚，修改添加很容易，还可以跨模块
# 缺点也是，太过独立，不同情况无法共用某些局部变量

# 叠放装饰器
# 也就是使用多个装饰器


def a(func):
    def b():
        print('aaa')
        func()
    return b


def b(func):
    def b():
        print('bbb')
        func()
    return b


@a
@b
def c():
    print('ccc')


if __name__ == '__main__':
    # condition('I Love You')
    # condition(5201314)
    # condition([1, 2, 3])
    c()