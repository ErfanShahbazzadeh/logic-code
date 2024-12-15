class QueueStack:
    def __init__(self, size):
        self.s1 = [None] * size 
        self.s2 = [None] * size  
        self.cap = 0
        self.size = size
        self.top1 = -1  
        self.top2 = -1  

    def IsEmpty(self):
        return self.cap == 0

    def IsFull(self):
        return self.cap == self.size

    def Enqueue(self, x):
        if self.IsFull():  
            print("Queue is full!")
            return
        self.top1 += 1  
        self.s1[self.top1] = x  
        self.cap += 1 

    def Dequeue(self):
        if self.top1 == -1 and self.top2 == -1:
            return -1

        if self.top2 == -1:
            while self.top1 != -1:
                temp = self.s1[self.top1]
                self.s1[self.top1] = None  
                self.top1 -= 1

                self.top2 += 1
                self.s2[self.top2] = temp

        result = self.s2[self.top2]
        self.s2[self.top2] = None  
        self.top2 -= 1
        self.cap -= 1
        return result

if __name__ == '__main__':
    q = QueueStack(5)
    q.Enqueue(1)
    q.Enqueue(2)
    q.Enqueue(3)
    q.Enqueue(4)
    q.Enqueue(54)
    q.Enqueue(55)
    print(q.Dequeue())  
    print(q.Dequeue()) 
    print(q.Dequeue())  
    print(q.Dequeue()) 
    print(q.Dequeue())