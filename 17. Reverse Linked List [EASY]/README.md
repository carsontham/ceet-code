# Qns : Reverse Linked List https://leetcode.com/problems/reverse-linked-list/

# Approach:
1) Use two pointers, prev and cur.
2) Prev = None, cur = head
3) use while loop to flip the directions until cur is None( meaning no more nodes )
4) Return prev (which is now the new head)

---

# Solution:
```
 def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            temp = cur.next 
            cur.next = prev
            prev = cur
            cur = temp
        return prev
```
---

# Time Complexity
Time complexity will be O(n).
We have to loop through the entire array thus O(n)

# Space Complexity
Space complexity is O(1). We only store pointers to prev and cur and temp.