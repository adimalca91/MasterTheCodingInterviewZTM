'''
Doubly Linked List Implementation
'''

class Node:
    def __init__(self, data) -> None:
        self.prev = None
        self.data = data
        self.next = None
        
    def __repr__(self) -> str:
        return f"Node data: {self.data}"
    

class DoublyLinkedList():
    
    def __init__(self) -> None:
        self.head = None
        
    def printList(self):
        temp = self.head
        
        print("Forward Traversal")
        while(temp != None):
            print(temp.data)
            if (temp.next == None):
                last = temp
            temp = temp.next
            
        print("Backward Traversal")
        temp = last
        while(temp != None):
            print(temp.data)
            temp = temp.prev
       
    def add_first(self,val):
        newNode = Node(val)
        if(self.head == None):
            self.head = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
         
    def addLast(self, val):
        newNode = Node(val)
        if(self.head == None):
            self.head = newNode
        else:
            temp = self.head
            while temp.next != None:  # in order to only know where the last node is and add another after it (and not to get the data of it).
                temp = temp.next
            temp.next = newNode
            newNode.prev = temp
            
    def search(self, key):
        
        temp = self.head
        
        while temp != None:      # in order to actually go over (iterate) the last node itself and check it's data we do while temp and not while temp.next
            if temp.data == key:
                return True
            temp = temp.next
        return False

if __name__ == "__main__":
    l = DoublyLinkedList()
    l.head = Node(10)
    middle = Node(20)
    last = Node(30)
    
    l.head.prev = None
    l.head.next = middle
    middle.prev = l.head
    middle.next = last
    last.prev = middle
    last.next = None
    
    # l.printList()
    
    l.add_first(60)
    
    l.printList()
    
    l.addLast(100)
    
    l.printList()