# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            slow=head.next
            if slow==None:
                return None
            fast=head.next.next
            if fast==None:
                return None
            while(fast!=slow and fast!=None and fast.next!=None):
                slow=slow.next
                fast=fast.next.next
            if fast==None or fast.next==None:
                return None
            new=head
            while(new!=slow):
                new=new.next
                slow=slow.next
            return new
        return None