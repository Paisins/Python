import os.path

file_name = input('请输入要打开的文件（C:\\test.txt）：')
rows = input('请输入需要显示的行数【格式如 13:21 或 :21 或 21:】：')

[start,end] = rows.split(':')

if start == '':
    A = None
    a = '开始'
elif start.isdigit():
    A = int(start)
    a = '第' + start + '行'
else:
    print ('起始行数输入格式有误！')

if end =='':
    B = None
    b = '末尾'
elif end.isdigit():
    B = int(end)
    b = '第' + end + '行'
else:
    print ('结束行数输入格式有误！')

print ('文件%s从'%file_name + a + '到' + b + '的内容如下：' ,end = '\n \n')


if os.path.exists(file_name):
    file = open(file_name)
    File = list(file)
    for i in File[A:B]:
        print (i)
else:
    print ('文件不存在！')

