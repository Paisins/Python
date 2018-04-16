name_1 = input('请输入需要比较的头一个文件名：')
name_2 = input('请输入需要比较的另一个文件名：')

file_1 = open('D:\\%s'%name_1)
file_2 = open('D:\\%s'%name_2)

num = 0
Num = []

File_1 = list(file_1)
File_2 = list(file_2)

length = len(File_1)          #默认两个文件有相同的行数
i = 0

while i < length:
    if File_1[i] != File_2[i]:
        Num.append(i+1)
        num += 1
    i += 1
    
file_1.close()
file_2.close()

print ('两个文件共有【%d】处不同：'%num)
for j in Num:
    print ('第%d行不一样'%j)

#for i in File_1:
#   if i != File_2.readline():
#       num += 1
#       Num.append(num)
