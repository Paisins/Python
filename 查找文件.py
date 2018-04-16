import os
import os.path

def search(path, file_name):
    if os.path.exists(path + '\\' + file_name):
        print (path + '\\' + file_name)
    name = os.listdir(path)
    folder = [i for i in name if oa.path.isdir(path + '\\' + i)]
    for i in folder:
        new_path = path + '\\' + i
        search(new_path,file_name)

path = input('请输入待查找的初始目录：')
file_name = input('请输入需要查找的目标文件：')
search(path, file_name)

# os.sep 代表 '\\', 它是系统中的文件分隔符
        
