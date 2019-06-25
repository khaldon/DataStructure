# BinarySearchTree data structure

#create class Node

class Node:
    def __init__(self, value):
       self.value = value 
       self.right = None 
       self.left  = None  

class BST: 
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            return self._insert(value, self.root)
    
    def _insert(self, value, currentnode):
        if currentnode.value < value:
            if currentnode.right == None:
                currentnode.right = Node(value)
            else:
                self._insert(value, currentnode.right)
        else:
            if currentnode.left == None:
                currentnode.left = Node(value)
            else:
                self._insert(value, currentnode.left)
    
    def search(self, value):
        if self.root.value == value:
            return self.root.value
        else:
            return self._search(self.root, value) 
    def _search(self, currentnode, value):
        if currentnode == None:
            return None 
        else:
            self._search(currentnode.right, value)
            self._search(currentnode.left, value)

        
            

            

bst = BST()
bst.insert(22)
bst.insert(33)
bst.insert(44)
bst.insert(11)
bst.insert(10)