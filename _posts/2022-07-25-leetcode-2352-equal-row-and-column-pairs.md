--- 
layout      : single
title       : LeetCode 2352. Equal Row and Column Pairs
tags        : LeetCode Medium Array Matrix HashTable
---
周賽303。python的comprehension在這題節省了不少時間，加上tuple可以雜湊，寫起來是真的快。  

# 題目
輸入n*n的整數矩陣grid，回傳有多少(i, j)數對，其中第i行和第j列相等。  
只要行和列出現的元素及順序相同，則認為它們是相等的。  

# 解法
同一個列可以和多個行組成數對，先將每一列轉成tuple後放入雜湊表d中計數。之後遍歷每一行，在雜湊表中找到相同結構的列有多少，並加入答案中。  

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
