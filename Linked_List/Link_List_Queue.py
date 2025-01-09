from Linked_List import Linked_list

class Linked_List_Queue():

    def __init__(self):
         self.linked_queue = Linked_list()  

    def linked_Enqueue(self,data):
        self.linked_queue.InsertAtEnd(data)

    def linked_Dequeue(self):
        self.linked_queue.RemoveNodeAtBegin()

    def Linked_Peek(self):
        return self.linked_queue.head.data

    def Linked_size(self):
        self.linked_queue.SizeOfList()

    def Linked_Dis(self):
        self.linked_queue.Display()

