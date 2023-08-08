'''
Linked Lists Implementation
'''

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        
    def __repr__(self) -> str:
        return f"Node data: {self.data}"

class LinkedList():
    def __init__(self) -> None:
        self.head = None
    
    def is_empty(self):
        """
        checks if the linked list is empty or not
        """
        return self.head == None
    
    def size(self):
        """
        Returns the size of the linked list - the number of elements in the linked list
        Takes O(n) Time
        """
        temp = self.head
        lst_size = 0
        while(temp):
            lst_size += 1
            temp = temp.next
        return lst_size    
    
    def add_first(self, val):
        """
        prepend function - Adds a new node containing val at the head of the list
        Takes O(1) Time 
        """
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode

    def add_last(self, val):
        """
        append function - Adds a new node containing val at the end of the list
        Takes O(n) Time
        """
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
        else:
            temp = self.head    # temp to traverse the linked list
            while(temp.next):
                temp = temp.next
            temp.next = newNode
    
    def insert(self, data, index):
        """
        Inserts a new Node containing data at given index position
        Insertion itself takes O(1), but finding the position to insert in takes O(n) time.
        
        Takes overall O(n) time
        """
        
        if index == 0:
            self.add_first(data)
        else:
            temp = self.head
            while(index - 1):   # Traverse to the node at index before the index we want to insert
                temp = temp.next
                index -= 1
            new_node = Node(data)
            new_node.next = temp.next
            temp.next = new_node
        
        
    
    def search(self, key):
        """
        Search for the first node containing data that matches the key
        If list containing more than one node with the same value this function
        will return the first appearance.
        Return the node or 'None' if not found.
        
        Takes O(n) Time
        """
        temp = self.head
        while(temp.next != None):
            if (temp.data == key):
                return temp
            temp = temp.next
        return None
    
    def delete(self, key):
        """
        Deletes Node containing data that matches the given key
        Takes O(n) time.
        """
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

    
    def remove_at_index(self, index):
        """
        Removes Node at given index.
        Takes O(n) time.
        """
        if index == 0:
            self.head = self.head.next
        else:
            temp = self.head
            while(index > 1):
                temp = temp.next
                index -= 1
            temp.next = temp.next.next
            
    
    def print_list(self):
        temp = self.head
        print("The LinkedList Elements Are: ")
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
            
    def __repr__(self) -> str:
        """
        Return a string representation of the linked list
        Takes O(n) Time
        """
        temp = self.head
        lst = []
        if self.head == None:
            return str(lst)
        while(temp):
            lst.append(str(temp.data))
            temp = temp.next
        lst.append("None")
        return "->".join(lst)
            

if __name__ == '__main__':
    l = LinkedList()
    l.add_first(1)
    l.add_first(2)
    l.add_first(3)
    l.add_first(4)
    print(l)
    print(l.search(2))
    l.insert(6,2)
    print(l)
    l.remove_at_index(2)
    print(l)
    l.remove_at_index(0)
    print(l)