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
        
        if self.head == None:
            print("List is Empty")
            return
        
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
    
    def insert(self, index, val):
        if index == 0:
            self.add_first(val)
        else:
            new_node = Node(val)
            tmp = self.head
            for i in range(index-1):
                tmp = tmp.next
            new_node.next = tmp.next
            new_node.prev = tmp
            tmp.next = new_node
            new_node.next.prev = new_node
            
    def search(self, key):
        
        temp = self.head
        
        while temp != None:      # in order to actually go over (iterate) the last node itself and check it's data we do while temp and not while temp.next
            if temp.data == key:
                return True
            temp = temp.next
        return False

    '''
    This is my implementation of deleting a node in a doubly linked list!
    For another implementation look below.
    
    '''
    def delete(self, val):
        
        print("Delete a node")
        
        if self.head == None:
            print("List is Empty")
            return
        elif self.head.data == val:  # If the node to delete is the first node
            if self.head.next == None: # This is the ONLY node in the list.
                self.head = None
                print("Deleted the last node in the list, now the list is empty")
                return
            self.head = self.head.next
            self.head.prev = None
            return
        
        temp = self.head
        
        while temp != None:
            if temp.data == val:  # If the node to delete is the last node
                if temp.next == None:
                    temp.prev.next = temp.next
                    break
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                temp.prev = None            # optional
                temp.next = None            # optional
                break
            temp = temp.next
            
    
    '''
        This is another implementation of deleting a node in a linked list.
    '''       
    
    def deleteNode(self, key):

        if self.head == None:
            return

        temp = self.head

        while temp != None and temp.data != key:
            temp = temp.next

        if temp == None:
            print("Key Not Found")
        elif temp == self.head:
            self.head = self.head.next
            self.head.prev = None
        elif temp.next == None:
            temp.prev.next = None
        else:
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            

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
    
    # l.printList()
    
    l.addLast(100)
    
    l.printList()
    
    l.insert(2,50)
    
    l.printList()
    
    print("deleting")
    
    l.delete(100)
    
    l.printList()
    
    l.delete(60)
    
    l.printList()
    
    l.delete(20)
    
    l.printList()
    
    l.delete(30)
    
    l.printList()
    
    l.delete(10)
    
    l.printList()
    

    
