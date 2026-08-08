# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseEvenLengthGroups(self, head):
        def reverse(head, times):
            prev, curr = None, head
            for _ in range(times):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev  # new head of the reversed segment

        prev_tail = head        # group size 1 is always odd — never reversed, skip it outright
        start = head.next
        length = 2

        while start:
            # find how many nodes are ACTUALLY in this group (may be < length if list runs out)
            node = start
            count = 1
            while count < length and node.next:
                node = node.next
                count += 1
            next_group_start = node.next

            if count % 2 == 0:
                new_head = reverse(start, count)
                prev_tail.next = new_head
                start.next = next_group_start
                prev_tail = start          # start is now the tail after reversal
            else:
                prev_tail = node           # leave as-is, tail is just the last node scanned

            start = next_group_start
            length += 1

        return head