'''
Stack Implementation with Arrays

Without using Python List's built in functions such as append() and pop()

Note - Here we need to define in advance the size of the stack and it's limited - we can't add more once it's full!
'''

class Stack():
    
    def __init__(self, size):
        self.stack = [None] * size
        self.top = -1
        self.size = size
        
    def push(self, val):
        if self.top == self.size -1:
            print("Stack is Full")
        else:
            self.top = self.top + 1
            self.stack[self.top] = val
            
    def pop(self):
        if self.top == -1:
            print("Stack is Empty")
        else:
            print(f"Popped element = {self.stack[self.top]}")
            self.top = self.top - 1 
        
        
        

if __name__=='__main__':

    s = Stack(3)

    s.pop()

    print("Pushing element: ",10)
    s.push(10)
    print("Pushing element: ",20)
    s.push(20)
    print("Pushing element: ",30)
    s.push(30)
    print("Pushing element: ",40)
    s.push(40)

    s.pop()
    s.pop()
    s.pop()
    s.pop()
