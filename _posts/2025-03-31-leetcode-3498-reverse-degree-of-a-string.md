---
layout      : single
title       : LeetCode 3498. Reverse Degree of a String
tags        : LeetCode Easy Simulation
---
biweekly contest 153。

## 題目

<https://leetcode.com/problems/reverse-degree-of-a-string/description/>

## 解法

[a..z] 原本對應的數字是 [0..25]。  
想要轉換成 [26..1]，很明顯就是把原本的數字 x 改成 26 - x。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i, c in enumerate(s):
            x = ord(c) - 97
            x = 26 - x
            ans += x * (i + 1) 

        return ans
```
