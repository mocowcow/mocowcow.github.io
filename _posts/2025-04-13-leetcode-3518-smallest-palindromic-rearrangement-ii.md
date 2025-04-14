---
layout      : single
title       : LeetCode 3518. Smallest Palindromic Rearrangement II
tags        : LeetCode Hard Math
---
weekly contest 445。  
以前總是抱怨 python 卡常數打比賽沒優勢，原來其實在暴力排列組合有巨大優勢，只是我不敢用。  
本周兩場真的在大數上吃了不少甜頭。  

## 題目

<https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/>

## 解法

和前一題一樣，回文串只需要處理其中一半。  
問題簡化成左半邊字串 half 第 k 小的**不同的**排列。  

相似題 [3470. permutations iv]({% post_url 2025-03-12-leetcode-3470-permutations-iv %})。  

---

設 half 長度為 sz，則全排列有 sz! 種。  
但題目要求的是**不同的**排列，所以對於每種元素都要去重。  
若對於 c 總共出現 v 次，則要除以 v! 種重複排列。  

若去重後的總排列數 tot 不足 k，沒有答案，直接回傳空字串。  

---

接著從小到到枚舉要填的元素。  
設當前填第 i 位，剩餘排列數有 rem_ways 種。  
如果填了字元 c，則分子會少乘一個 (sz-i)，分母會多乘一個 cnt[c]。  
代表由 c 開頭的共有 ways = rem_ways \* cnt[c] / (sz-i) 種排列。  

如果 k <= ways，則代表第 k 小的選法包含在這組內。答案填入 c，更新 c 的剩餘數量與剩餘排列數。  
否則 k > ways 代表 k 不屬於這組。直接從 k 中排除掉 ways 個更小的排法。  

最後填完把左半邊翻轉，並加上中心元素即可。  

```python
f = cache(factorial)

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        N = len(s)
        half = s[:N//2]
        mid = "" if N % 2 == 0 else s[N//2]
        sz = len(half)

        tot = f(sz)
        cnt = Counter(half)
        for v in cnt.values():
            tot //= f(v)

        # 排列數不足
        if tot < k:
            return ""

        rem_ways = tot
        ans = []
        for i in range(sz):
            for c in ascii_lowercase:
                if cnt[c] == 0:
                    continue
                ways = rem_ways*cnt[c]//(sz-i)
                if k <= ways:
                    ans.append(c)
                    rem_ways = ways
                    cnt[c] -= 1
                    break
                k -= ways

        pre = "".join(ans)

        return pre + mid + pre[::-1]
```
