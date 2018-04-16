def Function(string):
    length = len(string) - 1
    i = 0
    while i <= length//2:
        if string[i] == string[length - i]:
            i += 1
            flag = True
        else:
            flag = False
            break
    if flag:
        print ('是回文联！')
    else:
        print ('不是回文联！')
