---
layout      : single
title       : LeetCode 3291. Minimum Number of Valid Strings to Form Target I
tags        : LeetCode Medium DP Trie
---
weekly contest 415。  
這題測資範圍也很神祕，界於一個不知道會不會過的神奇區域。  

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

跑了 16000ms，有夠驚悚的時間。  

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
