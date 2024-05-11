'''
Check for balanced parentheses in Python - From Gool

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


def is_balanced(expr):
    s = Stack()
    for each_char in expr:
        if each_char == "(" or each_char == "[" or each_char == "{":
            s.push(each_char)
        else:
            if (s.is_empty() and (each_char == ")" or each_char == "]" or each_char == "}")):
                return False
            if each_char == ")":
                if s.top() == "(":
                    s.pop()
            elif each_char == "]":
                if s.top() == "[":
                    s.pop()
            elif each_char == "}":
                if s.top() == "{":
                    s.pop()
            else:
                continue
    if s.is_empty():
        return True
    return False
    


# mystack = Stack()
# print(mystack.is_empty())
# mystack.push(1)
# mystack.push(2)
# mystack.push(3)
# print(mystack.is_empty())
# print(mystack)
# mystack.pop()
# print(mystack)
# mystack.push(10)
# mystack.push(20)
# mystack.push(30)
# print(mystack)

print(is_balanced("{x+78+15}"))

        

