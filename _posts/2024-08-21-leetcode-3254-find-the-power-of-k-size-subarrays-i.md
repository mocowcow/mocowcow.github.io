---
layout      : single
title       : LeetCode 3254. Find the Power of K-Size Subarrays I
tags        : LeetCode Medium Simulation
---
biweekly contest 137。  

## 題目

輸入長度 n 的正整數陣列 nums，還有正整數 k。  

一個陣列的**力量**定義為：  

- 若陣列是**連續**且**遞增**的，則力量為其最大元素。  
- 否則是 -1。  

你必須找到所有大小為 k 的**子陣列**的力量。  
回傳長度 n - k + 1 的整數陣列 results，其中 results[i] 代表 nums[i..(i + k - 1)] 的力量。  

## 解法

按照題意，連續指的是兩個相鄰數字相差 1。  
暴力模擬，枚舉所有大小 k 的子陣列，並檢查是否合法。  

時間複雜度 O(N^3)。  
空間複雜度 O(1)。  

```python
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        ans = [-1] * (N - k + 1)
        for i in range(N - k + 1):
            for j in range(i + 1, i + k):
                if nums[j] != nums[j - 1] + 1:
                    break
            else:
                ans[i] = nums[i + k - 1]

        return ans
```
