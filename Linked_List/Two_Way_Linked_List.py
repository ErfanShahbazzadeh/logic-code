class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head: 
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head: 
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert_at_index(self, data, index):
        if index == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        position = 0
        while current and position < index:
            position += 1
            if position == index:
                break
            current = current.next
        if not current:
            if position == index:  
                self.insert_at_end(data)
            else:
                print("Index out of range")
            return
        new_node.next = current
        new_node.prev = current.prev
        if current.prev:
            current.prev.next = new_node
        current.prev = new_node

    def remove_node_at_index(self, index):
        if not self.head:
            print("List is empty")
            return None
        if index == 0:  
            data = self.head.data
            if self.head == self.tail:  
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            return data
        current = self.head
        position = 0
        while current and position < index:
            position += 1
            current = current.next
        if not current:
            print("Index out of range")
            return None
        data = current.data
        if current.next:  
            current.next.prev = current.prev
        else: 
            self.tail = current.prev
        if current.prev:
            current.prev.next = current.next
        return data

    def size_of_list(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def invert(self):
        if not self.head:
            return
        current = self.head
        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev  
        self.head, self.tail = self.tail, self.head

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def display_reverse(self):
        current = self.tail
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")
