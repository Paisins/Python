import os
import os.path

def statistics(path):
    document = os.listdir(path)
    Type = {}
    
    for i in document:
        if os.path.isdir(path + '\\' + i):
            Type.setdefault('文件夹',0)
            Type['文件夹'] += 1
        else:
            a = os.path.splitext(i)[1]
            Type.setdefault(a,0)
            Type[a] += 1
    return Type

path = input('输入目录：')
Type = statistics(path)

for i in Type.keys():
    print ('该文件夹下共有类型为【%s】的文件%d个'%(i,Type[i]))


#在开始学编程的时候，很多的method虽然知道，但是总是不会优先使用，而是尽量用自己
#已知的功能去实现，这并非不好，也可以增加熟练度，不过随之而来的是，代码不够简洁
#出现bug的可能增加，所以我还是应该经常使用自己学到的新功能，比如这次的dict.setdefault()
#还有os.path.splitext
