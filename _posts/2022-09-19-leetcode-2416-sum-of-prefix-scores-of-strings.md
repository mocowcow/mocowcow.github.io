--- 
layout      : single
title       : LeetCode 2416. Sum of Prefix Scores of Strings
tags        : LeetCode Hard Array String Trie DFS
---
周賽311。打破個人最速通關紀錄，27分半解決。仔細想想，好像每次碰到字典樹題我都有做出來，真是我的好夥伴。  

# 題目
輸入長度n，且由非空字串組成的陣列words。  

定義字串word的**分數**等於以word作為前綴的的words[i]數量。  
例如words = ["a", "ab", "abc", "cab"]，那麼"ab"的分數是2，因為"ab"是"ab"和"abc"的前綴。  

回傳長度N的陣列answer，其中answer[i]是words[i]的每個非空前綴的**分數總和**。  
注意，字串可被視為自身的前綴。  

# 解法
這題目描述有點爛，我直接看範例才搞懂意思。  
簡單來說就是一個words[i]可以產生x個前綴，然後這些前綴分別是幾個words[i]的前綴，最後加總起來。  

範例2舉的非常好，字串"abcd"總共可以產生四個前綴"abcd", "abc", "ab", "a"。  
而這四個前綴都是"abcd"的前綴，所以分數為4。  

我們可以遍歷words中所有word，列舉word的所有前綴，並透過字典樹來紀錄各前綴的出現次數。  
然後再遍歷一次words，再重新列舉所有前綴，將前綴的出現次數加總，得到總分數。  

時空複雜度皆為O(N*\M)，其中N為words長度，上限1000。M為words[i]長度，上限也是1000。

```python
class Node:
    def __init__(self):
        self.child=defaultdict(Node)
        self.cnt=0

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root=Node()
        ans=[]
        
        for w in words:
            curr=root
            for c in w:
                curr=curr.child[c]
                curr.cnt+=1
        
        for w in words:
            curr=root
            total=0
            for c in w:
                curr=curr.child[c]
                total+=curr.cnt
            ans.append(total)
            
        return ans
```
