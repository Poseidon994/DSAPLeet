class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        first = head

        prev = None
        curr = second
        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        second = prev

        while second:
            a, b = first.next, second.next
            first.next = second
            second.next = a
            first, second = a, b