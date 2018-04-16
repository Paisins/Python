# 思路，不算8个，算4个，再用总的去减。
red = 3
yellow = 3
green = 6
a = b = c =0     # a,b,c为三个球的数目
for a in range(0,4):
    for b in range(0,5-a):
        for c in range(0,5-a-b):
            if a + b + c == 4 and b <=3:
                 print ("红球：%d，黄球：%d，绿球：%d"%(3-a,3-b,6-c))
    
