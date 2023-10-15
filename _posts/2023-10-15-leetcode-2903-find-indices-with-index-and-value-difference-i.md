---
layout      : single
title       : LeetCode 2903. Find Indices With Index and Value Difference I
tags        : LeetCode Easy Array Simulation Greedy
---
周賽367。

## 題目

輸入長度n的整數陣列nums，還有整數indexDifference、整數valueDifference。  

你的目標是找到兩個索引i和j，兩者都介於[0, n-1]間，且滿足以下條件：  

- abs(i - j) >= indexDifference  
- abs(nums[i] - nums[j]) >= valueDifference  

若存在i, j，則回傳整數陣列answer，其中answer = [i, j]；否則answer = [-1, -1]。若有多個答案，則回傳任意一個。  

注意：i和j可以相等。  

## 解法

測資不大的話，暴力枚舉所有[i, j]，只要符合兩條件則回傳。  

時間複雜度O(n^2)。  
空間複雜度O(n^2)。  

```python
class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        N=len(nums)
        
        for i in range(N):
            for j in range(i,N):
                diff=abs(nums[j]-nums[i])
                if j-i>=indexDifference and diff>=valueDifference:
                    return [i,j]
                
        return [-1,-1]
```

也可以枚舉i或j其中之一，這樣可以確保另一個索引來自相同方向。  
這裡枚舉j，並維護位於左方、且距離j至少indexDifference的索引i。

為了使abs(nums[i]-nums[j])盡可能大，nums[i]要比nums[j]要馬大很多、不然就是小很多。  
維護可用nums[i]中會出現的最大、最小值，只要其中一者能與nums[j]差值達到valueDifference則回傳答案。  

時間複雜度O(N)。  
空間複雜度O(1)。  

```python
class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        mx=-inf
        mn=inf
        mxi=mni=None
        for j,x in enumerate(nums):
            i=j-indexDifference
            if i>=0:
                y=nums[i]
                
                # upd max
                if y>mx:
                    mx=y
                    mxi=i
                    
                # upd min
                if y<mn:
                    mn=y
                    mni=i
                    
                # check ans
                if x-mn>=valueDifference:
                    return [mni,j]
                if mx-x>=valueDifference:
                    return [mxi,j]
                
        return [-1,-1]
```
