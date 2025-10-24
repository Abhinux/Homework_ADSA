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

root1=n1
n1.left=n2
n2.left=n4
n2.right=n5
n1.right=n3
n3.left=n6

m1=Node(1)
m2=Node(2)
m3=Node(3)
m4=Node(4)
m5=Node(5)
m6=Node(6)

root2=m1
m1.left=m2
m2.left=m4
m2.right=m5
m1.right=m3
m3.left=m6

def isIdentical(root1,root2):
    if root1==None and root2==None:
        return True
    elif root1==None or root2==None:
        return False
    if root1.data==root2.data:
        return isIdentical(root1.left,root2.left) and isIdentical(root1.right,root2.right)
    else:
        return False

print(isIdentical(root1,root2))
