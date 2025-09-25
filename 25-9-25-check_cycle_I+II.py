class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self,data):
        self.head=Node(data)
        self.length=1

    def add_last(self,data):
        last=Node(data)
        temp=self.head
        while(temp.next!=None):
            temp=temp.next
        temp.next=last
        self.length+=1

    def cycle_at(self,num):
        temp=self.head
        temp2=self.head
        while(num>1 and temp.next!=None):
            temp=temp.next
            num-=1
        while(temp2.next!=None):
            temp2=temp2.next
        temp2.next=temp
    
LL=LinkedList(1)
LL.add_last(2)
LL.add_last(3)
LL.add_last(4)
LL.add_last(5)
LL.add_last(6)
LL.add_last(7)
LL.add_last(8)
LL.cycle_at(4)

def check_cycle(LL:LinkedList):
    temp=LL.head
    slow=LL.head.next
    fast=LL.head.next.next

    while(slow!=fast):
        slow=slow.next
        fast=fast.next.next

    while(temp!=slow):
        temp=temp.next
        slow=slow.next
    
    print(temp.data)

check_cycle(LL)