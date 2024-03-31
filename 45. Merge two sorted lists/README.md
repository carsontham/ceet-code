# Qns : Merge Two Sorted Lists https://leetcode.com/problems/merge-two-sorted-lists/

# Approach
1) Use two pointer approach. Create the head node(), use a While loop to add to this head node 
2) return head node.

# Solution:
```
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        cur = head

        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        if list1:
            cur.next = list1
        else:
            cur.next = list2
        
        return head.next
```
---

# Time Complexity
Time complexity is O(n), iterate through entire linked list.

# Space Complexity
Space complexity is O(n), store all nodes.