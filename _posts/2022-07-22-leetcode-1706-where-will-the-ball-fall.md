--- 
layout      : single
title       : LeetCode 1706. Where Will the Ball Fall
tags        : LeetCode Medium Array Matrix DFS DP Simulation
---
LC75學習計畫。這題的圖例嚇到我了，看起來有夠複雜，還以為是併查集類型，結果不是。  

# 題目
矩陣grid，代表一個m*n的盒子，盒子的頂部和底部都是打開的。  
盒子中的每個格子都有一個斜放的板子，可以將球導向左方或是右方：  
- 若板子為左上向右下放，則記為1  
- 若板子為右上向左下放，則記為-1  

我們在盒子每一列的頂部放一個球，球有可能在中途被板子堵住，或是順利掉出盒子外。  
回傳長度為n的陣列answer，其中answer[i]代表球從第i列放入後，最後出來的列數。若在中途被堵住，則回傳-1。  

# 解法
球抵達某個格子(r,c)後，只可能發生三種情形：  
1. 被卡住  
2. 往左下滾  
3. 往右下滾  

定義dp(r,c)：球從(r,c)出發，最後離開盒子的列數。  
轉移方程式：若板子為右斜且沒被卡住，則dp(r+1,c+1)；若板子為左斜且沒被卡住，則dp(r+1,c-1)；否則-1。  
base case：當r等於M時，代表順利掉出盒子外，直接回傳當前列數c。  

有以下四種情形會被卡住：  
1. 球往左滾碰到牆壁  
2. 球往左滾碰到向右的板子  
3. 球往右滾碰到牆壁  
4. 球往右滾碰到向左的板子  

最後分別對最上方的每一列投入球，加到答案中即可。  

```python
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        M,N=len(grid),len(grid[0])
        
        @cache
        def dp(r,c):
            if r==M:
                return c
            if grid[r][c]==1:
                if c==N-1 or grid[r][c+1]!=1:
                    return -1
                return dp(r+1,c+1)
            else:
                if c==0 or grid[r][c-1]!=-1:
                    return -1
                return dp(r+1,c-1)
    
        ans=[]
        for c in range(N):
            ans.append(dp(0,c))
        
        return ans
```

看到[lee神的解法](https://leetcode.com/problems/where-will-the-ball-fall/discuss/988576/JavaC%2B%2BPython-Solution-with-Explanation)才驚覺，或許右斜、左斜板子分別設為1和-1是有設計過的，否則為何不是1和0呢？是我沒有猜透出題者的心思。  
雖然執行時間慢了一些，但是邏輯看起來更清晰易懂。  

```python
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        M,N=len(grid),len(grid[0])
        
        @cache
        def dp(r,c):
            if r==M:
                return c
            cc=c+grid[r][c]
            if cc<0 or cc==N or grid[r][c]!=grid[r][cc]:
                return -1
            return dp(r+1,cc)
    
        ans=[]
        for c in range(N):
            ans.append(dp(0,c))
        
        return ans
```