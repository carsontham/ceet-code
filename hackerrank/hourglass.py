def hourglassSum(arr):
    # Write your code here
    maxSum = float('-inf')
    for r in range(1,5):
        for c in range(1,5):
            #upper 
            curSum = 0
            curSum += arr[r-1][c-1] + arr[r-1][c] + arr[r-1][c+1]
            #mid
            curSum += arr[r][c]
            #lower
            curSum += arr[r+1][c-1] + arr[r+1][c] + arr[r+1][c+1]
            maxSum = max(maxSum, curSum)
    return maxSum
            
            
            