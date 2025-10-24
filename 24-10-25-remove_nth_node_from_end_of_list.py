# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start=head
        end=head
        for i in range(n):
            if end.next==None:
                head=head.next
                return head
            end=end.next
        while(end.next!=None):
            end=end.next
            start=start.next
        start.next=start.next.next
        return head