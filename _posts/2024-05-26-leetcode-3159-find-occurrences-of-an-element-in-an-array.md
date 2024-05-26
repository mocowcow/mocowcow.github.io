---
layout      : single
title       : LeetCode 3159. Find Occurrences of an Element in an Array
tags        : LeetCode Medium Array Simulation
---
雙周賽 131。根本和 Q1 沒兩樣的奇怪題目。  

## 題目

輸入整數陣列 nums, queries 還有整數 x。  

對於每個 queries[i]，你必須找到 x 在 nums 中出現第 queries[i] 次的索引。若不存在則為 -1。  

回傳包含查詢結果的陣列 answer。  

## 解法

先找 x 出現的所有索引，再處理查詢。  
注意查詢 q 是否超過 x 的出現次數即可。  

時間複雜度 O(N + Q)。  
空間複雜度 O(N)，答案空間不計入。  

```python
code class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        a = [i for i, num in enumerate(nums) if num == x]
        ans = []
        
        for q in queries:
            if q <= len(a):
                ans.append(a[q - 1])
            else:
                ans.append(-1)

        return ans
```
