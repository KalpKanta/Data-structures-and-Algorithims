class Queue():
    def __init__(self, size):
        self.queue = [None] * size
        self.size = size
        self.front = 0
        self.rear = 0
        self.available = size
        
    def enq(self, item):
        if self.available == 0:
            print("Queue is full!")
        else:
            self.queue[self.rear] = item
            self.available = self.available - 1
            self.rear = self.rear + 1
    
    def deq(self):
        if self.available == self.size:
            print("Queue is empty")
        else: 
            item = self.queue[self.front]
            self.queue[self.front] = None
            self.available = self.available + 1
            self.front = (self.front + 1) % self.size
    
    def peek(self):
        if self.available == self.size:
            print("Queue is empty")
        else:
            return self.queue[self.front]
    
queue = Queue(3)
queue.enq("Water bottle")
queue.enq("Pencil")
queue.enq("Chocolates")
queue.enq("yes")
print(queue.queue)
queue.deq()
print(queue.peek())