'''
Interview Question from Google

Implement a Queue using 2 Stacks

Level - Easy

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
        
    
    


'''

Implementing a Queue using 2 stacks where the Insertion / push operation in efficient
but the pop operation is not - 0(n) - b/c we need to 'traverse' through all elements
in the main stack and move them to the helper stack

''' 

class QueueUsingStacksInsert():
    
    def __init__(self):
        self.main_stack = Stack()
        self.helper_stack = Stack()
        
    def push(self,x):
        self.main_stack.push(x)
        
    def pop(self):
        
        while(self.main_stack.is_empty() == False):   # 'Traverse' through all elements in stack
            last = self.main_stack.top()
            self.main_stack.pop()
            self.helper_stack.push(last)
            
            # self.helper_stack.push(self.main_stack.pop())  # NOTE: this does not work correctly so I do it in 3 steps above
        
        self.helper_stack.pop()
        
        while(self.helper_stack.is_empty() == False):
            last2 = self.helper_stack.top()
            self.helper_stack.pop()
            self.main_stack.push(last2)
            
    def peek(self):
        
        if (self.main_stack.is_empty()):
            return []
        else:
            while(self.main_stack.is_empty() == False):
                last = self.main_stack.top()
                self.main_stack.pop()
                self.helper_stack.push(last)
        
            top = self.helper_stack.top()
        
            while(self.helper_stack == False):
                last2 = self.helper_stack.top()
                self.helper_stack.pop()
                self.main_stack.push(last2)
                
            return top
        
    def is_q_empty(self):
        if self.main_stack.is_empty():
            return True
        return False
    
    
    
    # O(n) - looping over the self.stack list and running through all elements.
    def __repr__(self):
        if self.main_stack.size == 0:
            return "[]"
        else:
            q = "Queue: "
            for element in self.main_stack.stack:
                q += f"{element} -> "
            return q[:-3] + f" , size: {self.main_stack.size}"
    
    

q = QueueUsingStacksInsert()

q.push(1)
q.push(2)
q.push(3)
q.push(4)

print(q)

q.pop()
q.pop()

print(q)

print(q.is_q_empty())

print(q.peek())


            
        
        
    

