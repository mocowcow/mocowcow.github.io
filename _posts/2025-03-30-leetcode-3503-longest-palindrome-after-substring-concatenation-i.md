---
layout      : single
title       : LeetCode 3503. Longest Palindrome After Substring Concatenation I
tags        : LeetCode Medium
---
weekly contest 443。

## 題目

<https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-i/description/>

## 解法

本題字串長度至多 30，暴力枚舉還算能過。  

先枚舉 s 的所有子字串，再枚舉 t 的所有子字串，兩個拼起來後檢查是否回文，更新答案。  
注意：子字串可以為空，別忘記枚舉空字串。  

時間複雜度 O(M^2 \* N^2 \* (M + N))。  
空間複雜度 O(M + N)。  

```python
class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        M, N = len(s), len(t)
        ans = 1
        for i in range(M):
            for j in range(i-1, M): # s[i:i-1+1] = ""
                sub1 = s[i:j+1]
                for k in range(N):
                    for l in range(k-1, N): # s[k:k-1+1] = ""
                        sub2 = t[k:l+1]
                        merge = sub1 + sub2
                        if merge == merge[::-1]:
                            ans = max(ans, len(merge))

        return ans
```

也可以單獨處理 t 和 s 的回文子字串。  
有點冗長就是。  

```python
class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        M, N = len(s), len(t)

        ans = 1
        # palindromic substring of s
        for i in range(M):
            for j in range(i, M):
                sub = s[i:j+1]
                if sub == sub[::-1]:
                    ans = max(ans, len(sub))

        # palindromic substring of t
        for i in range(N):
            for j in range(i, N):
                sub = t[i:j+1]
                if sub == sub[::-1]:
                    ans = max(ans, len(sub))

        # palindromic substring of s[i..j] + t[k..l]
        for i in range(M):
            for j in range(i, M):
                sub1 = s[i:j+1]
                for k in range(N):
                    for l in range(k, N):
                        sub2 = t[k:l+1]
                        merge = sub1 + sub2
                        if merge == merge[::-1]:
                            ans = max(ans, len(merge))

        return ans
```
