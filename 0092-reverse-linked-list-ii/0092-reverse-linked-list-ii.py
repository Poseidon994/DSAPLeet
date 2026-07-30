class Solution(object):
    def reverseBetween(self, head, left, right):
        dummy = ListNode(0, head)
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next          # prev = node just before `left`

        curr = prev.next              # curr will always be the (unchanged) start of the sublist
        for _ in range(right - left):
            nex = curr.next
            curr.next = nex.next
            nex.next = prev.next
            prev.next = nex

        return dummy.next