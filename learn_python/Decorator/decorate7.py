# 三个内置的装饰方法的函数分别是property、classmethod、staticmethod
class Property:
    def __init__(self, score):
        self._score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value

# 我对property的第一感觉是这个功能有些鸡肋， 它的主要作用是把方法变为属性，
# 而且只是涉及调用和赋值（也许有其他的用处？）
# 作为装饰器使用的几点情况
# 1、适用于隐私属性，外界不能直接调用
# 2、能够实现调用和修改（删除不能实现吗？）

# 其实我之前在小甲鱼的视频中还学到过另一种property的用法
# x = property(fget, fset, fdel)
# 分别对应某个属性的获取，修改和删除


# 类方法classmethod
class Classmethod:
    # 可以正常运行，无需提前设置变量
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def out_date(self):
        print(f'year:{self.year}')
        print(f'year:{self.month}')
        print(f'year:{self.day}')
# 正常情况下该类可以正常使用，但是假如需要需要输入某种格式的时间，如‘2018-7-25’
# 这时候就需要做一些实例化前的处理
# 这个处理过程可以在类外，如
# year,month,day = map(int, string_date.split('-'))
# c = Classmethod(year, month, day)
# c.out_date()
# 但是也可以把这个操作放在类中，作为功能的扩展，而这个是通过类方法实现的

    @classmethod
    def get_date(cls, string_date):
        year, month, day = map(int, string_date.split('-'))
        date = cls(year, month, day)
        return date


# 静态方法staticmethod
# 独立方法，不依赖self，只是简单的把一个函数放进了类中？
# 提供除了__init__之外的创建实例对象的方式（？），哎，等等
# 这不是类方法的功能吗？
class Staticmethod:

    @staticmethod
    def f(n1, n2):
        print(n1, n2)

# 目前来看静态方法的特点是，
# 1、不需要self或cls这样的参数，可以只传入数据参数，
# 2、可以直接用类调用，class.staticmethod(*args)
# 3、也可以在创建实例对象后，通过实例对象调用


if __name__ == '__main__':
    # property:测试
    # p = Property(50)
    # print(p.score)
    # p.score = 60
    # print(p.score)
    # classmethod:测试1
    # c = Classmethod(2018, 7, 25)
    # c.out_date()
    # classmethod:测试2
    # c = Classmethod.get_date('2018-7-25')
    # c.out_date()
    # classmethod:测试1
    Staticmethod.f(1, 2)
    # classmethod:测试2
    s = Staticmethod
    s.f(1, 2)