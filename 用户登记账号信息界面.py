import easygui as g

while 1:
    term = ['*用户名','*真实姓名','固定电话','*手机号码','QQ','*E-mail']
    values = g.multenterbox('【*】为必填项','账号中心',fields = term)

    j = 0
    for i in values:
        if '*' in term[j]:
            if i == '':
                g.msgbox('错误！【%s】为必填项'%term[j],'账号中心')
                break
        j += 1
    else:
        g.msgbox('您已完成用户登记！','账号中心')
        break
