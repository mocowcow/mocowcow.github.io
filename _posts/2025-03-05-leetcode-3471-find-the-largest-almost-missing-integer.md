---
layout      : single
title       : LeetCode 3471. Find the Largest Almost Missing Integer
tags        : LeetCode Easy Simulation
---
weekly contest 439。  
這題有點陷阱，好多人都中計，其中不乏高手。  

## 題目

<https://leetcode.com/problems/find-the-largest-almost-missing-integer/>

## 解法

枚舉所有大小 k 的子陣列，並找出子陣列出現的**不同元素**，然後再對幾些元素頻率加 1。  
最後枚舉出現過的元素，只有**出現一次**的才符合要求，更新答案。  

時間複雜度 O(N^2)。  
空間複雜度 O(N)。  

```python
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        N = len(nums)
        d = Counter()
        for i in range(N-k+1):
            sub = nums[i:i+k]
            for x in set(sub):
                d[x] += 1

        ans = -1
        for k, v in d.items():
            if v == 1 and k > ans:
                ans = k

        return ans
```
