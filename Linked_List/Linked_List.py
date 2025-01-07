class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def InsertAtIndex(self, data, index):
        if index == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        position = 0
        while current and position < index - 1:
            current = current.next
            position += 1
        if not current:
            print("Index out of range")
            return
        new_node.next = current.next
        current.next = new_node

    def InsertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def UpdateNode(self, data, index):
        if not self.head:
            print("No node exists to update")
            return
        current = self.head
        position = 0
        while current and position < index:
            current = current.next
            position += 1
        if not current:
            print("Index out of range")
        else:
            current.data = data

    def RemoveNodeAtIndex(self, index):
        if not self.head:
            print("List is empty")
            return None
        if index == 0:
            data = self.head.data
            self.head = self.head.next
            return data
        current = self.head
        prev = None
        position = 0
        while current and position < index:
            prev = current
            current = current.next
            position += 1
        if not current:
            print("Index out of range")
            return None
        prev.next = current.next
        return current.data

    def RemoveNodeAtEnd(self):
        if not self.head:
            print("List is empty")
            return None
        if not self.head.next:
            data = self.head.data
            self.head = None
            return data
        current = self.head
        while current.next and current.next.next:
            current = current.next
        data = current.next.data
        current.next = None
        return data

    def RemoveNodeAtBegin(self):
        if not self.head:
            print("List is empty")
            return None
        data = self.head.data
        self.head = self.head.next
        return data

    def SizeOfList(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def Concatenate(self, linked_list):
        if not self.head:
            self.head = linked_list.head
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = linked_list.head

    def Invert(self):
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous

    def Display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

