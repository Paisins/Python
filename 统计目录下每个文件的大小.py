import os
import os.path

def collect(path):
    file_name = os.listdir(path)
    name_size = {}

    for i in file_name:
        name = path + '\\' + i
        size = os.path.getsize(name)
        name_size[i] = str(size) + 'Bytes'

    return name_size

path = input('请输入目录：')
name_size = collect(path)

for i in name_size.keys():
    print ('%s【%s】'%(i, name_size[i]))
