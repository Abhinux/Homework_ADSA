class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class LinkedList:
    def __init__(self,data):
        self.head=Node(data)
        self.length=1

    def add_head(self,data):
        new_head=Node(data)
        new_head.next=self.head
        self.head=new_head
        self.length+=1


    def add_last(self,data):
        last=Node(data)
        temp=self.head
        while(temp.next!=None):
            temp=temp.next
        temp.next=last
        self.length+=1
    
    def insert_at(self,data,num):
        ele=Node(data)
        temp=self.head
        while(num>1 and temp.next!=None):
            temp=temp.next
            num-=1
        if num==1 and temp.next!=None:
            ele.next=temp.next
            temp.next=ele
            self.length+=1
        elif num==1 and temp.next==None:
            temp.next=ele 
            self.length+=1
        else:
            print("Num Invalid")
    
    def remove_last(self):
        temp=self.head
        while(temp.next.next!=None):
            temp=temp.next
        temp.next=None
        self.length-=1


    def remove_beginning(self):
        temp=self.head
        if temp.next==None:
            print("Invalid")
        else:
            self.head=temp.next
            self.length-=1

    def remove_from_begin_at(self,num):
        num-=1
        temp=self.head
        if temp.next!=None:
            while(num>1 and temp.next.next!=None):
                temp=temp.next
                num-=1
            if num==1:
                temp.next=temp.next.next
                self.length-=1
            else:
                print("Num Invalid")
        else:
            print("LinkedList only has 1 element")

    def remove_from_end_at(self,num):
        i=self.length-num
        temp=self.head
        if temp.next!=None :
            while(i>1 and temp.next.next!=None):
                temp=temp.next
                i-=1
            if i==1:
                temp.next=temp.next.next
                self.length-=1
            else:
                print("Num Invalid")
        else:
            print("LinkedList only has 1 element")

    def remove_middle(self):
        mid=self.length//2
        if self.length%2==0:
            self.remove_from_begin_at(mid)
        else:
            self.remove_from_begin_at(mid+1)

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
    
LL=LinkedList(1)
LL.add_last(2)
LL.add_last(3)
LL.add_last(4)
LL.add_last(5)
LL.print_ll()

LL.insert_at(9,3)
LL.print_ll()
            
LL.remove_last()
LL.print_ll()

LL.remove_beginning()
LL.print_ll()

LL.remove_from_begin_at(2)
LL.print_ll()

LL.add_head(6)
LL.print_ll()

LL.add_last(7)
LL.print_ll()

LL.remove_from_end_at(2)
LL.print_ll()

LL.remove_middle()
LL.print_ll()

LL.reverse_ll()
LL.print_ll()