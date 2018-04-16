def Function(*x):
    length = len(x)
    Sum = 0
    if x[length - 1] == 5:
        for i in x:
            Sum += i
        return (Sum - 5)*5
    else:
        for i in x:
            Sum += i
        return Sum*3
