'''
Sort a Stack via a Helper Stack - GOOL

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
        
        
def sort_stack(stack):
    tmp_stack = Stack()
    if tmp_stack.is_empty():
        tmp = stack.top()
        tmp_stack.push(tmp)
        stack.pop()
    while(stack.is_empty() != True):
        temp = stack.top()
        stack.pop()
        while(tmp_stack.is_empty() != True and temp < tmp_stack.top()):
            stack.push(tmp_stack.top())
            tmp_stack.pop()
        tmp_stack.push(temp)
    return(tmp_stack)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
print(stack)
sorted_stack = sort_stack(stack)
print("sorted stack is: ")
print(sorted_stack)
        