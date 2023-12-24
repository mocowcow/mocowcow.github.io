---
layout      : single
title       : LeetCode 2970. Count the Number of Incremovable Subarrays I
tags        : LeetCode Easy Array Simulation
---
雙周賽120。這個incremovable還真不知道怎麼翻譯，中國站翻做**移除遞增**。  

## 題目

輸入正整數陣列nums。  

若nums某個子陣列被移除後，可以使得剩餘元素**嚴格遞增**，則稱為**移除遞增**子陣列。  
例如從[5, 3, 4, 6, 7]中移除[3, 4]後變成[5, 6, 7]，所以是**移除遞增**子陣列。  

求nums有多少**移除遞增**子陣列。  

注意：空陣列也視為嚴格遞增。  

## 解法

先來個暴力解，枚舉所有子陣列移除後的結果。  

時間複雜度O(N^2)。  
空間複雜度O(N)。  

```python
class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        N=len(nums)
        
        def ok(i,j):
            sub=nums[:i]+nums[j+1:]
            for a,b in pairwise(sub):
                if a>=b:
                    return False
            return True
        
        ans=0
        for i in range(N):
            for j in range(i,N):
                if ok(i,j):
                    ans+=1
                    
        return ans
```
