def gcd(a,b):
    c = 1
    if a < b:
        Max = b
        Min = a
    else:
        Max = a
        Min = b
    while c:
        c = Max%Min
        Max = Min
        Min = c
    return Max
