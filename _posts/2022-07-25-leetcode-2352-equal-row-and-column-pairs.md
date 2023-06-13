--- 
layout      : single
title       : LeetCode 2352. Equal Row and Column Pairs
tags        : LeetCode Medium Array Matrix HashTable Simulation Trie
---
周賽303。python的comprehension在這題節省了不少時間，加上tuple可以雜湊，寫起來是真的快。  

# 題目
輸入n*n的整數矩陣grid，回傳有多少(i, j)數對，其中第i行和第j列相等。  
只要行和列出現的元素及順序相同，則認為它們是相等的。  

# 解法
同一個列可以和多個行組成數對，先將每一列轉成tuple後放入雜湊表d中計數。之後遍歷每一行，在雜湊表中找到相同結構的列有多少，並加入答案中。  

時間複雜度O(N^2)。  
空間複雜度O(N^2)。  

```python
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        N=len(grid)
        d=defaultdict(int)
        ans=0
        
        for row in grid:
            t=tuple(row)
            d[t]+=1
            
        for c in range(N):
            col=[grid[r][c] for r in range(M)]
            t=tuple(col)
            ans+=d[t]
            
        return ans
```

也可以用字典樹來處理比對的過程，先以列建樹，在尾節點將出現次數加1，之後改以行訪問樹，將答案加上尾節點的出現次數。  

時間複雜度O(N^2)。  
空間複雜度O(N^2)。  

```python
class TrieNode:
    def __init__(self):
        self.child=defaultdict(TrieNode)
        self.cnt=0

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        N=len(grid)
        
        # build trie
        root=TrieNode()
        for row in range(N):
            curr=root
            for i in range(N):
                curr=curr.child[grid[row][i]]
            curr.cnt+=1
            
        # count equal
        ans=0
        for col in range(N):
            curr=root
            for i in range(N):
                curr=curr.child[grid[i][col]]
            ans+=curr.cnt
        
        return ans
```

因為測資很小，所以暴力比對也可以。  

時間複雜度O(N^3)。  
空間複雜度O(1)。  

```python
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        N=len(grid)
        ans=0
        
        for row in range(N):
            for col in range(N):
                ok=True
                for i in range(N):
                    if grid[row][i]!=grid[i][col]:
                        ok=False
                        break
                if ok:
                    ans+=1
                    
        return ans
```