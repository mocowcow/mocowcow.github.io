--- 
layout      : single
title       : LeetCode 2658. Maximum Number of Fish in a Grid
tags        : LeetCode Medium Array Matrix DFS
---
雙周賽103。這鬼題當初還標hard，一看發現根本是經典題，真是騙很大。今天寫題解發現被打回medium。  
順帶一題，這題正是字面意思的**竭澤而漁**。  

# 題目
輸入m\*n的二維矩陣grid，其中(r,c)：  
- 若grid[r][c]為0，代表**陸地**  
- 否則是**海洋**，且有grid[r][c]隻魚  

一個漁夫可以從任意**海洋**位置(r,c)出發，並執行以下動作數次：  
- 把(r,c)的魚抓完  
- 或是前往其他相鄰的**海洋**  

求漁夫的**最大捕魚數**。如果捕不到魚則回傳0。  

# 解法
簡單來講就是連在一起的海洋裡面的魚可以全抓，所以只要選一塊最多魚著連通塊。  

寫一個函數dfs(r,c)，代表從(r,c)開始抓，總共可以抓到多少魚。  
判斷上下左右四個方向，如果同為海洋，那也可以一起捕抓。  
然而捕捉過的點可以把魚清空設為0，這樣可以省略掉標記訪問狀態vis陣列。  

最後遍歷整個矩陣，碰到還有魚的就dfs下去看可以抓多少魚，更新答案最大值。  

時間複雜度O(MN)。  
空間複雜度O(MN)。  

```python
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        M,N=len(grid),len(grid[0])
        ans=0
        
        def dfs(r,c):
            fish=grid[r][c]
            grid[r][c]=0
            for dx,dy in pairwise([0,1,0,-1,0]):
                rr,cc=r+dx,c+dy
                if 0<=rr<M and 0<=cc<N and grid[rr][cc]>0:
                    fish+=dfs(rr,cc)
            return fish
        
        for r in range(M):
            for c in range(N):
                if grid[r][c]>0:
                    ans=max(ans,dfs(r,c))
                    
        return ans
```
