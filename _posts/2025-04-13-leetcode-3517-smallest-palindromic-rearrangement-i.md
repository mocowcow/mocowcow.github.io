---
layout      : single
title       : LeetCode 3517. Smallest Palindromic Rearrangement I
tags        : LeetCode Medium Greedy Sorting
---
weekly contest 445。

## 題目

<https://leetcode.com/problems/smallest-palindromic-rearrangement-i/description/>

## 解法

回文串兩邊是對稱的，只要處理中心和其中一半就好。  

對於左半邊來說，若想要字典序最小，直接排序一下就行。  
最後把中心還有反轉後的半邊加回去。  

時間複雜度 O(N log N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        N = len(s)

        if N % 2 == 1:
            mid = s[N//2]
        else:
            mid = ""

        pre = s[:N//2]
        pre = "".join(sorted(pre))

        return pre + mid + pre[::-1]
```
