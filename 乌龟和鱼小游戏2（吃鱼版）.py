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
        self.x = bound(self.x)
        self.y = bound(self.y)
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
        self.x = bound(self.x)
        self.y = bound(self.y)
def bound(x):
    if x < boundary[0]:
        x = boundary[0] - x
    elif x > boundary[1]:
        x = 2*boundary[1] - x
    return (x)

def position_test(position):
    x = position[0]
    y = position[1]
    X = []
    Y = []
    new_pos = []
    for i in [-1,1]:
        x = bound(x+i)
        y = bound(y+i)
        X.append(x)
        Y.append(y)
    for i in X:
        for j in Y:
            new_pos.append([i,j])
    index = 0
    for i in FISH:
        for j in new_pos:
            if i.position() == j:
                index += 1
    if index == len(new_pos):
        return 0
    else:
        return 1
turtle = Turtle()
FISH = []
for i in range(0,10):
    fish = Fish()
    FISH.append(fish)
fish_num = 10
times = 0
while 1:
    turtle.move()
    for i in FISH:
        p = i.position()
        if position_test(p):
            i.move()
        print (i.position(),end = '')
        if turtle.position() == i .position():
            turtle.eat()
            FISH.remove(i)
            fish_num -= 1
            
    print (turtle.position())
    if fish_num and turtle.strength != 0:
        times += 1
        continue
    else:
        print (times)
        break
#还是一只都没抓到！
