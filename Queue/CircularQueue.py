class CircularQueue:
    def __init__(self, size):
        self.front = -1
        self.rear = -1
        self.Queue = [None] * size
        self.size = size

    def IsEmpty(self): 
        return self.front == -1

    def IsFull(self): 
        return (self.rear + 1) % self.size == self.front

    def Enqueue(self, obj):
        if self.IsFull():
            print("Queue is full!")
            return

        if self.IsEmpty():
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.Queue[self.rear] = obj
        print(f"Enqueued: {obj}")

    def Dequeue(self):
        if self.IsEmpty():
            print("Queue is empty!")
            return

        dequeued_item = self.Queue[self.front]
        self.Queue[self.front] = None

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        print(f"Dequeued: {dequeued_item}")

    def Peek(self):
        if self.IsEmpty():
            print("Queue is empty!")
            return

        print(f"The front of the queue is: {self.Queue[self.front]}")

if __name__ == "__main__":
    cq = CircularQueue(5)

    cq.Enqueue(10)
    cq.Enqueue(20)
    cq.Enqueue(30)
    cq.Enqueue(40)
    cq.Enqueue(50)
    cq.Enqueue(60) 
    cq.Peek()
    cq.Dequeue()
    cq.Dequeue()
    cq.Enqueue(60)  
    cq.Enqueue(70)  
    cq.Enqueue(80) 