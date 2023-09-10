---
layout      : single
title       : LeetCode 2849. Determine if a Cell Is Reachable at a Given Time
tags        : LeetCode Medium Math
---
周賽362。這題挺陷阱的，但很有良心沒搞隱藏測資，不然提交通過率可能連15%都不到。  

## 題目

輸入四個整數sx, sy, fx, fy，還有一個**非負**整數t。  

有個無限大的二維網格，起點位於(sx, sy)。每一秒鐘，你**必須**移動到任意相鄰(8個方向)的格子。  

如果可以在**正好t秒**時抵達(sx, sy)則回傳true，否則回傳false。  

## 解法

格子是無限大的，秒數t也很大，想要bfs模擬肯定不行。  

本題中允許斜走，所以抵達終點的最短距離dis取決於兩點間**x軸差和y軸差的較大者**。  
若dis>t，則不可能抵達；反之可以多移動幾次來消耗多餘時間，理論上一定可以達成要求。  

但是起終點也可能**相同**，這時又剛好t=1，強迫你一定要從起點離開，但是**就回不來了**。  
這是唯一一個dis小於等於t卻不可能達成的情況。  

時間複雜度O(1)。  
空間複雜度O(1)。  

```python
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        dx=abs(sx-fx)
        dy=abs(sy-fy)
        dis=max(dx,dy)
        
        if dis>t:
            return False
        
        if dis==0 and t==1:
            return False
        
        return True
```
