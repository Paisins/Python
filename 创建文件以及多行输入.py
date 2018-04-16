file_name = input('请输入文件名：')
file = open('C:\\Users\\dell\\Desktop\\%s.txt'%(file_name),'w')

print('请输入内容【单独输入‘:q’保存退出】：')
file_content = []
while 1:
    enter = input()
    if enter != ':q':
        file_content.append(enter + '\n')
    else:
        file.writelines(file_content)
        file.close()
        break
