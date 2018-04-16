print ('''
           |--- 欢迎进入通讯录程序 ---|
           |--- 1：查询联系人资料  ---|
           |--- 2：插入新的联系人  ---|
           |--- 3：删除已有联系人  ---|
           |--- 4：退出通讯录程序  ---|''')
dirc = {}
code = 0
while 1:
    enter = input('请输入相关的指令代码：')
    if enter.isdigit():
        code = int(enter)
    else:
        print ('输入有误！')
        continue
    if code == 1:
        name = input('请输入联系人姓名：')
        if name in dirc.keys():
            print ('%s ：%s'%(name,dirc[name]))
            print ('\n \n ')
        else:
            print ('该联系人不存在！')
            print ('\n \n ')
    elif code == 2:
        name = input('请输入联系人姓名：')
        if name in dirc.keys():
            while 1:
                answer = input('该联系人已存在%s : %s，是否修改联系方式？回答“是”或“否”'%(name,dirc[name]))
                if answer == '是':
                    phone = input('请输入用户联系电话：')
                    dirc[name] = phone
                    print ('\n \n ')
                    break
                elif answer == '否':
                    print ('\n \n ')
                    break
                else:
                    print ('请输入“是”或“否”')
        else:
            phone = input('请输入用户联系电话：')
            dirc[name] = phone
            print ('\n \n ')
    elif code == 3:
        name = input('请输入联系人姓名：')
        while 1:
            answer = input('请确认是否删除该联系人的联系方式？回答“是”或“否”')
            if answer == '是':
                dirc.pop(name)
                print ('\n \n ')
                break
            elif answer == '否':
                print ('\n \n ')
                break
            else:
                print ('请输入“是”或“否”')
    elif code == 4:
        #answer = input('是否保存本次修改？')这个需要文件部分的知识
        print ('|--- 感谢使用通讯录程序  ---|', end = '\n \n \n')
        break
    else:
        print ('输入有误！')
   

    
