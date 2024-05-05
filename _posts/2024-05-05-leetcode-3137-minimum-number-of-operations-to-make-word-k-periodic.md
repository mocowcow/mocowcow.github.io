---
layout      : single
title       : LeetCode 3137. Minimum Number of Operations to Make Word K-Periodic
tags        : LeetCode Medium String HashTable Greedy
---
周賽 396。反而比 Q1 簡單。  

## 題目

輸入長度 n 的字串 word，還有整數 k。保證 k 可以整除 n。  

每次操作，你可以選擇兩個可被 k 整除的索引 i, j，然後把子字串 word[i..(i+k-1)] 替換成 word[j..(j+k-1)]。  

求最少需要幾次才能使得 word 滿足 **k 週期**。  

**k 週期**指的是一個由長度 k 的字串 s 重複數次而成的字串。  
例如：s = "ab" 的 **2 週期**字串是 "ababab"。  

## 解法

講得很囉唆，其實就是把 k 個字元當成一組，每次可以改變一組的值。最少幾次才能使全部相等。  
當然是找到出現最多次的子字串 sub，然後把其餘的都變成 sub。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        N = len(word)
        d = Counter()
        for i in range(0, N, k):
            sub = word[i:i + k]
            d[sub] += 1
            
        return (N // k) - max(d.values())
```
