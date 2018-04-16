grade = int(input("请输入您的分数："))
temp = grade - 80
if (0<= temp <=20):
    if (temp >= 10):
        print ("A")
    elif (temp >= 0):
        print ("B")
elif (-80< temp < 0):
    if (temp >= -20):
        print ("C")
    elif (temp < -20):
        print ("D")
else:
    print ("输入错误！")
