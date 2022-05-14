---
layout      : single
title       : LeetCode 2002. Maximum Product of the Length of Two Palindromic Subsequences
tags 		: LeetCode Medium String DP Backtracking BitManipulation Bitmask
---
好久以前某次周賽TLE沒過的，今天又TLE好幾次才過。

# 題目
輸入字串s，找s的兩個**不相交**的**回文子序列**，長度分別為M和N，求M*N最大值為多少。  
且2<=s長度<=12。  
例：  
> s = "leetcodecom"  
> s1 = "ete", s2 = "cdc"  
> len(s1) * len(s2) = 9  

# 解法
當時看到長度最大12，心想就是回溯法。  
bt(i,sub1,sub2)表示處理s[i]字元，sub1和sub2是現有的子序列，每次可以選擇將s[i]加入sub1或sub2，或是丟掉不用。當i=N時更新答案。  
結果最多只通過212/226測資，好慘。  

今天把子序列改成字串，對bt函數做快取才勉強AC。翻了翻討論區也沒看到人python用只用回溯AC的，不確定問題出在哪。

```python
class Solution:
    def maxProduct(self, s: str) -> int:

        def isPalindromic(s):
            l = 0
            r = len(s)-1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        ans = 0
        N = len(s)

        @lru_cache(None)
        def bt(i, sub1, sub2):
            nonlocal ans
            if i >= N:
                if isPalindromic(sub1) and isPalindromic(sub2):
                    ans = max(ans, len(sub1)*len(sub2))
            else:
                # try s[i] to sub1
                bt(i+1, sub1+s[i], sub2)
                # try s[i] to sub2
                bt(i+1, sub1, sub2+s[i])
                # ignore s[i]
                bt(i+1, sub1, sub2)

        bt(0, '', '')

        return ans

```

改用bit mask方法，順便把回文檢查方式改用內建函數，速度快了不少。試了好幾次才發現關鍵加速點是回文檢查函數，太苦了。  
先把所有回文子序列找出來，以對應的mask儲存長度，放到雜湊表pa裡。之後再找任意兩個mask配對，如果做and運算為0，代表沒有重複到，以pa[s1]*pa[s2]更新答案。

```python
class Solution:
    def maxProduct(self, s: str) -> int:
        # build palindromic
        pa = {}
        N = len(s)
        for mask in range(1, 1 << N):
            # build subsequence
            sub = ''
            for i in range(N):
                if mask & (1 << i):
                    sub += s[i]
            if sub == sub[::-1]:
                pa[mask] = len(sub)

        # check disjoint
        ans = 0
        for s1 in pa:
            for s2 in pa:
                if s1 & s2 == 0:
                    ans = max(ans, pa[s1]*pa[s2])

        return ans
            
```            