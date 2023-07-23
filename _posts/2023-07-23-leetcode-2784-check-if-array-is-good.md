--- 
layout      : single
title       : LeetCode 2784. Check if Array is Good
tags        : LeetCode Easy Array Simulation Sorting
---
雙周賽109。

# 題目
輸入整數陣列nums。  
若一個陣列是base[n]的排列，則稱為**好的**。  

base[n] = [1, 2, ..., n - 1, n, n]。  
也就是說，一個長度為n+1的陣列，其中1\~n-1各出現一次，然後n出現兩次。  
例如base[1] = [1,1]，然後base[3] = [1,2,3,3]

若nums是**好的**則回傳true，否則回傳false。  

# 解法
按照題意，建構出長度為N的base陣列，將nums排序後檢查兩者是否相同即可。  

時間複雜度O(N log N)。  
空間複雜度O(N)。  

```python
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        N=len(nums)
        base=list(range(1,N))+[N-1]
        
        return sorted(nums)==base
```
