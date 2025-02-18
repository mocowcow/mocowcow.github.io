---
layout      : single
title       : LeetCode 3452. Sum of Good Numbers
tags        : LeetCode Easy Simulation
---
biweekly contest 150。

## 題目

<https://leetcode.com/problems/sum-of-good-numbers/description/>

## 解法

按照題意模擬。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        N = len(nums)
        ans = 0
        for i, x in enumerate(nums):
            if (i-k < 0 or nums[i-k] < x) and (i+k >=N or nums[i+k] < x):
                ans += x

        return ans
```

判斷反向邏輯跳過也可以，拆成兩行感覺比較不容易錯。  

```python
class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        N = len(nums)
        ans = 0
        for i, x in enumerate(nums):
            if i-k >= 0 and nums[i-k] >= x:
                continue
            if i+k < N and nums[i+k] >= x:
                continue
            ans += x

        return ans
```
