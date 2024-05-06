'''
Max Stack Implementation
'''


class maxStack():
    
    def __init__(self):
        self.stack = []
        self.maxstack = []
        
    def __repr__(self):
        if self.stack == [] and self.maxstack == []:
            return "Stacks are Empty"
        s = "stack: "
        for elem in self.stack[::-1]:
            s += f"{elem} -> "
        s = s[:-3]
        s += "\nmaxstack: "
        for minelem in self.maxstack[::-1]:
            s += f"{minelem} -> "
        
        return s[:-3]
        
    def push(self, x):
        self.stack.append(x)
        
        if self.maxstack == []:
            self.maxstack.append(x)
        else:
            if x > self.maxstack[-1]:
                self.maxstack.append(x)
    
    def pop(self):
        if self.stack == []:
            return []
        if self.stack[-1] == self.maxstack[-1]:
            self.maxstack.pop()
        self.stack.pop()
        
    def top(self):
        if self.stack == []:
            return None
        return self.stack[-1]
    
    def getMax(self):
        if self.maxstack == []:
            return None
        return self.maxstack[-1]
        
        

mystack = maxStack()
mystack.push(4)
print(mystack)
mystack.push(7)
mystack.push(9)
mystack.push(1)
mystack.push(5)
print(mystack)
print(mystack.getMax())
mystack.pop()
mystack.pop()
print(mystack)
print(mystack.getMax())
mystack.pop()
print(mystack)
print(mystack.getMax())
mystack.pop()
print(mystack)
print(mystack.getMax())
mystack.pop()
print(mystack)
print(mystack.getMax())
            
    
    