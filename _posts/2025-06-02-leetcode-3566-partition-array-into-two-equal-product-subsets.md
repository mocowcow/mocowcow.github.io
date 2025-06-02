---
layout      : single
title       : LeetCode 3566. Partition Array into Two Equal Product Subsets
tags        : LeetCode Medium Simulation DFS
---
weekly contest 452。

## 題目

<https://leetcode.com/problems/partition-array-into-two-equal-product-subsets/description/>

## 解法

nums 中的元素分成兩組，使得兩組乘積相等。  

N = 12 可以暴力枚舉每個元素放到哪組。  
乘積超過 target 立即退出，避免溢位 (雖然 python 沒差)。  

時間複雜度 O(2^N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        N = len(nums)

        def dfs(i, p, q):
            if p > target or q > target:
                return False
            if i == N:
                return p == q == target
            x = nums[i]
            return dfs(i+1, p*x, q) or dfs(i+1, p, q*x)

        return dfs(0, 1, 1)
```
