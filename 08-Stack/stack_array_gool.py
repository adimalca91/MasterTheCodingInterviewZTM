'''
Stack Implementation by GOOL

Note: here the pop() takes 0(n) b/c we implement it using the slice operation, but we don't
really need to use it, we can just NOT actually delete the last element and just move
the 'top' field to point to the current last element and if we push we override position where
there is the element we didnt delete / slice - look in the "stack_array_no_builtin_py_functions.py file"
There it takes O(1).

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

    # O(n) - due to the slicing operation in this method.
    def pop(self):
        ''' Pops the top element '''
        if self.size == 0:
            raise Exception("Stack is empty")
        else:
            return_val = self.stack[self.size-1]
            self.stack = self.stack[0:self.size-1] # we don't have to do that, look at Log2Base2 implementation
            self.size -= 1
            return return_val

    # O(n) - looping over the self.stack list and running through all elements.
    def __repr__(self):
        if self.stack == 0:
            return "[]"
        else:
            s = "stack: "
            for element in self.stack[::-1]:
                s += f"{element} -> "
            return s[:-3] + f" , size: {self.size}"



