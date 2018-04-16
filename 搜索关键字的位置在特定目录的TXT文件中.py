import os
import os.path

def search(path, keywords):
    dir_name = os.listdir(path)
    length = len(keywords)
    for i in dir_name:
        if os.path.isfile(path + '\\' + i):
            #检查是不是TXT文件
            a = i.split('.')
            a.reverse()
            if a[0] == 'txt':
                #查找关键词
                file = open(path + '\\' + i)
                File = list(file)
                line_numb = 0
                flag = 0
                for line in File:
                    position = []
                    if keywords in line:
                        Numb = line.count(keywords)
                        numb = 0
                        j = 0
                        flag += 1
                        if flag == 1:
                            print ('在文件【%s】中找到关键字【%s】'%(path + '\\' + i, keywords))
                        while numb < Numb :
                            c = line.index(keywords,j)
                            position.append(c)
                            j = c + length
                            numb += 1
                        print ('关键字出现在第%d行，第%r个位置'%(line_numb, position))
                    line_numb += 1
                if flag >1:
                    print ('\n')
        elif os.path.isdir(path + '\\' + i):
            search(path + '\\' + i, keywords)

path = input('请输入当前目录：')
keywords = input('请输入需要搜索的关键字：')

search(path, keywords)


#如果不想输入文件目录，也可以将程序放置到所需要进行搜索的目录，只需要修改以下
#path = os.gecwd()
#其他不变


#比起标准答案来，我的代码行数较少，但是不美观，形状很难看，如果由别人修改也不好理解，所以以后遇到这样的问题，也经常使用函数，将不同的功能打包。
