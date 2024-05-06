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


'''
NOTE: You will get an IndexError: list assignment index out of range in line __ when trying to push to the stack
(which is a Python List)

This happens because stack is an empty list at the beginning, but you're attempting to write to element stack[0] , which doesn't exist yet.
Same happens if we initialize self.stack = [None] and then try to push a second element.

In short we need to have an initialization like above with [None] * size if we want to do the push without using append!

Otherwise we can just solve it using append built in method!

see explaination in the link below

Also check out the Array implementation we have

'''
        

# https://stackoverflow.com/questions/5653533/why-does-this-iterative-list-growing-code-give-indexerror-list-assignment-index 


# class Stack():
    
#     def __init__(self):
#         self.stack = []
#         self.top = -1
#         self.size = 0
        
#     def push(self, val):
#         self.top = self.top + 1
#         self.stack[self.top] = val    # NOTE: here we have a problem, to solve use append directly or the above code
#         self.size += 1
            
#     def pop(self):
#         if self.top == -1:
#             print("Stack is Empty")
#         else:
#             print(f"Popped element = {self.stack[self.top]}")
#             self.top = self.top - 1
#             self.size -= 1 
        

if __name__=='__main__':

    s = Stack(4)

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

    
    # def test_arr(arr):
    #     for i in range(len(arr)):
    #         print(i)

    #     if arr:
    #         print("Has something - condition True")
    #     else:
    #         print("Has NOTHING - condition False")
            
    # arr = []
     
    # test_arr(arr)
        
    # arr.append(6)
    
    # test_arr(arr)
    
   