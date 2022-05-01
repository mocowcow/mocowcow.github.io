--- 
layout      : single
title       : LeetCode 2257. Count Unguarded Cells in the Grid
tags        : LeetCode Medium Array Matrix Simulation
---
雙周賽77。我超喜歡這題的，本來還想說是不是要O(N^2)暴力法，一看測資覺得不對，原來有點小技巧。

# 題目
輸入整數m,n 代表一個M*N的空間。二維陣列guards和walls分別代表警衛和牆壁的位置。  
每個警衛同時監視著上下左右四個方向，除非被其他警衛或是牆壁擋住，否則可以一望到底。  
求有多少空位沒被監視。

# 解法
首先要找出那些地方是空位，建立m*n的陣列grid，初始化為0，並把警衛和牆壁標記為1。  
再來遍歷所有警衛，計算監視範圍。  
從警衛位置往四方出發，沿途標記標記為2，代表被監視，直到出界或是被其他警衛或是牆壁擋住為止。  
最後遍歷grid，計算剩下的0數量，就是沒被監視的位置數量。  

程式碼有點臭長，但是只跑3396ms，不算太差。

```python
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid=[[0]*n for _ in range(m)] 
        for r,c in walls:
            grid[r][c]=1
        for r,c in guards:
            grid[r][c]=1
        
        for r,c in guards:
            #4ways
            #up
            rr=r-1
            while rr>=0 and grid[rr][c] in [0,2]:
                grid[rr][c]=2
                rr-=1
            #down
            rr=r+1
            while rr<m and grid[rr][c] in [0,2]:
                grid[rr][c]=2
                rr+=1
            #left
            cc=c-1
            while cc>=0 and grid[r][cc] in [0,2]:
                grid[r][cc]=2
                cc-=1
            #right
            cc=c+1
            while cc<n and grid[r][cc] in [0,2]:
                grid[r][cc]=2
                cc+=1
                
        ans=0
        for row in grid:
            for x in row:
                if x==0:
                    ans+=1

        return ans
```

重構一下，把四個方向的檢查塞入一個迴圈，順便把最後加總計算改用內建函數。  
簡潔又可讀，還很快，執行2232ms，勝過100%。

```python
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid=[[0]*n for _ in range(m)] 
        dirs=[(1,0),(-1,0),(0,1),(0,-1)] #4ways
        for r,c in walls:
            grid[r][c]=1
        for r,c in guards:
            grid[r][c]=1
        for r,c in guards:
            for dr,dc in dirs:
                rr=r+dr
                cc=c+dc
                while 0<=rr<m and 0<=cc<n and grid[rr][cc]!=1:
                    grid[rr][cc]=2
                    rr+=dr
                    cc+=dc
            
        return sum(row.count(0) for row in grid)
```
