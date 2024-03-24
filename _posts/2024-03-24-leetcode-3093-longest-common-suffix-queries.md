---
layout      : single
title       : LeetCode 3093. Longest Common Suffix Queries
tags        : LeetCode Hard Array String Trie Sorting
---
周賽 390。

## 題目

輸入兩個字串陣列 wordsContainer 和 wordsQuery。  

對於每個 wordsQuery[i]，你需要從 wordsContainer 裡面找到一個與 wordsQuery[i] 擁有**最長公共後綴**的字串。  
如果有多個字串滿足最長公共後綴，則選擇長度較短者。  
如果長度還是相同，那就選擇最先在 wordsContainer 出現者。  

回傳整數陣列 ans，其中 ans[i] 代表 wordsQuery[i] 對應的**最長公共後綴**位於 wordsContainer 的索引。  

## 解法

看到在一堆字串裡面找前/後綴，八成就是**字典樹**。  
難點在於：怎麼在擁有共通後綴的一堆字串中找到滿足要求的？  

如果在每個節點都記上擁有相同後綴的字串索引，如果 wordsContainer 所有字串都相同，那麼一個節點可以塞滿 N 個字串。  
每次查詢都需要排序的 O(N log N)，肯定會超時。  

---

與其每次查詢都重新排序，不如**一開始就排序**，按照題目要求的順序去建字典樹。  
先把 wordsContainer 的所有索引依長度、索引大小排序。  

按照排序好的索引建立字典樹。  
節點只有在第一次被訪問的時候紀錄對應的字串索引，正好就是該後綴的最佳選擇。  
注意：空字串會對應到最短、且索引最小的字串，也就是排序後的第一個字串的索引。  

時間複雜度 O(N log N + L1 + L2)，其中 L1 = sum(len(wordsContainer))，L2 = sum(len(wordsQuery))。  
空間複雜度 O(L1)。  

```python
class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        N = len(wordsContainer)
        indexes = sorted(range(N), key=lambda x: [len(wordsContainer[x]), x])
        root = TrieNode()
        root.id = indexes[0]
        
        # add all words
        for i in indexes:
            curr = root
            w = wordsContainer[i]
            for c in reversed(w):
                curr = curr.child[c]
                if curr.id == -1:
                    curr.id = i
        
        ans = []
        for w in wordsQuery:
            curr = root
            for c in reversed(w):
                if c not in curr.child:
                    break
                curr = curr.child[c]
            ans.append(curr.id)
        
        return ans
    

class TrieNode:
    def __init__(self) -> None:
        self.child = defaultdict(TrieNode)
        self.id = -1
```
