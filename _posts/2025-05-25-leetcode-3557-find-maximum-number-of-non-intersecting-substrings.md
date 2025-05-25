---
layout      : single
title       : LeetCode 3557. Find Maximum Number of Non Intersecting Substrings
tags        : LeetCode Medium DP BinarySearch Greedy
---
biweekly contest 157。

## 題目

<https://leetcode.com/problems/find-maximum-number-of-non-intersecting-substrings/>

## 解法

枚舉 word[i] 是否以 i 為起點劃分子陣列 word[i..j]，決定**選或不選**。  
不選的話跳過 i，繼續處理 i+1；選的話跳到距離 i 最近的位置 j，繼續處理 j+1。  
有**重疊的子問題**，考慮 dp。  

定義 dp(i)：在 word[i..] 可劃分出的最大子陣列個數。  
轉移：  

- 不選，dp(i+1)  
- 選，dp(j+1) + 1  

至於如何找最近的 j？  
先按照字元將索引分組，若當前起點為 i，則二分找第一個大於等於 i+3 的位置即可。  

時間複雜度 O(N log N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def maxSubstrings(self, word: str) -> int:
        N = len(word)

        d = defaultdict(list)
        for i, x in enumerate(word):
            d[x].append(i)

        @cache
        def dp(i):
            if i >= N:
                return 0
            res = dp(i+1)
            a = d[word[i]]
            idx = bisect_left(a, i+3)
            if idx < len(a):
                j = a[idx]
                res = max(res, dp(j+1) + 1)
            return res

        return dp(0)
```
