---
layout      : single
title       : LeetCode 10036. Minimum Moves to Capture The Queen
tags        : LeetCode Medium Simulation
---
周賽379。又打錯變數名稱，再喜提一隻BUG。  
這種囉嗦的分類討論，一次寫出正確邏輯還是挺高興的。結果碰到打錯字這種低能錯誤，心情複雜。  
~~而且我不會玩西洋棋。~~  

## 題目

有個8x8的棋盤，上面有3顆棋子。  

輸入變數 a, b, c, d, e 和 f：  

- (a, b) 代表白城堡的座標  
- (c, d) 代表白主教的座標  
- (e, f) 代表黑皇后的座標  

你只能移動白棋，求最少需要移動幾次才能**吃到**黑皇后。  

注意：  

- 城堡可以水平/垂直移動任意步數，但是不可越過其他棋  
- 主教可以對角線移動任意步數，但是不可越過其他棋  
- 若皇后處於城堡或主教若的可移動範圍上，則可**吃到**黑皇后  
- 黑皇后不會移動  

## 解法

城堡吃皇后有以下幾種情況：  

1. 兩者不共線，需要水平垂直各移動一次。共2步  
2. 兩者共線，直接吃皇后。共1步  
3. 兩者共線，但中間被主教擋住。先把主教弄走，才吃皇后。共2步  

主教吃皇后的情況有：  

1. 兩者不共線，吃不到  
2. 兩者共線，直接吃皇后。共1步  
3. 兩者共線，但中間被城堡擋住。先把城堡弄走，才吃皇后。共2步  

發現只有1步或2步兩種可能。  
只要城堡或主教可以直接吃皇后，答案就是1；否則是2。  

好在這題非常良心，棋盤不大，可以直接模擬移動，一邊檢查是否碰到其他棋子。不然只靠座標判斷共線還不太好寫。  

時間複雜度O(1)。  
空間複雜度O(1)。  

```python
class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        # queen
        qx,qy=e,f
        
        # rook 4 dir
        for dx,dy in pairwise([0,1,0,-1,0]):
            x,y=a,b
            while 0<=x<=8 and 0<=y<=8:
                x,y=x+dx,y+dy
                if x==c and y==d: # block by bishop
                    break
                if x==qx and y==qy: # queen
                    return 1

        # bishop 4 dir
        for dx,dy in [[-1,-1],[-1,1],[1,1],[1,-1]]:
            x,y=c,d
            while 0<=x<=8 and 0<=y<=8:
                x,y=x+dx,y+dy
                if x==a and y==b: # block by rook
                    break
                if x==qx and y==qy: # queen
                    return 1
        
        return 2
```
