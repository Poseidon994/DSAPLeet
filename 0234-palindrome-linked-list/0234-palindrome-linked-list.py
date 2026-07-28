# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if not head.next:
            return True
        slow=head
        fast=head
        while fast and fast.next:
            slow= slow.next
            fast=fast.next.next
        
        curr=slow
        prev=None
        while curr:
            nex= curr.next
            curr.next=prev
            prev=curr
            curr=nex
        right,left=prev,head
        while right:
            if left.val!=right.val:
                return False
            left=left.next
            right=right.next
        return True