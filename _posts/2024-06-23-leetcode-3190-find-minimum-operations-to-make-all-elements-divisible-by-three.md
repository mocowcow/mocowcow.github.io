---
layout      : single
title       : LeetCode 3190. Find Minimum Operations to Make All Elements Divisible by Three
tags        : LeetCode Easy Array Simulation
---
雙周賽 133。

## 題目

輸入整數陣列 nums。  
每次操作，你可以對任何元素加 1 或減 1。  

求最少需要幾次操作，才能使得所有元素都能被 3 整除。  

## 解法

一個數 x 對 3 求餘數只有三種可能：  

- 餘 0。可整除  
- 餘 1。減 1 後可整除  
- 餘 2。加 1 後可整除  

發現除了本來就整除以外，只需要一次操作就可滿足條件。  
題目轉換成判斷幾個數不被 3 整除。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(x % 3 != 0 for x in nums)
```

如果不是固定被 3 整除，而是被 k 整除怎辦？  

更通用的作法是先求 x / k 的商 r。  
r\*k 即為 x 向下找到的第一個 k 的倍數，而 (r + 1)\*k 是往上找的第一個 k 的倍數。  

```python
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        k = 3
        ans = 0
        for x in nums:
            r = x // k
            ans += min(x - r * k, (r + 1) * k - x)
        
        return ans
```
