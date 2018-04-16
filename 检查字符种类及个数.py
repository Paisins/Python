def Check(string):
    List = []
    Count = []
    for i in string:
        if i in List:
            Index = List.index(i)
            Count[Index] += 1
        else:
            List.append(i)
            Count.append(1)
    length = len(List) - 1
    j = 0
    while j <= length:
        print ('字符：%s，有个%d'%(List[j],Count[j]))
        j += 1
    
