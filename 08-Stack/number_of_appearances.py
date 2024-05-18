'''
Find the number of appearances of a given value in a given stack

'''

class Stack:

    # O(1)
    def __init__(self):
        self.stack = []
        self.size = 0

    # O(1)
    def is_empty(self):
        '''Checks whether the stack is empty'''
        return self.size == 0

    # O(1)
    def top(self):
        '''Returns the top element of the stack'''
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            return self.stack[self.size-1]

    # O(1)
    def push(self, data):
        self.stack.append(data)  # we use the built in append method here - look at the notes in the stack_array_no_builtin_py_functions.py file
        self.size += 1

    # O(1) 
    def pop(self):
        ''' Pops the top element '''
        if self.size == 0:
            raise Exception("Stack is empty")
        else:
            self.stack.pop()
            self.size -= 1

    # O(n) - looping over the self.stack list and running through all elements.
    def __repr__(self):
        if self.stack == 0:
            return "[]"
        else:
            s = "stack: "
            for element in self.stack[::-1]:
                s += f"{element} -> "
            return s[:-3] + f" , size: {self.size}"
        

def number_appearances(stack, x):
    if stack.is_empty():
        return 0
    counter = 0
    tmp_stack = Stack()
    while stack.is_empty() != True:    # the way to "run / iterate" over a stack
        tmp = stack.top()
        if tmp == x:
            counter +=1
        tmp_stack.push(tmp)
        stack.pop()                   # Decrement the elements in the stack for the while loop
    
    while tmp_stack.is_empty() != True:
        stack.push(tmp_stack.top())
        tmp_stack.pop()
        
    return counter

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(21)
stack.push(2)
stack.push(2)
stack.push(92)

print(stack)

print(number_appearances(stack,13))

print(stack)
