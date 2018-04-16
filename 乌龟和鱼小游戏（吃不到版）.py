import random as r

boundary = [0,10]

class Turtle:
    strength = 100
    x = 0
    y = 0
    def position(self):
        return [self.x,self.y]
    def __init__(self):
        self.x = r.randint(0,boundary[1]+1)
        self.y = r.randint(0,boundary[1]+1)
    def move(self):
        self.x += r.choice([-1,1,1,2])
        self.y += r.choice([-1,1,1,2])
        if self.x < boundary[0]:
            self.x = boundary[0] - self.x
        elif self.x > boundary[1]:
            self.x = 2*boundary[1] - self.x
        if self.y < boundary[0]:
            self.y = boundary[0] - self.y
        elif self.y > boundary[1]:
            self.y = 2*boundary[1] - self.y
        self.strength -= 1

    def eat(self):
        self.strength += 20
        if self.strength > 100:
            self.strength = 100
class Fish:
    x = 0
    y = 0
    def position(self):
        return [self.x,self.y]
    def __init__(self):
        self.x = r.randint(0,11)
        self.y = r.randint(0,11)
    def move(self):
        self.x += r.choice([-1,1])
        self.y += r.choice([-1,1])
        if self.x < boundary[0]:
            self.x = boundary[0] - self.x
        elif self.x > boundary[1]:
            self.x = 2*boundary[1] - self.x
        if self.y < boundary[0]:
            self.y = boundary[0] - self.y
        elif self.y > boundary[1]:
            self.y = 2*boundary[1] - self.y

turtle = Turtle()
fish = locals()
for i in range(0,10):
    fish['fish%d'%i] = Fish()
    
fish_num = 10
times = 0
while 1:
    turtle.move()
    for i in range(0,10):
        try:
            fish['fish%d'%i].move()
            print ('%r'%fish['fish%d'%i].position(),end = '')
            if turtle.position() == fish['fish%d'%i].position():
                turtle.eat()
                del fish['fish%d'%i]
                fish_num -= 1
        except KeyError:
            pass
    print (' %d %d %r'%(fish_num,turtle.strength,turtle.position()))
    if fish_num and turtle.strength != 0:
        times += 1
        continue
    else:
        print (times)
        break
        
'''
这个小乌龟这辈子都不能吃到小鱼儿了，但是如果让小鱼儿不能呆在同一个位置或许会好些！
'''






                




