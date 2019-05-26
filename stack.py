class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 
    
class Stack:
    def __init__(self):
        self.top = None 
        self.bottom = None 
        self.length = 0 
    
    def peek(self):
        curr = self.top
        print(curr.value)

    def push(self, value):
        new_node = Node(value)
        if self.length == 0 and self.top and self.bottom == None:
            self.top = self.bottom = new_node
            self.length = 1 
        else:
            holdingpoint = self.top
            self.top = new_node
            self.top.next = holdingpoint
            self.length +=1
    
    def pop(self):
        if self.top == None:
            print("The stack is empty")
        else:
            unwanted = self.top
            self.top = unwanted.next
            self.length -=1 



Mystack = Stack()
Mystack.push(100) # add element to be top 
Mystack.push(300)
Mystack.push(555)
Mystack.peek() # show the first or the top of stack currently 
Mystack.pop()  # Remove the first element of stack 




