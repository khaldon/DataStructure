class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 

class Queue:
    def __init__(self):
        self.top = None 
        self.bottom = None 
        self.length = 0
    
    def peek(self):
        curr = self.top
        print(curr.value)
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.top = self.bottom = new_node
            self.length = 1 
        else:
            self.bottom.next = new_node
            self.bottom = new_node

    def dequeue(self):
        if self.length == 0:
            print("this queue empty")
        else:
            unwanted = self.top
            self.top = unwanted.next

q = Queue()
q.enqueue(22)
q.enqueue(99)
q.enqueue(55)
q.enqueue(88)
q.peek()