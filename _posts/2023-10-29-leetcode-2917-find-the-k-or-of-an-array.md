---
layout      : single
title       : LeetCode 2917. Find the K-or of an Array
tags        : LeetCode Easy Array BitManipulation Simulation
---
周賽369。這題目有點難懂，寫起來倒是沒難度。  

## 題目

輸入整數陣列nums，還有整數k。  

nums的**K-or數**，是一個滿足以下條件的非負整數：  

- 若nums中有至少k個數的第i個位元是1，則**K-or數**的該位元也是1  

求nums的**K-or數**。  

## 解法

按照題意模擬。  

時間複雜度O(N log MX)，其中MX為max(nums)。  
空間複雜度O(log MX)。  

```python
class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        ans=0
        for i in range(32):
            cnt=0
            for x in nums:
                if (1<<i)&x:
                    cnt+=1
            if cnt>=k:
                ans|=(1<<i)
                
        return ans
```
