class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class LinkedList:
    def __init__(self,data):
        self.head=Node(data)

    def add_last(self,data):
        last=Node(data)
        temp=self.head
        while(temp.next!=None):
            temp=temp.next
        temp.next=last
    
    def insert_at(self,data,num):
        i=num
        ele=Node(data)
        temp=self.head
        while(i>1 and temp.next!=None):
            temp=temp.next
            i-=1
        if i==1 and temp.next!=None:
            ele.next=temp.next
            temp.next=ele
        elif i==1 and temp.next==None:
            temp.next=ele 
        else:
            print("Num Invalid")
    
    def remove_last(self):
        temp=self.head
        while(temp.next.next!=None):
            temp=temp.next
        temp.next=None


    def remove_beginning(self):
        temp=self.head
        if temp.next==None:
            print("Invalid")
        else:
            self.head=temp.next

    def remove_at(self,num):
        i=num-1
        temp=self.head
        if temp.next!=None:
            while(i>1 and temp.next.next!=None):
                temp=temp.next
                i-=1
            if i==1:
                temp.next=temp.next.next
            else:
                print("Num Invalid")
        else:
            print("LinkedList only has 1 element")

    
    def print_ll(self):
        l=''
        temp=self.head
        while(temp.next!=None):
            l+=str(temp.data)+' => '
            temp=temp.next
        l+=str(temp.data)+' => /o'
        print(l)
    
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

LL.remove_at(2)

LL.print_ll()
