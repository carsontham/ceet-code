# Qns : Contains Duplicate https://leetcode.com/problems/contains-duplicate/

# Approach:
Use a set to store numbers so only unique values will be in the set.
Iterate through the array and store nums in set if not already in set.
If exists in set, there is a duplicate and thus return True.

---

# Solution:
```
def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # create an empty set
        unique = set()

        # iterate through the list and append to set if not already in set
        # if already in set, return True
        for num in nums:
            if num in unique:
                return True
            else:
                unique.add(num)
        
        return False
```
---

# Time Complexity
Worst case : O(n)
Have to loop through the entire array, thus O(n).

# Space Complexity
Worst case : O(n)
Have to store elements in set. Worse case if there is no duplicate and thus memory = n items.