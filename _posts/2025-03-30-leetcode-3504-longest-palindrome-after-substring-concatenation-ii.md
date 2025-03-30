---
layout      : single
title       : LeetCode 3504. Longest Palindrome After Substring Concatenation II
tags        : LeetCode Hard DP
---
weekly contest 443。

## 題目

<https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-ii/description/>

## 解法

本題字串長度至多 1000，暴力法超時，需要優化。  

先優化 s, t 單獨求回文。  
本來暴力法是 O(N^3)，有很多方法可以優化成 O(N^2)。  
相似題 [5. longest palindromic substring]({% post_url 2022-03-14-leetcode-5-longest-palindromic-substring %})。  

---

再來考慮 s, t 如何一起求回文。  
定義 dp(i, j)：子字串 s[i..] + t[..j] 的最長回文長度。  

原本判斷 s[i..j] 是否回文時，要先確保 s[i] = s[j]，然後檢查 s[i+1..j-1] 是否回文。  
有重疊的子問題，可以 dp。  

那麼我們判斷 s[i..] + t[..j] 是否回文，同樣也是先檢查最靠外的兩個字元是否相等。  
先確保 s[i] == t[j]，然後才檢查 s[i+1..] + t[..j-1]。  

---

但終止情況略有不同。  
原本判斷單個字串時，若 s[i] != s[j] 則 s[i..j] 不可能回文，直接終止，長度為 0。  

而對於 s[i..] + t[..j] 來說，即使 s[i] != t[j]，也可以直接停止，保留部分子陣列。例如：  
> s = "caabb", t = "cccaac"  
> 配到 s[3] != t[2] 終止  
> 保留 "caa" + "aac"  

甚至可以從剩餘的 s 或 t 再取出一部分的回文前綴 (或後綴)。例如：  
> s = "ababc", t = "ca"  
> 求 s[0..] + t[..1] 的最長回文  
> s[0] = t[1]，繼續匹配  
> s[1] != t[0]，終止匹配，改從 s, t 其中一邊取出回文  
> s[1..] = "babc"，最長回文前綴 = "bab"  
> t[..0] = "c"，最長回文後綴 = "c"  
> 答案即 "a" + "bab" + "a"  

複雜度 O(MN)。  

---

每次都檢查前後綴回文也很耗時，所以還要 dp 一次。  
重複利用先前的單字串回文求出最長前後綴。定義：

- pre_s(i)：以 i 開頭的子字串 s[i..] 中的最長回文長度。  
- suf_t(j)：以 j 結尾的子字串 t[..j] 中的最長回文長度。  

複雜度 O(M^2 + N^2)。  

---

最後枚舉 i, j 以 dp(i, j) 更新答案最大值即可。  

時間複雜度 O(M^2 + N^2 + MN) 。  
空間複雜度 O(M^2 + N^2 + MN)。  

```python
class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        M, N = len(s), len(t)

        @cache
        def pal(s, i, j):
            if i > j:
                return 0
            if i == j:
                return 1
            if s[i] != s[j]:
                return -inf
            return 2 + pal(s, i+1, j-1)

        @cache
        def pre_s(i):  # longest palindrome of s[i..]
            res = 0
            for j in range(i, M):
                res = max(res, pal(s, i, j))
            return res

        @cache
        def suf_t(j):  # longest palindrome of t[..j]
            res = 0
            for i in range(j+1):
                res = max(res, pal(t, i, j))
            return res

        @cache
        def dp(i, j):  # longest palindrome of s[i..] + t[..j]
            if i == M:
                return suf_t(j)
            if j < 0:
                return pre_s(i)
            if s[i] != t[j]:
                return max(suf_t(j), pre_s(i))
            return 2 + dp(i+1, j-1)

        ans = 1
        for i in range(M):
            for j in range(N):
                ans = max(ans, dp(i, j))

        # prevent MLE
        pal.cache_clear()
        dp.cache_clear()
        pre_s.cache_clear()
        suf_t.cache_clear()

        return ans
```
