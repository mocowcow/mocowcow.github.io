--- 
layout      : single
title       : LeetCode 2395. Find Subarrays With Equal Sum
tags        : LeetCode Easy Array
---
雙周賽86。有點誤導性的題目名，與其說subarray，改成pair更貼切。  

# 題目
輸入整數陣列nums，判斷是否存在兩個長度為2且總和相等的子陣列。請注意，兩個子陣列必須從不同的索引開始。  
若存在則回傳true，否則回傳false。  

# 解法
說要找子陣列，但子陣列長度固定為2，那其實就只是兩個相鄰的數字求和。  

維護一個集合紀錄出現過的總和，並列舉所有可能的子陣列。若途中出現重複的值則回傳true，否則在最後回傳false。  

```python
class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        N=len(nums)
        s=set()
        for i in range(1,N):
            sm=nums[i]+nums[i-1]
            if sm in s:return True
            s.add(sm)
            
        return False
```

在python內建的itertools裡面，有一個叫做pairwise的函數，一樣會疊代所有的相鄰元素供使用。  

```python
class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        s=set()
        for a,b in pairwise(nums):
            sm=a+b
            if sm in s:return True
            s.add(sm)
            
        return False
```