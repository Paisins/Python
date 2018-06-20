# 输出：阶段和第几天
# 从时间模块中处理得到输出结果
# 使用tkinter将结果可视化，并且开机启动
# 优化界面
# 1、添加图标
# 2、每日增加一些文字
# 制作高清图标成了最难的事
import time
import random
import tkinter as tk


def func(start, now):
    tmp = [0, 0]
    tmp[0] = now[0] - start[0]
    tmp[1] = now[1]
    if tmp[0] == 0:
        result = tmp[1] - 19
    elif tmp[0] == 1:
        result = tmp[1] + (30 - 19)
    elif tmp[0] == 2:
        result = tmp[1] + (30 - 19) + 31
    elif tmp[0] == 3:
        result = tmp[1] + (30 - 19) + 31 + 31
    return result


def show(stage, result ):
    with open('D:\My Python\CSDN\Python小程序\data\color.txt') as f:
        color = random.choice(list(f))
    with open('D:\My Python\CSDN\Python小程序\data\名人名言.txt') as f:
        quote = random.choice(list(f))
    win = tk.Tk()
    win.title('ALive Project')
    win.geometry('1000x500+185+130')
    pad = 30
    if result in (10, 20, 30):
        tk.Label(win, font=('OCR A Extended', 30), text='Congratulations! Stage %d finished!' % stage)\
            .pack(side='top', pady=10)
        pad = 0
    tk.Label(win, foreground=color, font=('OCR A Extended', 32),\
             text='Stage %d  Day %d' % (stage, result)).pack(pady=30 + pad)
    tk.Label(win, font=("楷体", 14), text='%s' % quote).pack(pady=20 + pad)
    win.iconbitmap('D:\\My Python\\CSDN\\Python小程序\\data\\图标.ico')
    win.mainloop()


if __name__ == '__main__':
    start = [6, 19]
    now = time.strftime("%m %d").split()
    for i in range(2):
        now[i] = int(now[i])
    result = func(start, now)
    if result <= 10:
        stage = 1
    elif result <= 30:
        stage = 2
        result -= 10
    elif result <= 60:
        stage = 3
        result -= 30
    show(stage, result)



