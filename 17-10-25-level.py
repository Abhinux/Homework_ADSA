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

root=n1

def level(root,cnt=1):
    if root.left:
        h1=level(root.left,cnt+1)
    else:
        h1=cnt
    if root.right:
        h2=level(root.right,cnt+1)
    else:
        h2=cnt
    return max(h1,h2)

print(level(root))