# Qns : Insert Interval https://leetcode.com/problems/insert-interval/

# Approach
1) iterate through the loop, check if newInterval start and end has any overlapping.
2) if no, then add to result.
3) if there is overlapping, update the newInterval. At the end of the iteration, add the newInterval and return result

# Solution:
```
 def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
            
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
        
        result.append(newInterval)

        return result
            
```
---

# Time Complexity
Time complexity is O(n), worse case is to iterate the entire array.

# Space Complexity
Space complexity is O(n), store all intervals incase if no overlapping.