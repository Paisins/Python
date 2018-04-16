print ("1-100随机数")
import random
n = int(input("请输入你所需要的随机数的个数："))
while n:
    n -= 1
    temp = random.randint(1,100)
    print (temp)
