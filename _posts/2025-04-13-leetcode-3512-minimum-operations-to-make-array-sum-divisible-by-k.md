---
layout      : single
title       : LeetCode 3512. Minimum Operations to Make Array Sum Divisible by K
tags        : LeetCode Easy Math
---
biweekly contest 154。

## 題目

<https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/description/>

## 解法

x 若能被 k 整除，代表 x % k == 0。  

每次操作可以將 sum(nums) 減少 1。  
若要使得 sum(nums) % k = 0，則需要將餘數減少至 0。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k
```
