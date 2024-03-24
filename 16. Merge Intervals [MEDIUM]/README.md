# Qns : Merge Intervals https://leetcode.com/problems/merge-intervals/

# Approach:
1) First sort the by it's "start" value, using lambda `intervals.sort(key = lambda i : i[0])`
2) Set the first interval into output array
3) Loop through the intervals, check if cur start < prev end. if yes, output = max of either Ends
4) else, append new interval

---

# Solution:
```
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start,end])

        return output
```
---

# Time Complexity
Time complexity will be O(n log n).
Reason is sort() takes time O(n log n). We also iterate through the array which is O(n).
Ultimately the time complexity is O(n log n)

# Space Complexity
Space complexity is O(n).
Worst case is no overlap, so we append all the arrays to output, thus O(n).
In addition, sorting also takes O(n) space.
