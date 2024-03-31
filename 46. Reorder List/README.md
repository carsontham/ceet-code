# Qns : Reorder Lists https://leetcode.com/problems/reorder-list/

# Approach
1) For this, we have to use slow-fast pointer, to half the linked list into 2 different list
2) Then, reverse the second linked list
3) Lastly, merge the first and second linked list.

# Solution:
```
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
```
---

# Time Complexity
Time complexity is O(n), iterate through entire linked list.

# Space Complexity
Space complexity is O(1), only store pointers.