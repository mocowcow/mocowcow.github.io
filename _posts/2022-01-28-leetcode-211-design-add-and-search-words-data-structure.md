---
layout      : single
title       : LeetCode 211. Design Add and Search Words Data Structure
tags 		: LeetCode Medium Design Trie DFS
---
選擇每日題的人很喜歡字典樹啊，連續兩天出現。

# 題目
設計一個資料結構，可以新增單字或查詢是否存在。
實作類別WordDictionary，包含以下功能：
1. 建構子
2. void addWord(word)，將word加入字典
3. bool search(word)，查詢是否存在word，且可用"."代表萬用字元

# 解法
比普通的字典樹多支援萬用字元搜尋，但只需回傳布林值，處理起來不難。  
在search方法裡面，如果碰到"."則對每個子節點做DFS，任一匹配成功則回傳True。

```python
class TrieNode:
    def __init__(self) -> None:
        self.children = defaultdict(TrieNode)
        self.isWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            curr = curr.children[c]
        curr.isWord = True

    def search(self, word: str, curr=None) -> bool:
        if not curr:
            curr = self.root
        for i, c in enumerate(word):
            if c == '.':
                sub = word[i+1:]
                for v in curr.children.values():
                    if self.search(sub, v):
                        return True
                return False
            else:
                if c not in curr.children:
                    return False
                curr = curr.children[c]

        return curr.isWord
```
