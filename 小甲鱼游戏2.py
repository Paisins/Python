import random
answer = random.randint(1,10)
print ("你有三次机会猜中我心里想的数字，请输入1-10之间的整数：",end = "")
times = 3
guess = 0
while (guess != answer and times > 0):
    temp = input()
    guess = int(temp) 
    times -= 1
    if guess == answer:
        print ("你好幸运，竟然猜到了！")
    elif guess < answer:
        print ("太小了，再试一次！")
    elif guess > answer:
        print ("太大了，再试一次！")
if guess != answer:
    print ("你太笨了，不玩了！")
