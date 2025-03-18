---
layout      : single
title       : LeetCode 3483. Unique 3-Digit Even Numbers
tags        : LeetCode Easy Simulation
---
biweekly contest 152。
有點囉嗦的暴力題。  

## 題目

<https://leetcode.com/problems/unique-3-digit-even-numbers/>

## 解法

從 digits 選三個數字，求能組能幾個**三位數的偶數**。  
且不可有前導零。  

直接暴力三層迴圈，枚舉三個不同索引 i, j, k 組成數字 val。  
判斷 val 是否為三位數 (至少 100) 且為偶數後，加入集合去重。  

時間複雜度 O(N^3)。  
空間複雜度 O(N^3)。  

```python
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        N = len(digits)
        s = set()
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                for k in range(N):
                    if i == k or j == k:
                        continue
                    val = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if val >= 100 and val % 2 == 0:
                        s.add(val)

        return len(s)
```
