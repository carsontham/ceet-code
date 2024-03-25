# Qns : Remove Nth Node From End of List https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Approach:
1) Use two pointers, fast and slow
2) Move fast by n times. If fast is None, return the head.next()
3) use while loop to move fast and slow
4) when fast.next is None, make slow.next = slow.next.next. Return head
---

# Solution:
```
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head

        for _ in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next

        return head
```
---

# Time Complexity
Time complexity is O(n). Iterate through the entire linked list in worse case.

# Space Complexity
Space complexity is O(1). Only kept pointers to fast and slow.