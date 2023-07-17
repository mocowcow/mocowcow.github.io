--- 
layout      : single
title       : LeetCode 2778. Sum of Squares of Special Elements
tags        : LeetCode Easy Array Simulation
---
周賽354。沒睡醒，想了半天才搞懂在問什麼，至少沒有WA就好。  

# 題目
輸入索引由1開始，且長度為n的整數陣列nums。  

對於nums[i]，如果n能夠被i整除，即n % i == 0，則稱nums[i]為**特殊元素**。  

求所有特殊元素**平方**後的總和。  

# 解法
題目說了索引從1開始計，很重要，這樣就不會出現0作為分母的情形。  

按照題目模擬，如果i能整除n，就把nums[i]的平方加入答案中。  

時間複雜度O(N)。  
空間複雜度O(1)。  

```python
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        N=len(nums)
        ans=0
        
        for i in range(1,N+1):
            if N%i==0:
                ans+=nums[i-1]*nums[i-1]
                
        return ans
```
