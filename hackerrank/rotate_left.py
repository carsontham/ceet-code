def rotLeft(a, d):
    
    d = d % len(a)
    left, right = 0, len(a)-1
    
    while left < right:
        a[left], a[right] = a[right], a[left]
        left += 1
        right -= 1
    
    left, right = 0, len(a)-d-1
    
    while left < right:
        a[left], a[right] = a[right], a[left]
        left += 1
        right -= 1
    
    left, right = len(a)- d, len(a)-1
    while left < right:
        a[left], a[right] = a[right], a[left]
        left += 1
        right -= 1
    
    return a