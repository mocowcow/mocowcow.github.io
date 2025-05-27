---
layout      : single
title       : LeetCode 3563. Lexicographically Smallest String After Adjacent Removals
tags        : LeetCode Hard DP
---
weekly contest 451。  
雖然是承接 Q2，但是難度跨度也太大了，而且還是複雜度妙妙屋。  

## 題目

<https://leetcode.com/problems/lexicographically-smallest-string-after-adjacent-removals/description/>

## 解法

**連續**定義同 Q2，即在字母表中絕對差為 1 或 25 的兩個字母。  

每次操作可從 s 中刪除任意一對**相鄰**且**連續**的字母。  
求任意次操作後可得的**字典序最小**結果。  

---

繼續用括號相消為例，將可刪除的連續字母以括號表示。  
研究怎樣的模式可以被刪除，最後成為空字串：  

- 最單純的相鄰連續，如 ()  
- 多個區間互相包含，如 ([])  
- 多個括號並排，如 ()[]  

若區間 s[i..j] 要能刪除，需要滿足以上任一情況。  

不同的刪除順序可能得到剩餘的子區間，有**重疊的子問題**，考慮 dp。  
定義 can_remove(i, j)：是否可透過操作刪除 s[i..j]。  
若須滿足以下任一情況，則可刪除為空：  

- s[i..j] 相鄰且連續。  
- s[i+1..j-1] 可被刪除，最後使得 s[i] 和 s[j] 變成相鄰且連續。  
- s[i..mid] 可被刪除，另一段 s[mid+1..j] 也可被刪除

---

知道能不能刪之後，再來決定 s 中的字元要不要刪，是**選或不選**的問題。  
不同的刪法也可能得到相同的結果，有重疊的子問題，還是 dp。  

定義 dp(i)：s[i..] 若干次刪除後可得的**最小字典序**字串。  
轉移：  

- 不刪 s[i]，結果為 s[i] + dp(i+1)  
- 刪 s[i]，需要找長度為 2 個區間 s[i..j] 刪除，結果為 f(j+1)  

---

題目求 s[0..] 若干次刪除得到的最小字典序結果。  
答案入口 dp(0)。  

時間複雜度 O(N^3)。  
空間複雜度 O(N^2)。  

```python
def is_consecutive(x, y):
    diff = abs(ord(x) - ord(y))
    return diff == 1 or diff == 25

class Solution:
    def lexicographicallySmallestString(self, s: str) -> str:
        N = len(s)

        @cache
        def can_remove(i, j):
            if i+1 == j:
                return is_consecutive(s[i], s[j])
            if is_consecutive(s[i], s[j]) and can_remove(i+1, j-1):
                return True
            for mid in range(i+1, j, 2):
                if can_remove(i, mid) and can_remove(mid+1, j):
                    return True
            return False

        @cache
        def dp(i):
            if i == N:
                return ""
            # keep s[i]
            res = s[i] + dp(i+1)
            # remove s[i..j]
            for j in range(i+1, N, 2):
                if can_remove(i, j):
                    res = min(res, dp(j+1))
            return res

        return dp(0)
```
