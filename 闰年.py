#同时满足以下条件：
#1、年份能被4整除；
#2、年份若是100的整数倍的话，需被400整除，否则是平年。
#举例如下：
#1900年能被4整除，但是因为其是100的整数倍，却不能被400整除，所以是平年；而2000年就是闰年；1904和2004、2008等直接能被4整除且不倍100整除，都是闰年。

while True:
    temp = input("请输入年份：")
    if temp.isdigit():
        year = int(temp)
        if year%4 == 0 and year%100 != 0:
            print ("%d是闰年"%year)
        elif year%4 == 0 and year%400 == 0:
            print ("%d是闰年"%year)
        else:
            print ("%d不是闰年"%year)
        break
    else:
        print ("输入有误，请重新输入！")
