---
layout      : single
title       : LeetCode 3333. Find the Original Typed String II
tags        : LeetCode Hard Math DP PrefixSum
---
biweekly contest 142。  

## 題目

Alice 想在電腦上輸入某個字串。  
但他有時候會手殘，按著按鍵太久，讓一個字元輸入好幾次。  

輸入字串 word，代表 Alice 螢幕上顯示的**最終結果**。另外還有整數 k，表示 Alice 原本想輸入的字串長度**至少**為 k。  

求 Alice 一開始原本想輸入的字串有幾種可能。  
答案可能很大，先模 10^9 + 7 後回傳。  

## 解法

與 Q1 差別在於，現在**不限失誤次數**。  
word 分組後，每組長度分別為 cnt，則有不失誤 + (cnt-1) 種失誤方案，共 cnt 種方案。  
不考慮 k 的情況下，根據**乘法原理**把 M 個組長度相乘，就是所有的原始字串方案數。  

---

但是本題還限制原始字串長度**至少** k。  

最壞情況下，原字串每個相鄰字元都不同，最高達 M = 5e5 組。  
若想直接找到長度至少 k=1 的方案，那麼合法的長度範圍必須求出長度範圍為 [1,5e5]。  

為找出合法長度 j 的方案，很直覺想到枚舉每個組別所貢獻的長度。  
我們只在乎長度，而不在乎字元本身，不同選法都能湊出相同長度，有**重疊的子問題**，因此考慮 dp。  
但光是狀態數就有 M^2 個，一看就知道會超時，得想想其他方法。  

---

注意到 k 至多 2000，**正難則反**，可以改求出**不足 k 的**非法方案數，再從總方案數中扣掉。  
並且，每一組至少都要貢獻一個字元，若組數 M 大於 k-1，則不可能有任何非法方案。  
因此狀態數至多 k^2 = 4e6 個。  

定義 dp(i, j)：在剩餘的 groups[i..] 組中，長度為 j 的原始字串方案數。  
轉移：dp(i, j) = sum(dp(i+1, j-use) for 1 <= use <= min(groups[i], j))。  
base：  

- 當 i = M 時，沒有剩餘組別，且 j = 0 代表空字串，只有 1 種方案。  
- 否則只有 i = M 或是 j = 0 之一成立，則不合法，回傳 0。  

時間複雜度 O(N + k^3)。  
空間複雜度 O(k^2)。  

雖然狀態數 K^2 合理，但每個狀態需要轉移 k 次，還是會超時。  

```python
MOD = 10**9 + 7
class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        ans = 1
        groups = []
        for _, g in groupby(word):
            cnt = len(list(g))
            groups.append(cnt)
            ans = (ans * cnt) % MOD

        @cache
        def dp(i, j):  # groups[i..] for length j
            if i == M and j == 0:
                return 1
            if i == M or j == 0:
                return 0
            res = 0
            for use in range(1, min(j, groups[i]) + 1):
                res += dp(i + 1, j - use)
            return res

        M = len(groups)
        if k - 1 < M:
            return ans

        for j in range(k):
            ans -= dp(0, j)

        return ans % MOD
```

列出轉移過程，會發現轉移來源有部分重疊。  

dp(i, j-1) 的來源有：  
> dp(i+1, (j-1)-1)  
> dp(i+1, (j-1)-2)  
> ..  
> dp(i+1, (j-1)-(j-1))  

dp(i, j) 的來源有：  
> dp(i+1, j-1)  
> dp(i+1, j-2)  
> ..  
> dp(i+1, j-j)  

發現 dp(i, j) 比起 dp(i, j-1) 多了一個 dp(i+1, j-1) 而已。  
當 j 每次增加 1 時，轉移來源也增加一個。可以用**前綴和**優化。  

---

但要注意注意，當 j 超過 limit = groups[i] 時，反而會失去轉移來源。例如：  
limit = 3, j = 3 的來源：  
> dp(i+1, 3-1)  
> dp(i+1, 3-2)  
> dp(i+1, 3-3)  

limit = 3, j = 4 的來源：  
> dp(i+1, 4-1)  
> dp(i+1, 4-2)  
> dp(i+1, 4-3)  

雖然多出一個來源 dp(i+1, 3)，但也因為可用長度不足，而少一個 dp(i+1, 0)。  
因此在 j > limit 時要記得扣除 dp(i+1, j-1-limit)。  

---

優化過後每個狀態轉移只需要 O(1)，快了很多。  
但是 python 記憶化還是容易超時，需要加一堆剪枝才能勉強過。  

時間複雜度 O(N + k^2)。  
空間複雜度 O(k^2)。  

```python
MOD = 10**9 + 7
class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        ans = 1
        groups = []
        for _, g in groupby(word):
            cnt = len(list(g))
            groups.append(cnt)
            ans = (ans * cnt) % MOD

        @cache
        def dp(i, j):  # groups[i..] for length j
            if M-i > j: # pruning, prevent TLE
                return 0
            if i == M and j == 0:
                return 1
            if i == M or j == 0:
                return 0
            res = ps(i + 1, j - 1)
            if j > groups[i]:
                res -= ps(i + 1, j - 1 - groups[i])
            return res % MOD

        @cache
        def ps(i, j):
            if M-i > j: # pruning, prevent TLE
                return 0
            if i == M:
                return 1
            if j == 0:
                return 0
            res = ps(i, j - 1) + dp(i, j)
            return res % MOD

        M = len(groups)
        if k - 1 < M:
            return ans

        for j in range(k):
            ans -= dp(0, j)
        dp.cache_clear() # prevent MLE
        ps.cache_clear() # prevent MLE

        return ans % MOD
```

上面記憶化跑了 8000ms，改成遞推之後只需要 3000ms。  

```python
MOD = 10**9 + 7
class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        ans = 1
        groups = []
        for _, g in groupby(word):
            cnt = len(list(g))
            groups.append(cnt)
            ans = (ans * cnt) % MOD

        M = len(groups)
        if k - 1 < M:
            return ans

        f = [[0]*k for _ in range(M+1)]
        f[M][0] = 1

        for i in reversed(range(M)):
            limit = groups[i]
            ps = 0
            for j in range(1, k):
                ps += f[i+1][j-1]
                if j > limit:
                    ps -= f[i+1][j-1-limit]
                f[i][j] = ps % MOD

        for j in range(k):
            ans -= f[0][j]

        return ans % MOD
```
