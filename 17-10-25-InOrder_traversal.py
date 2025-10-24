class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)
n5=Node(5)
n6=Node(6)

root=n1
n1.left=n2
n2.left=n4
n2.right=n5
n1.right=n3
n3.left=n6

def inOrder(root):
    if root==None:
        return
    inOrder(root.left)
    print(root.data)
    inOrder(root.right)

def preOrder(root):
    if root==None:
        return
    print(root.data)
    preOrder(root.left)
    preOrder(root.right)
    
def postOrder(root):
    if root==None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.data)

def lvlOrder(root):
    q=[root]
    while(q!=[]):
        n=q.pop(0)
        print(n.data)
        if n.left:
            q.append(n.left)
        if n.right:
            q.append(n.right)

inOrder(root)
print("\n")

preOrder(root)
print("\n")

postOrder(root)
print("\n")

lvlOrder(root)