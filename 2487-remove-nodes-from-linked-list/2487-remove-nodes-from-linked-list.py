# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr=head
        prev=None
        while curr:
            nex=curr.next
            curr.next=prev
            prev=curr
            curr=nex
        st=[]
        st.append(prev.val)
        curr=prev
        curr_head=curr
        curr=curr.next
        while curr:
            while st and st[-1] <= curr.val:
                st.pop()
            if st:                    # something bigger survives ahead → curr is dominated
                prev.next = curr.next          # remove curr
            else:                      # curr is the new max so far
                st.append(curr.val)
                prev = curr                    # only advance prev when curr is KEPT
            curr = curr.next
        curr=curr_head
        prev=None
        while curr:
            nex=curr.next
            curr.next=prev
            prev=curr
            curr=nex
        return prev