# 实现一个功能，每加入一个数字，计算一次平均值
# 使用类来实现


def Averager():
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


# 这个应该就是所谓的闭包
# def make_averager():
#     series = []
#
#     def averager(new_value):
#         series.append(new_value)
#         total = sum(series)
#         return total / len(series)
#     return averager
# 在上面的高阶函数中，series所在的空间很特别，他不属于全局变量，
# 也不是averager函数的局部变量，而是make_averager的局部变量，
# 尽管执行make_averager函数后，它的作用域已经失效，但是series变量
# 仍然存在，被称为自由变量，而所谓的闭包就是延伸了作用的函数


def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count
    return averager
# nonlocal的作用是将局部变量转换为自由变量，如果不添加这个声明的话，
# 执行时会报错。


if __name__ == '__main__':
    avg = make_averager()
    print(avg(10))
    print(avg(11))
    print(avg(12))