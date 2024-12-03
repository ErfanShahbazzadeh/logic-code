class Queuecalss:
    def __init__(self,size):
        self.front = 0
        self.cap = 0
        self.rear = size - 1
        self.Queue = [None]*size
        self.size = size


    def IsEmpty(self): 
        return self.cap == 0


    def IsFull(self): 
        return self.cap == self.size


    def Enqueue(self,object):
        if self.IsFull():
            print("Full")
            return
        self.rear = (self.rear + 1) % (self.size)
        self.Queue[self.rear]  = object
        self.cap += 1 

    def Dequeue(self):
        if self.IsEmpty():
            print("Empty")
            return
        print("dequeued object:",self.Queue[self.front] )
        self.front = (self.front + 1) % (self.size)
        self.cap -= 1
    
    def Peek(self):
        if self.IsEmpty():
            print("Queue is empty!")
            return
        print("The front of the Queue is:",self.Queue[self.rear])


    def ReverseQueue(self):
        i = 0
        temp_q = []
        for _ in range(self.cap , -1):
            temp_q[i] = self.Queue[_]
            i += 1
        print("Reversed Queue:", temp_q)


if __name__ == '__main__':

    obj = Queuecalss(5)
    obj.Enqueue(1)
    obj.Enqueue(5)
    obj.Enqueue(65)
    obj.Enqueue(100)
    obj.Enqueue(45)
    obj.Enqueue(100)
    obj.Dequeue()
    obj.Peek()
    obj.ReverseQueue()