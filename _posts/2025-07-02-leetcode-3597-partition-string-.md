---
layout      : single
title       : LeetCode 3597. Partition String 
tags        : LeetCode Medium Simulation Trie
---
weekly contest 456。  
本想說 Q1 就出字典樹有點刺激，原來是複雜度妙妙屋。  

## 題目

<https://leetcode.com/problems/partition-string/description/>

## 解法

按照題意模擬，子字串會不斷查找、增長。  
每次查找、增長的複雜度都是 O(N)，直覺需要更快的查找方式。  
過改用字典樹維護出現過的字串，則每次加入新的字元只需要 O(1)。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python

class Solution:
    def partitionString(self, s: str) -> List[str]:
        ans = []
        root = TrieNode()
        j = 0
        curr = root
        for i, c in enumerate(s):
            curr = curr.child[c]
            if not curr.vis:
                ans.append(s[j:i+1])
                curr.vis = True
                curr = root
                j = i + 1

        return ans


class TrieNode:
    def __init__(self) -> None:
        self.child = defaultdict(TrieNode)
        self.cnt = 0
        self.vis = False
```

仔細分析出現的子字串長度，長度為 1,2,3,4,...,x，其總和不超過 N。  
以等差數列和公式計算：  
> x \* (x+1) <= N  

x 約等於 sqrt(N)。  
直接用雜湊表暴力維護字串其實也是可以過的。  

時間複雜度 O(N \* sqrt(N))。  
空間複雜度 O(N)。  

```python
class Solution:
    def partitionString(self, s: str) -> List[str]:
        ans = []
        vis = set()
        sub = ""
        for i, c in enumerate(s):
            sub += c
            if not vis:
                ans.append(sub)
                vis.add(sub)
                sub = ""

        return ans
```
