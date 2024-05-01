''' Circular linked lists '''

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        
    def __repr__(self) -> str:
        return f"Node data: {self.data}"
    

class CircularLinkedList:
    def __init__(self) -> None:
        self.head = None
        
    def printList(self):
        temp = self.head
        
        if self.head == None:
            print("List is Empty!")
            return
        
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break
        print("\n")
    
    def addFirst(self, val):
        
        new_node = Node(val)
        
        if self.head == None:
            self.head = new_node
            new_node.next = self.head
        else:
            tmp = self.head
            while tmp.next != self.head:
                tmp = tmp.next
            tmp.next = new_node
            new_node.next = self.head
            self.head = new_node
            
            
    def addLast(self,val):

        new_node = Node(val)

        if self.head == None:
            self.head = new_node
            new_node.next = self.head
        else:
            tmp = self.head
            while tmp.next != self.head:
                tmp = tmp.next
                
            new_node.next = self.head
            tmp.next = new_node
    
    def search(self, key):
        
        if self.head == None:
            return False
        
        tmp = self.head
        
        while True:
            if tmp.data == key:
                return True
            tmp = tmp.next
            if tmp == self.head:
                break
        return False
    
    def delete(self, key):
        if self.head == None:                                           # Case 1: List is Empty
            return
        
        if self.head.data == key and self.head.next == self.head:       # Case 2.1: When the Node to delete is the head and its the only node in the list
            self.head = None
            
        elif self.head.data == key:                                    # Case 2.2: When the Node to delete is the head (the first node) and there are more nodes after it in the list
            tmp = self.head
            while tmp.next != self.head:
                tmp = tmp.next
                
            tmp.next = self.head.next
            self.head = self.head.next
            
        else:                                                         # Case 3: When the node to be deleted is any other node except the first node (the head)
            cur = self.head
            while cur.next != self.head:
                if cur.next.data == key:
                    cur.next = cur.next.next
                    break
                cur = cur.next            
            

if __name__ == '__main__':
    circular_list = CircularLinkedList()
    
    circular_list.head = Node(10)
    middle = Node(20)
    last = Node(30)
    
    circular_list.head.next = middle
    middle.next = last
    last.next = circular_list.head
    
    circular_list.printList()
    
    print("\nAdding a new node at the beginning of the list\n")
    
    circular_list.addFirst(100)
    
    circular_list.printList()
    
    circular_list.addFirst(200)
    
    circular_list.printList()
    
    print("\nAdding a new node at the end of the list\n")
    
    circular_list.addLast(400)
    
    circular_list.addLast(500)
    
    circular_list.printList()
    
    print(circular_list.search(7))
    
    print(circular_list.search(20))
    
    print("\nDeleting a node from the list\n")
    
    circular_list.delete(10)
    
    circular_list.printList()
    