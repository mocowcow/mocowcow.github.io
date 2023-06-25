--- 
layout      : single
title       : LeetCode 2748. Number of Beautiful Pairs
tags        : LeetCode Easy Array Simulation
---
周賽351。

# 題目
輸入整數陣列nums。  
對於一個滿足0 <= i < j < nums.length的索引對(i,j)，如果nums[i]的第一個數字和nums[j]的最後一個數字互質，則稱為**美麗的**。  

求總共有多少**美麗的**索引對。  

# 解法
按照題目模擬，窮舉所有(i,j)，取出對應的數字求gcd即可。  

時間複雜度O(N^2 \* log N)。  
空間複雜度O(1)。  

```python
class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        N=len(nums)
        ans=0
        
        for j in range(N):
            last=nums[j]%10
            for i in range(j):
                first=nums[i]
                while first>=10:
                    first//=10
                if gcd(last,first)==1:
                    ans+=1
                    
        return ans
```
