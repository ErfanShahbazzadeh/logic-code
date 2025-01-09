from Linked_List import Linked_list

class Linked_List_Array:
    def __init__(self):
        self.linked_list = Linked_list()  
    def Link_appand(self, data):
        self.linked_list.InsertAtEnd(data)

    def Link_insert(self, data, index):
        self.linked_list.InsertAtIndex(data, index)

    def Link_pop(self, index):
        self.linked_list.RemoveNodeAtIndex(index)

    def Link_reverse(self):
        self.linked_list.Invert()

    def Link_len(self):
        return self.linked_list.SizeOfList()

    def Link_Dis(self):
        self.linked_list.Display()
