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


def search(root,element):
  if root.data == element:
    return True
  elif root.data > element and root.leftchild != None:
    return search(root.leftchild, element)
  elif root.data < element and root.rightchild != None:
    return search(root.rightchild, element)
  else:
    return False
  

s = search(root, 20)
if s == True:
  print("Your number is in the tree.")
else:
  print("Your number is not in the tree.")

def insert(root, element):
  if root == None:
    return Tree(element)
  elif element < root.data:
    root.leftchild = insert(root.leftchild, element)
  else:
    root.rightchild = insert(root.rightchild, element)
  return root

root = insert(root, 90)
postorder(root)

def delete(root, element):
  if root == None:
    return root
  elif element > root.data:
    root.rightchild = delete(root.rightchild, element)
  elif element < root.data:
    root.leftchild = delete(root.leftchild, element)
  else:
    pass
