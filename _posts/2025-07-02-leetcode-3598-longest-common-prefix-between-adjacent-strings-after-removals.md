---
layout      : single
title       : LeetCode 3598. Longest Common Prefix Between Adjacent Strings After Removals
tags        : LeetCode Medium Simulation SortedList
---
weekly contest 456。

## 題目

<https://leetcode.com/problems/longest-common-prefix-between-adjacent-strings-after-removals/description/>

## 解法

按照題意模擬刪除 words[i] 後，剩餘相鄰字串的最長公共前綴 (lcp) 長度。  

分類討論刪除刪除 i 會發生什麼事情：  

- i > 0，會損失 i-1 和 i 的 lcp  
- i < N-1，會損失 i 和 i+1 的 lcp  
- i > 0 且 i < N-1，會得到 i-1 和 i+1 的 lcp  

---

先預處理所有字串 i 和 i+1 的 lcp，記做 adj。  
還有刪除 i 會得到兩旁產生的 lcp，記做 gap。  

以 sorted list 維護現有的 lcp，初始化將所有 adj 加入。  
枚舉刪除的位置 i，按照上述討論結果，先刪除後求答案，然後再還原刪除前的狀態。  

時間複雜度 O(L + N log N)，其中 L = 字串總長度。  
空間複雜度 O(L + N)。  

```python

class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        N = len(words)
        sl = SL()
        sl.add(0)  # 哨兵
        adj = [0] * N
        gap = [0] * N
        for i in range(N-1):
            adj[i] = lcp(words[i], words[i+1])
            sl.add(adj[i])
            if i > 0:
                gap[i] = lcp(words[i-1], words[i+1])

        ans = [0] * N
        for i in range(N):
            # 先刪除
            if i > 0:
                sl.remove(adj[i-1])
            if i < N-1:
                sl.remove(adj[i])
            if i > 0 and i < N-1:
                sl.add(gap[i])

            # 算答案
            ans[i] = sl[-1]

            # 恢復刪除
            if i > 0:
                sl.add(adj[i-1])
            if i < N-1:
                sl.add(adj[i])
            if i > 0 and i < N-1:
                sl.remove(gap[i])

        return ans


def lcp(s, t):
    res = 0
    for c1, c2 in zip(s, t):
        if c1 != c2:
            break
        res += 1
    return res
```
