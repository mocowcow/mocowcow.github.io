---
layout      : single
title       : LeetCode 2913. Subarrays Distinct Element Sum of Squares I
tags        : LeetCode Easy Array HashTable
---
雙周賽116。既是Q1又是Q4，測資範圍不同，難度大概差了二十倍。  

## 題目

輸入整數陣列nums。  

nums子陣列的**不同計數**定義為：  

- 令nums[i..j]為nums的子陣列，其中包含介於[i, j]之間的所有索引對應的元素  
- nums[i..j]的**不同計數**等於nums[i..j]中不同值的數量  

求所有子陣列**不同計數**的**平方和**。  
答案可能很大，先模10^9+7後回傳。  

## 解法

暴力枚舉所有子陣列，集合去重後得到**不同計數**，平方後加入答案。  

時間複雜度O(N^3)。  
空間複雜度O(N)。  

```python
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        N=len(nums)
        ans=0
        
        for i in range(N):
            for j in range(i,N):
                sub=nums[i:j+1]
                s=set(sub)
                ans+=len(s)**2
                
        return ans
```

Q4的nums長度高達10^5，真的有夠變態，晚點再來補答案。  
