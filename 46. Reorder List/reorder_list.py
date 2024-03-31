# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # first find the second half of the linkedlist using fast and slow
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = slow.next

        # reverse the second half
        cur = second_half
        prev = slow.next = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        second_half = prev

        # merge the two linked lst now
        first, second = head, prev

        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
