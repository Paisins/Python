password = input('密码安全性检查，请输入您的密码：')
length = len(password)
SpecialChar = "~!@#$%^&*()_=-/,.?<>;:[]{}\|" 
a = 0
b = 0
c = 0
for i in password:
    if i.isdigit():
        a = 1
    elif i.isalpha():
        b = 1
    elif i in SpecialChar:
        c = 1
n = a + b + c
print (password[0].isalpha())
if length <= 8 or n == 1:
    print ('低')
elif 8 < length <= 16 or n == 2:
    print ('中')
elif length > 16 and n == 3 : #在这里修改了原定的规则，取消了“只能以字母开头”的规定
    print ('高')


