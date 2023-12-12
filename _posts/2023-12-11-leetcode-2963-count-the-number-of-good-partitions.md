---
layout      : single
title       : LeetCode 2963. Count the Number of Good Partitions
tags        : LeetCode Hard Array Greedy HashTable
---
周賽375。

## 題目

輸入正整數陣列nums。  

將陣列分割成一個或多個**連續**的子陣列，若沒有任意兩個子陣列包含相同數字，則稱為**好的**。  

求nums有多少好的分割方式。  
答案可能很大，先模10^9+7後回傳。  

## 解法

沒有任意兩個子陣列包含相同數字，其實就是**相同的數字**都要在同一個子陣列內。  
若將nums[i]加入區間中，則該區間的右邊界至少為nums[i]**最後**出現的位置。不斷更新右邊界，直到當前元素正好是右邊界為止，

例如[1,2,3,4]最多可以分割成[1],[2],[3],[4]四個最小的**不重複區間**。  
至於[1,2,1,3]，將nums[0]加入區間後，右邊界變成至少是2。接著加入nums[1]，右邊界還是2。最後加入nums[2]，右邊界還是2。  
因此最小可以分割出[1,2,1]和[3]兩個不重複區間。  

而這些區間也可以選擇不分割，構成同一個子陣列。  
如果最多有cnt個區間，共有cnt-1個分割點，每個分割點可以選擇分割/不分割，總共有2^(cnt-1)種分割方案。  

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        MOD=10**9+7
        N=len(nums)
        
        last={x:i for i,x in enumerate(nums)}
        cnt=0
        rb=0
        for i,x in enumerate(nums):
            rb=max(rb,last[x])
            if i==rb: # nums[i] is right bound of a interval
                cnt+=1
        
        return pow(2,cnt-1,MOD)
```
