# Qns : Non Overlapping Intervals https://leetcode.com/problems/non-overlapping-intervals/

# Approach
1) use sort() to sort the intervals
2) prevEnd = intervals[1][0]
3) iterate through the array. check if start >= prevEnd. If yes, no actions to do, update prevEnd.
4) Else, this means there is overlap. we need to keep the one with shorter end using min(). increment the counter by 1
5) return the counter after the iteration

# Solution:
```
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0

        intervals.sort()
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                count += 1
                prevEnd = min(prevEnd, end)

        return count 
```
---

# Time Complexity
Time complexity is O(n log n), iterate through the array + sorting

# Space Complexity
Space complexity is O(n) due to sorting.