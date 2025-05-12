---
layout      : single
title       : LeetCode 3541. Find Most Frequent Vowel and Consonant
tags        : LeetCode Easy Simulation
---
biweekly contest 156。

## 題目

<https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/description/>

## 解法

按照題意模擬。  
統計各字元出現次數，依母音、子音更新最大值。  

時間複雜度 O(N + D)，其中 D = 不同字元個數。  
空間複雜度 O(D)。  

```python
class Solution:
    def maxFreqSum(self, s: str) -> int:
        d = Counter(s)
        vow = con = 0
        for k, v in d.items():
            if k in "aeiou":
                vow = max(vow, v)
            else:
                con = max(con, v)

        return vow + con
```
