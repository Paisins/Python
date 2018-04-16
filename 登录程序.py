def Login():
    print ('''
           |--- 新建用户：N/n ---|
           |--- 登录账号：E/e ---|
           |--- 退出程序：Q/q ---|''')
    Name = {}
    while 1:
        enter = input('请输入指令代码：')
        if enter == 'N' or enter == 'n':
            name = input('请输入用户名：')
            while 1:
                if name in Name:
                    name = input ('此用户名已被使用，请重新输入：')
                elif name not in Name:
                    password = input('请输入密码：')
                    Name[name] = password
                    print ('注册成功，赶紧试试登录吧^_^',end = '\n'*3)
                    break
        elif enter == 'E' or enter == 'e':
            name = input('请输入用户名：')
            while 1:
                if name not in Name:
                    name = input('您输入的用户名不存在，请重新输入：')
                elif name in Name:
                    password = input('请输入密码：')
                    if Name[name] == password:
                        print ('欢迎进入%%%系统！',end = '\n'*3)
                        break
        elif enter == 'Q' or enter == 'q':
            print ('您已退出，欢迎下次使用！',end = '\n'*3)
            break
