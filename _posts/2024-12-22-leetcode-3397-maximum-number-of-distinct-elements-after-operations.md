---
layout      : single
title       : LeetCode 3397. Maximum Number of Distinct Elements After Operations
tags        : LeetCode Medium Sorting Greedy
---
weekly contest 429。

## 題目

輸入整數陣列 nums 和整數 k。  

你可以對陣列中的每個元素都**操作最多一次**：  

- 將 [-k, k] 內的整數加到元素上。  

求操作後，nums 中可以擁有的**最大**不同元素數量。  

## 解法

nums 中的順序不影響答案，先排序一下。  

遍歷 nums 中每個元素 x，考慮要加多少。  
因為剩餘元素都大於等於 x，所以盡量對 x 加上負數，才能**貪心**的保留更多空間給後方。  

最理想是選 x-k，最差是 x+k。越大的 k 會搶到後面的空間。
因為依序貪心處理，可以保證上一個元素操作後的值 prev 是已有的最大值，所以 x 修改後至少是 prev+1。  

若 x+k 不足 prev+1，那就跳過不管。  
否則選 x-k 和 prev+1 的最大值。  

時間複雜度 O(N log N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        prev = -inf
        for x in nums:
            if x+k > prev:
                t = max(prev+1, x-k)
                ans += 1
                prev = t

        return ans
```
