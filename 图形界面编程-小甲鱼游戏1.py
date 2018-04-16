import easygui as g
import random

guess = 0
times = 3
answer = random.randint(1,10)

guess = g.integerbox('猜猜我心里想的数字是多少？你有%d次机会'%times,'数字游戏',lowerbound = 1, upperbound = 10)

while 1:
        if guess == answer:
                g.msgbox('恭喜你竟然猜对了！','游戏结束！')
                break
        elif guess < answer and times > 1:
                guess = g.integerbox('你猜的太小了！再试','结果',lowerbound = 1, upperbound = 10)
        elif guess > answer and times > 1:
                guess = g.integerbox('你猜的太大了！','结果',lowerbound = 1, upperbound = 10)
        else:
                break
        times -= 1
print (guess,answer)
if guess != answer:
        g.msgbox('机会用光了哦，下次再玩吧！','游戏结束！')
