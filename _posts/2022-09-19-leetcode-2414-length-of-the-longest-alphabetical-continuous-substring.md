--- 
layout      : single
title       : LeetCode 2414. Length of the Longest Alphabetical Continuous Substring
tags        : LeetCode Medium String Greedy
---
周賽311。這次的Q2也是簡單，有提交答案的人幾乎全部都通過了。  

# 題目
**連續字母字串**是由字母表中的連續字母組成的字串。換句話說，它是字串"abcdefghijklmnopqrstuvwxyz"的任何子字串。  
例如"abc"是連續字母字串，而"acb"和"za"則不是。  

輸入僅由小寫字母組成的字串s，求**最長連續字母字串**長度。

# 解法
只要每個字元c都接在ascii碼前一位的字元後面，那他就是連續的。  
遍歷s中每一個字元c，和前一個字元prev比較ascii值，如果正好是下一位則使字串長度遞增1，否則重置連續字串。  

時間複雜度為O(N)，空間複雜度為O(1)。  

```python
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        prev=inf
        cnt=0
        ans=1
        
        for c in s:
            curr=ord(c)-97
            if curr==prev+1:
                cnt+=1
                ans=max(ans,cnt)
            else:
                cnt=1
            prev=curr
 
        return ans
```
