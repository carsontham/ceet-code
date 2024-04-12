# Qns : Longest Consecutive Sequence https://leetcode.com/problems/longest-consecutive-sequence/

# Approach:
1) Cast the array into a set, loop through the array and check if the current number has a prev number
2) If no, it is the start of a sequence. 
3) Then use a while loop to check if the next sequential number exists in the set
4) If yes, increase length of sequence. Otherwise, exit loop and compare the longest_seq and return it.

---

# Solution:
```
def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # use a set to remove duplicates 
        numSet = set(nums)

        # initialized longest as 0
        longest_seq = 0

        # loop through the original array
        for num in numSet:
            # if there is no left number, it is start of a sequence
            if (num-1) not in numSet:

                # now check if there is a next number in the numSet
                # if yes, increase length by 1
                length = 0
                while (num+length) in numSet:
                    length += 1
                
                # get the longest sequence
                longest_seq = max(longest_seq, length)

        return longest_seq
```
---

# Time Complexity
Worst case : O(N)
Only one iteration is done in the set. 
Example: [ 1, 2, 3, 5, 6, 9, 10, 11 ,12 ]
Seq        ---3---  -2-    ---- 4 ----
Longest sequence is 4.

For the start of seq, the loop spawns a while loop to continue looking for sequence.
After breaking, the iteration goes from index position 0 to position 1. 
But at this juncture, (2 - 1) exists in the set, and thus the for loop does NOTHING. 
Same for the other leading numbers.

Thus, it is save to say that the time complexity is O(n).

# Space Complexity
Worst case : O(n)
We only create an additional set in memory.
