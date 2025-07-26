class Tree(self):
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