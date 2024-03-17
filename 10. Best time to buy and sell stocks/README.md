# Qns : Best time to buy and sell stock https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Approach:
1) Using two pointers, check if left value is less than right value. If yes, use max() to get maxProfit
2) If no, this means that left value is larger than right value. thus, it shift left pointer to equal right pointer
3) when right pointer hits the end of the array, return the max profit
---

# Solution:
```
def maxProfit(self, prices: List[int]) -> int:
        
        left, right = 0, 1
        maxProfit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                curProfit = prices[right] - prices[left]
                maxProfit = max(maxProfit, curProfit)
            else:
                left = right
            right += 1
        
        return maxProfit 
```
---

# Time Complexity
Worst case : O(N)
Have to loop through the entire array.

# Space Complexity
Worst case : O(1)
Only store 3 values = left, right and maxProfit