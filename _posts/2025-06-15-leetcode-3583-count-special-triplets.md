---
layout      : single
title       : LeetCode 3583. Count Special Triplets
tags        : LeetCode Medium Math
---
weekly contest 454。

## 題目

<https://leetcode.com/problems/count-special-triplets/description/>

## 解法

三元組的值會是 [2x, x, 2x]。  

維護左右邊剩餘的元素個數 left, right。  
枚舉作為中間 x，根據乘法原理，共有 left[2x] * right[2x] 種選法。  
記得取 MOD。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
MOD = 10 ** 9 + 7


class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        left = Counter()
        right = Counter(nums)
        ans = 0
        for x in nums:
            right[x] -= 1
            ans += left[x*2] * right[x*2] % MOD
            left[x] += 1

        return ans % MOD
```
