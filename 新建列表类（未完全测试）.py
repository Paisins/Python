class CountList:
    def __init__(self, *item):
        self.L = [x for x in item]
        self.count = {}.fromkeys(range(len(item)), 0)

    def __len__(self):
        return len(self.L)

    def __getitem__(self, key):
        if len(self.count) <= key:
            self.count[key] += 1
            return self.L[key]
        else:
            print ('列表中不存在该项')

    def __setitem__(self, key, value):
        self.L[key] = value
        self.count[key] = 0
    def __delitem__(self, key):
        del self.L[key]
        for i in range(key, len(self.L)):
            self.count[i] = self.count[i + 1]
        self.count.pop(len(self.L))

    def counter(self, index):
        return self.count[index]

    def append(self, value):
        self.L.append(value)
        self.count[len(self.count)] = 0

     #在这里pop输入的是key呢？还是value呢？如果是列表输入的应该是key，   
    def pop(self, key):
        temp = self.L[key]
        del self.L[key]
        for i in range(key, len(self.L)):
            self.count[i] = self.count[i + 1]
        self.count.pop(len(self.L))
        return temp
    def remove(self, value):
        key = self.L.index(value)
        del self.L[key]
        for i in range(key, len(self.L)):
            self.count[i] = self.count[i + 1]
        self.count.pop(len(self.L))

    def insert(self, key, value):
        self.L.insert(key, value)
        self.count[len(self.count)] = 0
        for i in range(len(self.L) - key):
            if i:
                self.count[-i] = self.count[-i-1]
        self.count[key] = 0

    def clear(self):
        self.L.clear()
        self.count.clear()

    def reverse(self):
        self.L.reverse()
        for i in range(len(self.L)//2):
            temp = self.count[i]
            self.count[i] = self.count[-(i+1)]
            self.count[-(i+1)] = temp






            












        
        
        
