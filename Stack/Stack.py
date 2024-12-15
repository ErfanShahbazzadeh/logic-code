class Stack:
    def __init__(self, size):
        self.stack = [None] * size
        self.size = size
        self.pointer = -1

    def Push(self, value):
        if self.pointer == self.size - 1:  
            print("Stack is full.")
            return
        self.pointer += 1
        self.stack[self.pointer] = value
        print(f"Pushed {value} to the stack.")

    def Pop(self):
        if self.IsEmpty():
            print("Stack is empty. Cannot pop.")
            return None
        popped_value = self.stack[self.pointer]
        print(f"The popped value is {popped_value}.")
        self.stack[self.pointer] = None
        self.pointer -= 1
        return popped_value

    def Peek(self):
        if self.IsEmpty():
            print("Stack is empty. No peek value.")
            return None
        print(f"The peek value is {self.stack[self.pointer]}")
        return self.stack[self.pointer]

    def IsEmpty(self):
        return self.pointer == -1


# Example Usage
obj = Stack(5)
obj.Push(1)
obj.Push(43)
obj.Push(23)
obj.Push(5)
obj.Push(87)
obj.Push(987)  
obj.Peek()  
obj.Pop()  
obj.Pop()
obj.Peek()
