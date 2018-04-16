class Stack:
    
    def __init__(self,a = []):
        self.stack = a
    
    def isEmpty(self):
        if self.stack:
            return True
        else:
            return False

    def push(self,a):
        stack.append(a)
        
    def pop(self):
        return stack.pop()
     
    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            print ('栈中没有数据！')

    def bottom(self):
        if self.stack:
            return self.stack[0]
        else:
            print ('栈中没有数据！')
        
