import time

class Record:
    def __init__(self, value, name):
        self.name = name
        self.value = value
        self.f = open('C:\\Users\\dell\\Desktop\\record.txt', 'w')
    def __get__(self, instance, owner):
        t = time.asctime()
        line = '%s变量于北京时间 %s 被读取， %s = '%(self.name, t, self.name) + str(self.value) + '\n'
        self.In(line)
        return self.value
    def __set__(self, instance, value):
        self.value = value
        t = time.asctime()
        line = '%s变量于北京时间 %s 被修改， %s = '%(self.name, t, self.name) + str(self.value) + '\n'
        self.In(line)
    def In(self, line = ''):
        self.f = open('C:\\Users\\dell\\Desktop\\record.txt')
        List = list(self.f)
        self.f = open('C:\\Users\\dell\\Desktop\\record.txt', 'w')
        List.append(line)
        self.f.writelines(List)
        self.f.close()
        
    
    
