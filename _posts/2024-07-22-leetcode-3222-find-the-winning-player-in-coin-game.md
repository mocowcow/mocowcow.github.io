---
layout      : single
title       : LeetCode 3222. Find the Winning Player in Coin Game
tags        : LeetCode Easy Simulation
---
biweekly contest 135。  

## 題目

輸入兩個正整數 x 和 y，分別代表面額 75 和 10 的硬幣個數。  

Alice 和 Bob 在玩遊戲，由 Alice 先手。  
每個玩家都必須選取價值共 115 的硬幣。若無法選擇，則該玩家敗北。  

回傳贏家的名字。  

## 解法

要湊 115 只有一種選法：一個 75 配上四個 10。  

直接看這兩種面額能夠玩幾回合，以較小者為準。  
若回合數是奇數，代表 Alice 贏；否則 Bob 贏。  

時間複雜度 O(1)。  
空間複雜度 O(1)。  

```python
class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        # 75*1 + 10*4
        r = min(x, y // 4)
        if r % 2 == 1:
            return "Alice"
        else:
            return "Bob"
```
