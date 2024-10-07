---
layout      : single
title       : LeetCode 3309. Maximum Possible Number by Binary Concatenation
tags        : LeetCode Medium Simulation
---
weekly contest 418。  
這題用 python 寫起來是真方便。  

## 題目

輸入大小為 3 的整數陣列 nums。  

你可以把 nums 任意排列，並將他們的**二進制表示**全部**連接**起來，求可得到的**最大**數值。  

注意：任何數的二進制表示都**不含**前導零。  

## 解法

首先將每個數轉成二進制字串。  

因為只有 3 個數，共只有 3! = 6 種排列。  
暴力枚舉所有排列，找到最大值即可。  

時間複雜度 O(log MX)，其中 MX = max(nums)。  
空間複雜度 O(log MX)。  

```python
class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        a = [bin(x)[2:] for x in nums]
        ans = 0
        for p in permutations(a):
            s = "".join(p)
            ans = max(ans, int(s, 2))

        return ans
```
