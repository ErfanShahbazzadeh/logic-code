from Linked_List import Linked_list

class Linked_List_Stack():

    def __init__(self):
        self.linked_stack = Linked_list()  

    def Linked_Push(self,data):
        self.linked_stack.InsertAtEnd(data)

    def Linked_Pop(self):
        self.linked_stack.RemoveNodeAtEnd()

    def Linked_Dis(self):
        self.linked_stack.Display()

    def Linked_Peek(self,):
        if not self.linked_stack.head:  
            return None
        current = self.linked_stack.head
        while current.next: 
            current = current.next
        return current.data

