class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        self.head = Node(value)
        self.tail = self.head
        self.length  = 1
  
    def append(self, value):
        self.newnode = Node(value)
        self.current  = self.tail
        self.tail.next = self.newnode # next 
        self.tail = self.newnode # to show the last node or assignment end of the node 
        self.length +=1
    
    def prepend(self, value):
        self.newnode = Node(value)
        self.newnode.next = self.head
        self.head = self.newnode
        self.length +=1
        return self.head
    
    def traverseToIndex(self, index):
        self.counter = 0
        self.currentNode = self.head
        while self.counter  != index : 
            self.currentNode = self.currentNode.next
            self.counter +=1 
        return self.currentNode

    def insert(self, index, value):
        self.newnode = Node(value)
        if index > self.length:
            return "error"
        else:
            self.leader = self.traverseToIndex(index-1) 
            self.holdingpoint = self.leader.next #  99 100 
            self.leader.next = self.newnode # 33 
            self.newnode.next = self.holdingpoint

            self.length +=1 

    def printlist(self):
        self.array = []
        self.currentNode = self.head
        while (self.currentNode != None):
            self.array.append(self.currentNode.value)
            self.currentNode = self.currentNode.next
        print(self.array)
            
    def remove(self,  index):
        if index > self.length:
            print("the index out of range")
        elif index == 0:
            curr = self.head.next
            self.head = curr

        else:
            self.leader = self.traverseToIndex(index-1)
            self.unwanted = self.traverseToIndex(index)
            self.leader.next = self.unwanted.next
            self.length  -=1 
            return self.printlist()

a = LinkedList(10)

a.append(11)
a.append(33)
a.prepend(200)
a.insert(1, 1000)
a.remove(0)
a.printlist()
