---
layout      : single
title       : LeetCode 567. Permutation in String
tags 		: LeetCode Medium SlidingWindow TwoPointers String HashTable
---
[相似題目Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)。

# 題目
輸入兩個字串s1,s2，查看s2是否存有s1的任何排列(就是anagram)。若有則回傳true，否則false。

# 解法
先檢查兩字串長度，s2若小於s1直接false。  
使用雜湊表做sliding window，如果s2一個範圍內各字元出現次數與s1相同，就回傳true。

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        M, N = len(s1), len(s2)
        if M > N:
            return

        target = [0]*123
        window = [0]*123
        for c in s1:
            target[ord(c)] += 1

        for i in range(M):
            window[ord(s2[i])] += 1
            
        if target == window:
            return True

        for i in range(M, N):
            window[ord(s2[i-M])] -= 1
            window[ord(s2[i])] += 1
            if target == window:
                return True

        return False
``` 
