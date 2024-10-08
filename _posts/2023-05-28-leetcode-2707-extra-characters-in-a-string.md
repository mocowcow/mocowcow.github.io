--- 
layout      : single
title       : LeetCode 2707. Extra Characters in a String
tags        : LeetCode Medium String DP Trie
---
雙周賽 105。這題用 python 是真的好寫，不少人被這題卡住。  

## 題目

輸入字串 s，還有各單字的字典 dictionary。  
你必須將 s 分割成數個**不重疊**子字串，且子字串必須在 dictionary 中。s 中可以有某些不屬於任何子字串的**多餘字元**。  

求s以最佳方式拆分後，最少有幾個**多餘字元**。  

## 解法

雖然從s中以任意順序切出子字串，但是如果先切中間，前後段的字串很難處理，不如固定一個方向切。  

對於一個字串s有兩種情況：  

- 前綴剛好是 dictionary 中的某個字 word，將 word 從 s 前方刪掉，繼續匹配  
- 把第一個字元視為**多餘**，刪掉第一個字元，繼續匹配  

不同的匹配方式有可能得到相同的結果，例如：  
> s = "aab", dictionary = ["a", "aa"]  
> 第一種可能：匹配到兩個 "a"，最後剩下 "b" 是多餘的  
> 第二種可能：匹配到 "aa"，最後剩下 "b" 是多餘的  

擁有重疊的子問題，很明顯需要 dp。  

---

定義 dp(s)：字串 s 的最小**多餘字元**數量。  
轉移：min(dp(ns) FOR ALL w + ns = s)，其中 w 為 dictionary 任意單字。  
base：當 s 為空字串時，不需繼續匹配，答案為 0。  

只能由前方依序刪除字元，至多產生 N 個狀態。  
每個狀態需要對 M 個字串配對轉移，每次配對 O(N)。  

時間複雜度 O(N^2 \* M)，其中 N = len(s)，M = len(dictionary)。  
空間複雜度 O(N)。  

```python
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        @cache
        def dp(s):
            if s == "":
                return 0
            res = 1 + dp(s[1:])
            for w in dictionary:
                if s.startswith(w):
                    ns = s[len(w):]
                    res = min(res, dp(ns))
            return res

        return dp(s)
```

用字串當作 dp 狀態有點邪門，搞一個比較普通的寫法。  
為了快速查詢子字串是否合法，需要先將 dictionary 裝入集合中。  

定義 dp(s)：子字串 s[i..N-1] 的最小**多餘字元**數量。  
轉移：min(dp(j)) FOR ALL s[i..j] in dictionary。  
base：當 i=N 時不需繼續匹配，答案為 0。  

時間複雜度 O(N^3 + L)，其中 N = len(s)， L = sum(len(dictionary[i]))。  
空間複雜度 O(N + L)。  

```python
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        N = len(s)
        word_set = set(dictionary)

        @cache
        def dp(i):
            if i == N:
                return 0
            res = 1 + dp(i+1)
            for j in range(i, N):
                if s[i:j+1] in word_set:
                    res = min(res, dp(j+1))
            return res

        return dp(0)
```

每次狀態轉移的時候都需要重新構造子字串，這部分的開銷就佔了 O(N)，其實不小。  
使用字典樹的話可以將每個狀態的轉移複雜度從 O(N^2) 降到 O(N)。  

時間複雜度 O(N^2 + L)，其中 N = len(s)， L = sum(len(dictionary[i]))。  
空間複雜度 O(N + L)。  

```python
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        N = len(s)
        trie = Trie()
        for w in dictionary:
            trie.add(w)

        @cache
        def dp(i):
            if i == N:
                return 0
            res = 1 + dp(i+1)
            curr = trie.root
            for j in range(i, N):
                c = s[j]
                if c not in curr.child:
                    break
                curr = curr.child[c]
                if curr.cnt > 0:
                    res = min(res, dp(j+1))
            return res

        return dp(0)


class TrieNode:
    def __init__(self) -> None:
        self.child = defaultdict(TrieNode)
        self.cnt = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, s) -> None:
        curr = self.root
        for c in s:
            curr = curr.child[c]
        curr.cnt += 1  # count whole string
```
