'''
This is a python implementation to an Array data structure
'''

class MyArray():
    def __init__(self) -> None:
        self.length = 0
        self.data = {} # using a dictionary to represent the data of an array and its indexes

    def __str__(self) -> str:
        return f" Array length is {self.length} and context is {self.data}"
    
    def get(self, index):
        return self.data[index]
    
    # append
    def push(self, item):
        self.data[self.length] = item
        self.length += 1
        return self.length
    
    def pop(self):
        last_item = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -= 1
        return last_item
    
    def delete(self, index):
        del_item = self.data[index]
        self.shift_items(index)
        
    def shift_items(self, index):
        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1] # shifts elements to the left
                 
        del self.data[self.length-1]
        self.length -= 1
        
        # while(index < self.length-1):
        #     self.data[index] = self.data[index+1] # shifts elements to the left
        #     index += 1
     
        # del self.data[self.length-1]
        # self.length -= 1
        
    def insert(self, index, item):
        # cur_item = self.data[index]
        # self.data[index] = item
        # for i in range(self.length, index, -1):
        #     self.data[i] = self.data[i-1] # shifts elements to the right
        # self.data[index+1] = cur_item
        # self.length += 1
        
        shift = self.length
        while shift > index:
            self.data[shift] = self.data[shift-1]
            shift -= 1
        self.data[index] = item
        self.length += 1
            

# create an array instance 
print("----- ARRAY INITIALIZATION ------")
my_arr = MyArray()
print(my_arr)
print("------------------------")

# check the push method
print("----- PUSH METHOD ------")
my_arr.push("hi")
my_arr.push("you")
my_arr.push("!")
my_arr.push("?")
my_arr.push("are")
my_arr.push("nice")
my_arr.push("!")
my_arr.push("+")
print(my_arr)
print("------------------------")

# check the pop method
print("----- POP METHOD ------")
poped_item = my_arr.pop()
print(my_arr)
print(poped_item)
print("------------------------")

# check the delete method
print("----- DELETE METHOD ------")
my_arr.delete(3)
my_arr.delete(2)
print(my_arr)
print("------------------------")

# check the insert method
print("----- INSERT METHOD ------")
my_arr.insert(1, "insert #1")
my_arr.insert(6, "insert #2")
print(my_arr)
print("------------------------")