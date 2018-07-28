# 参数化装饰器
registry = set()


def register(active=True):
    def decorate(func):
        print(f'running register{active}->decorate{func}')
        if active:
            registry.add(func)
        else:
            registry.discard(func)   # 不报错删除
        return func
    return decorate


@register(active=False)
def f1():
    print('running f1()')


@register()
def f2():
    print('running f2()')


def f3():
    print('running f3()')


# 上面的例子可以看出我们实现了装饰器中传入参数，也就是参数化装饰器
# 但值得注意的是，首先register不再是装饰器，而是生成装饰器的工厂函数
# 明显的地方在于register后面加了()，来运行这个函数
# 其次，可以看到接受func参数的地方也发生了变化，变成了decorate函数
# 因此decorate函数才是真正的装饰器
# 其实我比较好奇的是，装饰器一般内部都有一个新的函数，用以返回
# 虽然decorate返回的是原本的func函数，但是如果要对做些处理，必然还是要添加新的函数


def new_register():
    def decorate(func):
        # test1: 没有任何处理
        # return func
        # test2: 做处理
        def new(p):
            print('running new')
            func(p)
        return new

    return decorate


@new_register()
def f4(p):
    print(f'running f4({p})')

# 如这个例子所示，这样参数化的装饰器要比普通的装饰器多了一层函数嵌套
# 同时两个test证明了如果原函数的参数接收很方便


if __name__ == '__main__':
    f4(5)