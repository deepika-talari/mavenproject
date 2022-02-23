class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

    
def preorder(root):
    if root:

        print(root.val)
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root:
        
        preorder(root.left)
        preorder(root.right)
        print(root.val)
def postorder(root):
    if root:
        
        preorder(root.left)
        print(root.val)
        preorder(root.right)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
print(preorder(root))


        
    
