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
    