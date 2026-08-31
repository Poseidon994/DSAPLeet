# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        curr=head
        if not curr or not curr.next:
            return [-1,-1]
        prev=head
        curr=curr.next
        res=[]
        i=2
        while curr and curr.next:
            if (curr.val>prev.val and curr.val>curr.next.val) or (curr.val<prev.val and curr.val<curr.next.val):
                res.append(i)
            i+=1
            prev=curr
            curr=curr.next
        if len(res)<2:
            return [-1,-1]
        id1,id2=max(res),min(res)
        ans=float('inf')
        for i in range(1,len(res)):
            diff=res[i]-res[i-1]
            ans=min(ans,diff)
        return [ans, id1-id2]