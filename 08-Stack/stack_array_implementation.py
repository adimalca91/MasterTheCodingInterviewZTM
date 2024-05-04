'''
Stack Implementation with Arrays
'''

class Stack():
    
    def __init__(self):
        self.stack = []
        
    def __repr__(self):
        if self.stack == []:
            return "Stack is Empty"
        s = "stack: "
        for elem in self.stack[::-1]:
            s += f"{elem} -> "
        return s[:-3]
          
        
    def push(self, val):
        self.stack.append(val)  # using append() method of Arrays / Lists in python
        
    def pop(self):
        if self.stack == []:
            return []
        self.stack.pop()       # using pop() method of Arrays / Lists in python
    
    def top(self):
        if self.stack == []:
            return None
        return self.stack[-1]
    
    
    
my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
print(my_stack)
print(my_stack.top())
my_stack.pop()
print(my_stack)
print(my_stack.top())
my_stack.pop()
print(my_stack)
print(my_stack.top())
my_stack.pop()
print(my_stack)
print(my_stack.top())
my_stack.pop()
print(my_stack)
print(my_stack.top())
my_stack.pop()
print(my_stack)
print(my_stack.top())

        
    
        