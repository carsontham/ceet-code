# Qns : Three Sum https://leetcode.com/problems/3sum/

# Approach:
1) Sort the array using array.sort()
2) iterate through each element in the array
3) notice how in each iteration, the remaining two numbers + cur number, must be equal to 0? 
4) thus, use 2 pointers approach to check for the other numbers
5) If all 3 numbers add up to = 0, then append to the result array. In addition, we have to shift the left pointer now to check if there are other possibility whereby A + B +C =0 exist and also, A + D + E = 0



---

# Solution:
```
def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            cur = numbers[left] + numbers[right]
            
            if cur > target:
                right -= 1

            elif cur < target:
                left += 1
            else:
                return [left+1, right+1] 
```
---

# Time Complexity
Time complexity will be O(n^2), because for each element in the array, we conduct a twoSum approach, which take O(n) time. Including the loop will be n * n

# Space Complexity
Space complexity is O(1) or O(n), as sort() may result in more memory
