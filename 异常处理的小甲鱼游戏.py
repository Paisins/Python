import random

number = random.randint(1,10)
temp = input('请输入一个10以内的数字：')
try:
    guess = int(temp)
    while guess != number:
        temp = input('猜错了，请重新输入吧：')
        guess = int (temp)
        if guess == number:
            print ('厉害，猜对了！')
        else:
            if guess > number:
                print ('大了')
            else:
                print ('小了')
    print ('游戏结束！')
except ValueError:
    print ('你输入的不是数字哦！')
    
except EOFError:
    print ('你刚刚按了Ctrl + D！')
except KeyboardInterrupt:
    print ('你刚刚停止了输入！')
