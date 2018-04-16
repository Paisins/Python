import os.path

file_name = input('请输入文件名：')
old = input('请输入需要替换的单词或字符：')
new = input('请输入新的单词或字符：')

if os.path.exists(file_name):
    file = open(file_name)
    File = list(file)

    Count = 0
    for i in File:
        numb = i.count(old)
        Count += numb
        
    print ('文件 %s 中共有%d个【%s】'%(file_name,Count,old))
    print ('您确定要把所有的【%s】替换为【%s】吗？'%(old,new))
    answer = (input('YES/NO：')).lower()

    if answer == 'yes':
        File_new = []
        for i in File:
            if old in i:
                line = i.replace(old,new)
                File_new.append(line)
            else:
                File_new.append(i)
        file_2 = open(file_name, 'w')
        file_2.writelines(File_new)
        file_2.close()
else:
    print ('文件不存在！')

                
