import os.path

file_name = input('请输入要打开的文件（C;\\test.txt）：')
row = input('请输入需要显示改文件的前几行：')

if row.isdigit():
    Row = int(row)
    if os.path.exists(file_name):
        file = open(file_name)
        File = list(file)

        i = 0
        while i < Row:
            print ('文件%s的前%d行的内容如下：'%(file_name, Row))
            print (File[i])
            i += 1
    else:
        print ('文件不存在！')
else:
    print ('行数输入格式有误！')
        
