'''
Minimun Stack Implementation

From Udemy - https://www.udemy.com/course/data-structures-and-algorithms-masterclass/learn/lecture/22753981#overview

'''

# push, pop, top and getMin in O(1) Time Complexity

class minStack():
    
    def __init__(self):
        self.stack = []
        self.minstack = []
        
    def __repr__(self):
        if self.stack == [] and self.minstack == []:
            return "Stacks are Empty"
        s = "stack: "
        for elem in self.stack[::-1]:
            s += f"{elem} -> "
        s = s[:-3]
        s += "\nminstack: "
        for minelem in self.minstack[::-1]:
            s += f"{minelem} -> "
        
        return s[:-3]
        
    def push(self, x):
        self.stack.append(x)
        
        if self.minstack == []:
            self.minstack.append(x)
        else:
            if x < self.minstack[-1]:
                self.minstack.append(x)
    
    def pop(self):
        if self.stack == []:
            return []
        if self.stack[-1] == self.minstack[-1]:
            self.minstack.pop()
        self.stack.pop()
        
    def top(self):
        if self.stack == []:
            return None
        return self.stack[-1]
    
    def getMin(self):
        if self.minstack == []:
            return None
        return self.minstack[-1]
        
        

mystack = minStack()
mystack.push(4)
print(mystack)
mystack.push(7)
mystack.push(9)
mystack.push(1)
mystack.push(5)
print(mystack)
print(mystack.getMin())
mystack.pop()
mystack.pop()
print(mystack)
print(mystack.getMin())
mystack.pop()
mystack.pop()
mystack.pop()
print(mystack)
print(mystack.getMin())
            
    
    