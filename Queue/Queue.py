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
    
    def Enqueue(self, obj):
            if self.IsFull():
                print("Queue is full!")
                return
            self.Queue[self.cap] = obj  # Add at the end of the filled portion
            self.cap += 1


    def Dequeue(self):
        if self.IsEmpty():
            print("Empty")
            return
        print("dequeued object:", self.Queue[self.front])

        for i in range(self.cap - 1):
            self.Queue[i] = self.Queue[i + 1]
    
        self.Queue[self.cap - 1] = None

        self.cap -= 1


    def Peek(self):
        if self.IsEmpty():
            print("Queue is empty!")
            return
        print("The front of the Queue is:", self.Queue[self.front])


    def ReverseQueue(self):
        if self.IsEmpty():
            print("Queue is empty!")
            return

        temp_q = [None] * self.size

        idx = self.front
        for i in range(self.cap):
            temp_q[self.cap - 1 - i] = self.Queue[idx]
            idx = (idx + 1) % self.size  

        self.Queue = temp_q

        self.front = 0
        self.rear = self.cap - 1

        print("Reversed Queue:", self.Queue[:self.cap])


if __name__ == '__main__':

    obj = Queuecalss(5)
    obj.Enqueue(1)
    obj.Enqueue(5)
    obj.Enqueue(65)
    obj.Enqueue(100)
    obj.Enqueue(45)
    obj.Enqueue(100)
    obj.Dequeue()
    obj.Enqueue(55)
    obj.Dequeue()
    obj.Dequeue()
    obj.Peek()
    obj.ReverseQueue()