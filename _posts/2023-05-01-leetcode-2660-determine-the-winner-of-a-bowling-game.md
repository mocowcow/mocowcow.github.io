--- 
layout      : single
title       : LeetCode 2660. Determine the Winner of a Bowling Game
tags        : LeetCode Easy Array Simulation
---
周賽343。

# 題目
輸入整數陣列player1和player2，分別代表選手1和2在各局的擊倒數。  

一場保齡球共有n個回合，每回合都有10個瓶子。  

假設在第i回合打中xi個瓶子，則當回合的得分為：  
- 如果前兩回合中曾經打中10個瓶，則分數為2倍的x  
- 否則為x  

總得分為n個回合的總和。  

若選手1得分高，回傳1；選手2得分高，回傳2；平手回傳0。   

# 解法
先寫一個函數f來求選手分數。  
維護前兩個回合的得分數，只要其中一個是10，就拿兩倍；否則只拿一倍。最後更新前兩回的得分數。  

時間複雜度O(N)。  
空間複雜度O(1)。  

```python
class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        
        def f(p):
            score=0
            pprev=prev=0
            for x in p:
                if pprev==10 or prev==10:
                    score+=x*2
                else:
                    score+=x
                pprev,prev=prev,x
            return score
        
        s1=f(player1)
        s2=f(player2)  
        
        if s1>s2:
            return 1
        
        if s2>s1:
            return 2
        
        return 0
```
