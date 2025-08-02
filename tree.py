class Tree():
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
        
root = Tree(50)
root.leftchild = Tree(30)
root.rightchild = Tree(70)
root.leftchild.leftchild = Tree(20)
root.leftchild.rightchild = Tree(40)
root.rightchild.leftchild = Tree(60)
root.rightchild.rightchild = Tree(80)

def inorder(root): #inorder means left node then root node then right node
  if root.leftchild != None:
    inorder(root.leftchild)
  print(root.data)
  if root.rightchild != None:
    inorder(root.rightchild)
    
inorder(root)

def preorder(root): #preorder root then left then right
  print(root.data)
  if root.leftchild != None:
    preorder(root.leftchild)
  if root.rightchild != None:
    preorder(root.rightchild)
    
print("----")
preorder(root)  
    
def postorder(root):
  if root.leftchild != None:
    postorder(root.leftchild)
  if root.rightchild != None:
    postorder(root.rightchild)
  print(root.data)
  
print("----")
postorder(root)
