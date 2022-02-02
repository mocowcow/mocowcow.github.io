---
layout      : single
title       : LeetCode 438. Find All Anagrams in a String
tags 		: LeetCode Medium HashTable SlidingWindow
---
Anagram中文到底是什麼？重組字詞、易位構詞、變位字…。腦中冒出八分相似的化學術語：同分異構。

# 題目
輸入兩個字串s及p，找出s之中所有p的anagram，並以起始index紀錄。  
>s = "cbaebabacd", p = "abc"  
ans = [0,6]
index 0 = "cba"  
index 6 = "bac"

# 解法
開頭直接檢查s長度是否大於p，否則回傳空陣列。  
滑動視窗的概念就是右進左出，依情況不同，從右方加入新的元素，或從左方扣除舊的元素。這題要找的anagram長度是固定的，所以視窗大小也固定，每次移動都是左右各+1。  
小寫字母"z"的ascii碼是122，我選用陣列計數。首先把p及s的前段初始化，之後將視窗慢慢向右移動，途中檢查並紀錄anagram位置。

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        M = len(s)
        N = len(p)
        if M < N:
            return []
        pattern = [0]*123
        window = [0]*123

        # init pattern
        for c in p:
            pattern[ord(c)] += 1

        # init window
        idx = 0
        for _ in range(N):
            window[ord(s[idx])] += 1
            idx += 1

        ans = []
        if window == pattern:
            ans.append(0)

        while idx < M:
            window[ord(s[idx])] += 1
            window[ord(s[idx-N])] -= 1
            idx += 1
            if window == pattern:
                ans.append(idx-N)

        return ans
```
