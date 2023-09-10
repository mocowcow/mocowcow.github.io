---
layout      : single
title       : LeetCode 2850. Minimum Moves to Spread Stones Over Grid
tags        : LeetCode Medium Array Matrix Backtracking
---
周賽362。連續兩次周賽做不出Q3，太吐血了，積分直接噴掉。  

## 題目

輸入3\*3的二維整數矩陣grid，代表每個格子的石頭數量。  
一個格子可以擁有多個石頭，但整個矩陣正好9個石頭。  

每次移動，你可以把一顆石頭移動到共邊的相鄰格子。  

求使得每個格子都有石頭的**最少移動次數**。  

## 解法

這次只能移動四個方向，所以將石頭移位的動作次數是**曼哈頓距離**。  

我想了超過一小時，一直在考慮如何用BFS還是什麼貪心方法來算，很可惜都不是。  
正確答案是：**暴力回溯**。  

只要暴力枚舉每個值為0的格子要從哪邊拿石頭，並把來源的石頭扣掉、加上移動步數，然後繼續遞迴處理下一個0。  

假設我們有N個沒有石頭的格子，剩下M個格子都是有石頭的。  
每次找石頭都要枚舉M個石頭堆，拿N次。  
雖然M^N看起來很大，但M+N=9，最差情況下M=4，N=5，M^N也才1024種結果。  

時間複雜度O(M^N)。  
空間複雜度O(N)。  

```python
class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        ans=inf
        
        def bt(i,cost):
            nonlocal ans
            if i==9:
                ans=min(ans,cost)
                return 
            r,c=i//3,i%3
            if grid[r][c]==0: # pick stone from somewhere
                for j in range(9):
                    rr,cc=j//3,j%3
                    if grid[rr][cc]>1:
                        grid[rr][cc]-=1
                        step=abs(r-rr)+abs(c-cc)
                        bt(i+1,cost+step)
                        grid[rr][cc]+=1
            else: # already has stone
                bt(i+1,cost)
        
        bt(0,0)
        
        return ans
```
