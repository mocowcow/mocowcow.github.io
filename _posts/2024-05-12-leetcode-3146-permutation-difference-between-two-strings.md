---
layout      : single
title       : LeetCode 3146. Permutation Difference between Two Strings
tags        : LeetCode Easy String HashTable Simulation
---
周賽 397。

## 題目

輸入兩個字串 s, t。每個字元在 s 中最多出現一次，且 t 是 s 的**排列**。  

**排列差**指的是所有字元分別在 s 和 t **出現的索引位置**絕對差的加總。  

求 s 和 t 的排列差。  

## 解法

s 中每個字元 c 只會出現一次，也保證只會在 t 出現一次。  
先遍歷 s 並記錄各字元 c 的索引位置，然後再遍歷 t，將兩個索引差加入答案。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        d = {c:i for i, c in enumerate(s)}
        ans = 0 
        for i, c in enumerate(t):
            ans += abs(i - d[c])
            
        return ans
```
