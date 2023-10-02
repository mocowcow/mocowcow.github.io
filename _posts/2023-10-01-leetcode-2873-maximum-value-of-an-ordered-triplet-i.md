---
layout      : single
title       : LeetCode 2873. Maximum Value of an Ordered Triplet I
tags        : LeetCode Easy Array Simulation SortedList PrefixSum
---
周賽365。

## 題目

輸入整數陣列nums。  

回傳所有索引三元組(i, j, k)的最大值，其中 i < j < k。  
若所有值都是負數，則回傳0。  

索引三元組(i, j, k)的值等於(nums[i] - nums[j]) * nums[k]。  

## 解法

在nums長度夠小的情況下，暴力枚舉還是挺方便的。  

時間複雜度O(N^3)。  
空間複雜度O(1)。  

```python
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        N=len(nums)
        ans=0
        
        for i in range(N):
            for j in range(i+1,N):
                for k in range(j+1,N):
                    ans=max(ans,(nums[i]-nums[j])*nums[k])
                    
        return ans
```

枚舉作為中心點的j，為了使得值盡可能大，則左方的nums[i]越大越好、右方的nums[k]也是越大越好。  
左方需要存取最大值，支持插入；右邊需要存取最大值，支持隨機刪除。  
正好可以使用sorted list來維護兩方的值。  

維護兩個sorted list，叫做L和R，分別裝著位於nums[j]左右方的元素。  
以nums初始化R後，遍歷nums，枚舉x = nums[j]：  

- 先從R中刪除x  
- 從L和R找到最大值  
- 帶入公式，更新答案  
- 將x加入L  

注意答案不允許負數，ans初始值設為0。  

時間複雜度O(N log N)。  
空間複雜度O(N)。  

```python
from sortedcontainers import SortedList as SL

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        N=len(nums)
        ans=0
        L=SL()
        R=SL(nums)
        
        for j,x in enumerate(nums):
            R.remove(x)
            if L and R:
                ans=max(ans,(L[-1]-x)*R[-1])
            L.add(x)
            
        return ans
```

sorted list維護的是兩邊的最大值，這時候又是老朋友**前後綴分解**上場了。  
先預處理前後綴的最大值，之後一次遍歷計算答案。  

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        N=len(nums)
        
        pref=[0]*N
        pref[0]=nums[0]
        for i in range(1,N):
            pref[i]=max(pref[i-1],nums[i])
        
        suff=[0]*N
        suff[-1]=nums[-1]
        for i in reversed(range(N-1)):
            suff[i]=max(suff[i+1],nums[i])
        
        ans=0
        for j in range(1,N-1):
            val=(pref[j-1]-nums[j])*suff[j+1]
            ans=max(ans,val)
            
        return ans
```
