# 了解闭包
# 了解装饰器的原理

# 例一
def deco(func):
    def inner():
        print('running inner()')
    return inner


@deco
def target():
    print('running target()')

# 如果说target只是inner的引用，也就是说此时target函数代表的就是inner函数
# 而这个实际上是由deco装饰器决定的，因为它返回的是inner，所以target变成了inner
# 从这个角度来讲，一个装饰器是不是应该必须返回一个函数呢？测试一下
# 此时就不能使用target()了，因为target只是一个字符串“running inner()”

# 例二


registry = []


def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


def f3():
    print('running f3()')


def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()

# 结果显示register装饰器的运行要早于main()函数，
# 如果从其他模块中导入装饰器，会在导入模块时立即执行
# 另外，例子中的列表的使用体现出我们可以对所有被某个装饰器装饰的函数做记录，

if __name__ == '__main__':
    # target()
    main()