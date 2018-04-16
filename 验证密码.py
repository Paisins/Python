print ("您有三次验证机会，请输入您的密码：")
password = 123456
times = 3
while times:
    temp = input()
    temp = temp.replace("*",'')
    print (temp)
    times -= 1
    if temp.isdigit():
        enter = int(temp)
        if enter == password:
            print ("密码输入正确！")
            break
        else:
            print ("密码输入错误，请重新输入！")
            continue
    else:
        print("密码格式有误，请重新输入！")
if enter != password:
    print ('验证次数已用光，请重新开始！')

#replace 比 strip 更好用
