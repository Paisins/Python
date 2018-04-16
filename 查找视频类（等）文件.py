import os
import os.path

def search(path):
    name = os.listdir(path)
    
    for i in name:
        if os.path.isfile(path + os.sep + i):
            [a,b] = os.path.splitext(path + os.sep + i)
            if b == 'lnk':
                print (1)
            if b in Format:
                print (b)
                videolist.append(path + os.sep + i + '\n \n')
        elif os.path.isdir(path + os.sep + i):
            new_path = path + os.sep + i
            search(new_path)


Format = ['.mp4','.rmvb','.avi','.mkv']

print ('目前支持查询的格式有：', end = '  ')
print ('%r'%Format, end = '\n')
    
path = input('请输入待查找的初始目录：')

videolist = []
search(path)

for i in videolist:
    print (i)
    
file = open('C:\\Users\\dell\\Desktop\\videolist.txt', 'w')
file.writelines(videolist)
file.close()
            
