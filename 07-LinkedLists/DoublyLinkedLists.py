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
    
    l.printList()