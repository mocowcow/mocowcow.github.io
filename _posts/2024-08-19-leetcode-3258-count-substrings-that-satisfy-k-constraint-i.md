---
layout      : single
title       : LeetCode 3258. Count Substrings That Satisfy K-Constraint I
tags        : LeetCode Easy String SlidingWindow TwoPointers
---
weekly contest 411。  

## 題目

輸入**二進位**字串 s，以及整數 k。  

若一個二進位字串滿足以下**任一**條件，則稱其 **k 約束**。  

- 字串中最多 k 個 0。  
- 字串中最多 k 個 1。  

求 s 有幾個 **k 約束** 子字串。  

## 解法

暴力枚舉所有子字串，並統計 0,1 個數。  

時間複雜度 O(N^3)。  
空間複雜度 O(N)。  

```python
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        N = len(s)
        ans = 0
        for i in range(N):
            for j in range(i, N):
                sub = s[i:j+1]
                cnt0 = sub.count("0")
                cnt1 = sub.count("1")
                if min(cnt0, cnt1) <= k:
                    ans += 1

        return ans
```
