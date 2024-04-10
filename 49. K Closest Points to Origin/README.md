# Qns : K Closest Points to Origin https://leetcode.com/problems/k-closest-points-to-origin/

# Approach
1) create a array to store the distance
2) iterare through the list and calculate the distance, append (dist, x, y) to array
3) use heapq.heapify(minHeap) -> it's a function that creates a minHeap
4) then use heapq.heappop() to pop the min and append to another result array

# Solution:
```
def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for x, y in points:
            dist = (x**2) + (y**2)
            minHeap.append([dist, x, y])
        
        heapq.heapify(minHeap)
        result = []

        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            result.append([x,y])
            k -= 1
        return result
```
---

# Time Complexity
Time complexity is O(k log n), iterate through entire linked list.

# Space Complexity
Space complexity is O(n), only store pointers.