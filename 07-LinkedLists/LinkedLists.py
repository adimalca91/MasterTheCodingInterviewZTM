'''
Linked Lists Implementation
'''

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self) -> None:
        self.head = None
        
    
    def add_first(self, val):
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode

    def add_last(self, val):
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
        else:
            temp = self.head    # temp to traverse the linked list
            while(temp.next):
                temp = temp.next
            temp.next = newNode
    
    def search(self, key):
        temp = self.head
        while(temp.next != None):
            if (temp.data == key):
                return True
            temp = temp.next
        return False
    
    def delete(self, key):
        if self.head.data == key:
            self.head = self.head.next
            
        else:
            temp = self.head
            while(temp.next != None):
                if(temp.next.data == key):
                    temp.next = temp.next.next
                    break
                else:
                    temp = temp.next

    def print_list(self):
        temp = self.head
        print("The LinkedList Elements Are: ")
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.add_first(10)
    linked_list.add_first(20)
    linked_list.print_list()
    linked_list.add_last(40)
    linked_list.print_list()
    linked_list.delete(10)
    linked_list.print_list()
    