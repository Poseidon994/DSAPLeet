# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def reverse(head, times):
            curr=head
            prev=None
            while times:
                times-=1
                nex=curr.next
                curr.next=prev
                prev=curr
                curr=nex
        size=2
        if not head:
            return head
        left=head
        prevleft=None
        res=None
        while True:
            right=left
            for i in range(size-1):
                if not right:
                    break
                else:
                    right=right.next
            if right:
                nextleft=right.next
                reverse(left,size)
                if prevleft:
                    prevleft.next=right
                prevleft=left
                if not res:
                    res=right
                left=nextleft
            else:
                if prevleft:
                    prevleft.next=left
                if not res:
                    res=left
                break
        return res