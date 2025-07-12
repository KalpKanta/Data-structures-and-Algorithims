class Stack():
    def __init__(self, n):
        self.stack = []
        self.n = n #n variable is the maximum number of variables we are able to store in the stack
    def display(self):
        print(self.stack)
    def push(self, num):
        if len(self.stack) >= self.n:
            print("Stack is full")
        else:
            self.stack.append(num)
    def pop(self):
        if len(self.stack) <= 0:
           print("Stack has no values")
        else:
             self.stack.pop(-1)
    def size(self):
        size = len(self.stack)
        print(size)


stack1 = Stack(2)
stack1.push(12)
stack1.push(3)
stack1.push(8)
stack1.display()
stack1.pop()
stack1.pop()
stack1.pop()