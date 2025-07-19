class Queue():
    def __init__(self, size):
        self.queue = [None]
        self.size = size
        self.front = 0
        self.rear = 0
        self.available = size
        
    def enqueue(self, item):
        if self.available == 0:
            print("Queue is full!")
        else:
            self.queue[self.rear] = item
            self.available = self.available - 1
            self.rear = self.rear + 1