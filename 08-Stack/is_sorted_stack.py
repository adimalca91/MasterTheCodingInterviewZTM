'''
Check if a given stack is sorted

This is my implementation - different than shown in gool

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
        

def is_sorted(stack):
    if stack.is_empty():
        return True
    
    tmp_stack = Stack()
    is_sort = True
    if tmp_stack.is_empty():
        tmp_stack.push(stack.top())        # insert the first item to the temporary helper stack
        stack.pop()
    while stack.is_empty() == False:       # as long as the stack is NOT empty
        tmp = stack.top()
        if tmp > tmp_stack.top():
            is_sort = False
            break
        else:
            tmp_stack.push(tmp)
            stack.pop()                    # the way to "increment" to another iteration
    
    while(tmp_stack.is_empty() == False):
        stack.push(tmp_stack.top())        # NOTE: stack.push(tmp_stack.pop()) returns None
        tmp_stack.pop()
        
    return is_sort
        

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(5)
stack.push(12)
stack.push(92)

print("stack before: ", stack)

print(is_sorted(stack))

print("stack after: ", stack)
