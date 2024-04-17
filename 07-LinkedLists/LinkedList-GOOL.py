''' Linked List Implementation for GOOL '''

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return (f"Node: {self.data}")


class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def __repr__(self):
        if self.head == None:
            return "[]"
        else:
            str_repr = ""
            tmp = self.head # Iter pointer to traverse all nodes
            while(tmp != None):
                str_repr += (str(tmp.data) + " -> ")
                tmp = tmp.next
            str_repr += str(None)
            return str_repr
    
    def __len__(self):
        size = 0
        if self.head ==  None:
            return size
        else:
            tmp = self.head
            while(tmp!=None):
                size+=1
                tmp = tmp.next
            return size
        
    def __getitem__(self, index):
        assert 0 <= index < len(self)
        tmp = self.head
        for i in range(index):
            tmp=tmp.next
        return tmp.data # or just tmp
                  
    
    def __setitem__(self, index, val):
        assert 0 <= index < len(self)
        tmp = self.head
        for i in range(index):
            tmp=tmp.next
        tmp.data = val
                 
    def pre_append(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            new_node.next = self.head
            self.head = new_node
        else:
            tmp = self.head
            while (tmp.next != None):
                tmp = tmp.next
            new_node.next = tmp.next
            tmp.next = new_node

    def data_sum(self):
        data_sum = 0
        if self.head == None:
            return data_sum
        else:
            tmp = self.head
            while(tmp!=None):
                data_sum+=tmp.data
                tmp=tmp.next
            return data_sum
            
    def find(self, val):
        if self.head == None:
            return None
        else:
            tmp = self.head
            while(tmp!=None):
                if tmp.data == val:
                    return tmp
                tmp = tmp.next
            return None
        
    def insert(self, index, val):
        assert 0 <= index < len(self)
        if index == 0:
            self.pre_append(val)
        else:
            new_node = Node(val)
            tmp = self.head
            for i in range(index-1):
                tmp = tmp.next
            new_node.next = tmp.next
            tmp.next = new_node
                
   
    def delete(self, index):
        assert 0 <= index < len(self)
        if index == 0:
            self.head = self.head.next
        else:
            tmp = self.head
            for i in range(index-1):
                tmp = tmp.next
            tmp.next = tmp.next.next
        
        
        
                    
    
        

l = LinkedList()
print(l)
print("length of linked list: ", len(l))
l.pre_append(10)
print(l)
l.pre_append(20)
print(l)
l.pre_append(30)
print(l)
l.pre_append(40)
print(l)
l.pre_append(50)
print(l)
print("length of linked list: ", len(l))
print(l.data_sum())
print(l.find(30))
print("node in position 1 is:", l[1])
print("node in position 0 is:", l[0])
l[0] = 500
print(l)
l.insert(2,11)
print(l)
l.delete(2)
l.delete(4)
print(l)
l.append(33)
print(l)
l.append(44)
l.append(55)
print(l)
    
        
        