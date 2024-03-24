# Qns : Linked List Cycle https://leetcode.com/problems/linked-list-cycle/

# Approach:
1) Use two pointers, fast and slow. 
2) Both fast and slow starts at head.
3) use while loop to check if fast.next and fast.next.next exists. If yes, move the pointers. Then check if true.
4) Otherwise, return false

---

# Solution:
```
def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
                
        return False
```
---

# Time Complexity
Time complexity will be O(n).
We have to loop through the entire array to figure out if theres cyclic.

# Space Complexity
Space complexity is O(1). We only store pointers to fast and slow.