---
layout      : single
title       : LeetCode 3001. Minimum Moves to Capture The Queen
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

棋盤大小是常數，不記入複雜度，因此上面方法才是 O(1)。  
如果棋盤超大，那上面方法就會超時。  
直接透過座標判斷是否**共線**才能做到真正的常數時間。  

透過 x, y 座標可以很簡單的判斷水平 / 垂直共線，而 x-y 可判斷是否同處一條**反斜線**， x+y 可判斷同處**斜線**。  

城堡直接吃皇后，必須和皇后共線，且滿足以下之一：  

1. 主教不共線 或  
2. 主線共線但沒擋在中間  

主教吃皇后同理。  

為了快速判斷三者共線但某者不擋住中間，把邏輯提取成函數 ok(left ,mid, right)：只要 mid 不夾在中間就是 true。  
當然有時候順序會相反，例如 [城堡, 主教, 皇后] 等價於 [皇后, 主教, 城堡]，只要左右兩值互換即可。  

時間複雜度 O(1)。  
空間複雜度 O(1)。  

```python
def ok(left, mid, right): # check if [left, right] not blocked by mid
    return not (min(left, right) < mid < max(left, right))
    
class Chess:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.slash = self.x + self.y
        self.r_slash = self.x - self.y

class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        rook = Chess(a, b)
        bishop = Chess(c, d)
        queen = Chess(e, f)
        
        # rook to queen
        # horizontal 
        if rook.x == queen.x and \
            (rook.x != bishop.x or ok(rook.y, bishop.y, queen.y)):
                return 1
        # vertical
        if rook.y == queen.y and \
            (rook.y != bishop.y or ok(rook.x, bishop.x, queen.x)):
                return 1
            
        # priest to queen
        # slash
        if bishop.slash == queen.slash and \
            (bishop.slash != rook.slash or ok(bishop.x, rook.x, queen.x)):
                return 1
        # reversed slash
        if bishop.r_slash == queen.r_slash and \
            (bishop.r_slash != rook.r_slash or ok(bishop.x, rook.x, queen.x)):
                return 1
        
        return 2
```
