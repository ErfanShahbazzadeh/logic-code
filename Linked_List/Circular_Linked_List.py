class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            new_node.next = self.head
            self.head = new_node
            current.next = self.head

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def insert_at_index(self, data, index):
        if index == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        position = 0
        while position < index - 1 and current.next != self.head:
            current = current.next
            position += 1
        if position < index - 1:
            print("Index out of range")
            return
        new_node.next = current.next
        current.next = new_node

    def remove_node_at_index(self, index):
        if not self.head:
            print("List is empty")
            return None
        if index == 0:
            if self.head.next == self.head:  
                data = self.head.data
                self.head = None
                return data
            current = self.head
            while current.next != self.head:
                current = current.next
            data = self.head.data
            current.next = self.head.next
            self.head = self.head.next
            return data
        current = self.head
        prev = None
        position = 0
        while position < index and current.next != self.head:
            prev = current
            current = current.next
            position += 1
        if position < index:
            print("Index out of range")
            return None
        prev.next = current.next
        return current.data

    def size_of_list(self):
        if not self.head:
            return 0
        count = 1
        current = self.head
        while current.next != self.head:
            count += 1
            current = current.next
        return count

    def concatenate(self, other_list):
        if not self.head:
            self.head = other_list.head
            return
        if not other_list.head:
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = other_list.head
        other_current = other_list.head
        while other_current.next != other_list.head:
            other_current = other_current.next
        other_current.next = self.head

    def invert(self):
        if not self.head or self.head.next == self.head:
            return
        previous = None
        current = self.head
        next_node = None
        start = self.head
        while True:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
            if current == start:
                break
        self.head.next = previous
        self.head = previous

    def display(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(Back to head)")


