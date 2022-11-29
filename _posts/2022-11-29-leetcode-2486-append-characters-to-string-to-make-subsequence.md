--- 
layout      : single
title       : LeetCode 2486. Append Characters to String to Make Subsequence
tags        : LeetCode Medium Array String TwoPointers
---
周賽321。

# 題目
輸入只由小寫字母組成的字串s和t。  

求**最少**需要在s最尾端附加幾個字元，才能使得t成為s的子序列。  

# 解法
其實就是在原本的s中找子序列t，看最多能匹配到幾個字元。t長度為M，假若成功配到j個字元，則剩下M-j個字串需要附加。  

遍歷長度N的字串s，時間為O(N)，空間O(1)。  

```python
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        M=len(t)
        j=0
        
        for c in s:
            if j==M:return 0
            if c==t[j]:j+=1
        
        return M-j
```
