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

    def reverse_ll(self):
        def link(t,r,self):
            if r.next!=None:
                link(t.next,r.next,self)
            else:
                self.head=r
            r.next=t
        temp=self.head
        link(self.head,self.head.next,self)
        temp.next=None
    
    def print_ll(self):
        l=''
        temp=self.head
        while(temp.next!=None):
            l+=str(temp.data)+' => '
            temp=temp.next
        l+=str(temp.data)+' => /o'
        print(l)
        print("Length is ",self.length)
            

l1=LinkedList(1)
l1.add_last(7)
l1.add_last(8)

l2=LinkedList(2)
l2.add_last(1)

def Add_two_ll(l1:LinkedList,l2:LinkedList):
    l1.reverse_ll()
    l2.reverse_ll()
    pointer1=l1.head
    pointer2=l2.head
    temp=(pointer1.data+pointer2.data)//10
    res=LinkedList((pointer1.data+pointer2.data)%10)
    pointer1=pointer1.next
    pointer2=pointer2.next
    while(pointer1!=None and pointer2!=None):
        Sum=pointer1.data+pointer2.data+temp
        res.add_last((Sum)%10)
        temp=Sum//10
        pointer1=pointer1.next
        pointer2=pointer2.next

    while(pointer2!=None):
        Sum=(temp+pointer2.data)
        res.add_last(Sum%10)
        temp=Sum//10
        pointer2=pointer2.next
    
    while(pointer1!=None):
        Sum=(temp+pointer1.data)
        res.add_last(Sum%10)
        temp=Sum//10
        pointer1=pointer1.next
    
    if temp>0:
        res.add_last(temp)

    res.reverse_ll()
    res.print_ll()

Add_two_ll(l1,l2)


