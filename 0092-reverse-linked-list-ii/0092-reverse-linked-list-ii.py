# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        prev=None
        curr=head
        start=None
        end=None
        start_prev=None
        end_post=None
        while curr:
            left-=1
            right-=1
            if left==0:
                start=curr
                start_prev=prev
            if right==0:
                end=curr
                end_post=curr.next
                break
            prev=curr
            curr=curr.next
        curr=start
        prev=None
        while curr!=end_post:
            nex=curr.next
            curr.next=prev
            prev=curr
            curr=nex
        if start_prev:
            start_prev.next=end
        else:
            head=end
        start.next=end_post
        return head