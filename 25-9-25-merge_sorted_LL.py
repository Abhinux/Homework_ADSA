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

    def print_ll(self):
        l=''
        temp=self.head
        while(temp.next!=None):
            l+=str(temp.data)+' => '
            temp=temp.next
        l+=str(temp.data)+' => /o'
        print(l)
        print("Length is ",self.length)

def merge_LL(LL1,LL2):
    num1=LL1.head
    num2=LL2.head
    res=LinkedList(None)
    temp=res.head
    while(num1!=None and num2!=None):
        if num1.data<=num2.data:
            res.add_last(num1.data)
            num1=num1.next
        else:
            res.add_last(num2.data)
            num2=num2.next

    while(num1!=None):
        res.add_last(num1.data)
        num1=num1.next

    while(num2!=None):
        res.add_last(num2.data)
        num2=num2.next

    res.head=res.head.next
    res.length-=1

    return res



LL1=LinkedList(1)
LL1.add_last(3)
LL1.add_last(5)

LL2=LinkedList(2)
LL2.add_last(4)
LL2.add_last(6)

res=merge_LL(LL1,LL2)

res.print_ll()

