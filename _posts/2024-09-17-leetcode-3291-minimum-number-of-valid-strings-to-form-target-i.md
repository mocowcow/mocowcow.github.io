---
layout      : single
title       : LeetCode 3291. Minimum Number of Valid Strings to Form Target I
tags        : LeetCode Medium String DP Trie HashTable Greedy
---
weekly contest 415。  
這題測資範圍 N = 5000 也很神祕，猜猜看 O(N^2) 能不能過？  

## 題目

輸入字串陣列 words，還有一個字串 target。  

若字串 x 是 words 中任意字串的**前綴**，則稱為**有效的**。  

求**最少**需要幾個**有效的字串**才能連接出 target。若不可能則回傳 -1。  

## 解法

前陣子才出過差不多的題。  
相似題 [3213. construct string with minimum cost]({% post_url 2024-07-10-leetcode-3213-construct-string-with-minimum-cost %})。  

能選的從整個 words[i] 變成 words[i] 的前綴，然後成本都固定 1。  
字典樹方法稍微調整一下就可以過了。  

時間複雜度 O(N^2 + L)，其中 L = sum(words[i].length)。  
空間複雜度 O(N + L)。  

跑了 16000ms，有夠驚悚的時間，勉強過關。  

```python
class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        N = len(target)
        trie = Trie()
        for w in words:
            trie.add(w)

        @cache
        def dp(i):
            if i == N:
                return 0
            res = inf
            curr = trie.root
            for j in range(i, N):
                c = target[j]
                if c not in curr.child:
                    break
                curr = curr.child[c]
                res = min(res, dp(j + 1) + 1)
            return res 

        ans = dp(0)
        if ans == inf:
            return -1
        
        return ans


class TrieNode:
    def __init__(self) -> None:
        self.child = defaultdict(TrieNode)
        self.val = inf


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, s) -> None:
        curr = self.root
        for c in s:
            curr = curr.child[c]
```

到 Q4 的時候 N = 5e4，字典樹就超時了，得換個方法。  
相似題原本也有 rolling hash 解法，我就在想這題應該也能用，但沒想出來。  

事實上的確能行，而且是 [45. Jump Game II](https://leetcode.com/problems/jump-game-ii) 的加強版。  
把 target 當作跳躍遊戲，最初從 target[0] 出發，看能不能跳到 target[N]。  

那麼如何求 target[i] 能夠跳多遠？  
若 target[i..j] 是某個 word 的**前綴**，則從 i 可以跳到 j+1。  
但是前綴最多也可以達到 N 個，枚舉肯定不行。  

根據**前綴的特性**，若 target[i..j] 是前綴，那麼更短的 target[i..j-1] 同樣也是前綴。  
定義 f(j)：判斷 target[i..j] 是否為前綴，則此函數具有**單調性**，可以**二分答案**。  
對於每個出發點 target[i]，找到滿足 target[i..j] 為前綴的最大的 j，並更新最大跳躍位置為 j+1。  

---

按照跳躍遊戲的方式選擇**使下次跳更遠的點**即可。  
注意：若無法跳更遠則直接回傳 -1。  
時間複雜度 O(L + N log N)，其中 L = sum(words[i].length)。  
空間複雜度 O(L + N)。  

```python
MOD1 = 1000000901
MOD2 = 1000015279
class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        N = len(target)

        # get all prefix hash
        hashes = set()
        for w in words:
            dh = DoubleHash(w, MOD1, MOD2)
            for r in range(len(w)):
                h = dh.get(0, r)
                hashes.add(h)
        
        def find(i):
            lo = i - 1
            hi = N - 1
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if dh.get(i, mid) not in hashes:
                    hi = mid - 1
                else:
                    lo = mid
            return lo

        dh = DoubleHash(target, MOD1, MOD2)
        # jump game II
        ans = 0
        curr_r = 0
        next_r = 0
        for i in range(N):
            # find longest target[i..j] which is prefix
            j = find(i)
            next_r = max(next_r, j + 1)
            if i == curr_r:
                if curr_r == next_r:  # cant jump
                    return -1
                curr_r = next_r
                ans += 1

        return ans


class RollingHash:
    def __init__(self, s, mod):
        self.mod = mod
        base = 8787
        ps = self.ps = [0]
        p = self.p = [1]
        for c in s:
            ps.append((ps[-1] * base + ord(c)) % mod)
            p.append(p[-1] * base % mod)

    def get(self, L, R):
        return (self.ps[R+1] - self.ps[L] * self.p[R-L+1]) % self.mod


class DoubleHash:
    def __init__(self, s, mod1, mod2):
        self.h1 = RollingHash(s, mod1)
        self.h2 = RollingHash(s, mod2)

    def get(self, L, R):
        return (self.h1.get(L, R), self.h2.get(L, R))
```
