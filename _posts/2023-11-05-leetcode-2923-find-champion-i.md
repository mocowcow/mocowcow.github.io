---
layout      : single
title       : LeetCode 2923. Find Champion I
tags        : LeetCode Easy Array Matrix Greedy
---
周賽370。這題有點腦筋急轉彎，害我卡了一陣子。  
然後網站伺服器也在卡，中國站卻沒事，只能說中國站各方面(可用性、題庫、價格)都做得比本站好。  

## 題目

有n個隊伍在比賽，編號分別為0到n-1。  

輸入n\*n的二維矩陣grid。若grid[i][j]==1，代表隊伍i比隊伍j**更強**；反之，隊伍j比隊伍i強。  

如果對於隊伍a來說，不存在任意隊伍b比a更強，則a是比賽的**冠軍**。  

求這場比賽的冠軍隊伍。  

## 解法

grid[i][j]是說i比j強，若grid[i][j]為1，只能告訴我們**j不是冠軍**。  
反過來說，對於固定的j來說，若不存在任意grid[i'][j]為1，則代表j最強。  

先枚舉j，裡面再來一次迴圈枚舉i，只要沒有grid[i][j]為1，則當前j就是答案。  

時間複雜度O(n^2)。  
空間複雜度O(1)。  

```python
class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        N=len(grid)
        
        for j in range(N):
            for i in range(N):
                if grid[i][j]==1:
                    break
            else:
                return j
```

仔細想想，那會不會有兩個隊伍一樣強的情況？  
測資保證了當i!=j時，grid[i][j]!=grid[j][i]，所以兩個不同的隊伍強度必定不等。  

既然如此，那麼冠軍一定會比自己以外的N-1個隊伍都強。  

時間複雜度O(N^2)。  
空間複雜度O(1)。  

```python
class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        N=len(grid)
        for i in range(N):
            if sum(grid[i])==N-1:
                return i
```
