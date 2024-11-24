---
layout      : single
title       : LeetCode 3360. Stone Removal Game
tags        : LeetCode Easy Simulation
---
biweekly contest 144。  
這兩人終於玩點正常的遊戲，只可惜我手殘按了兩次 WA。  

## 題目

Alice 和 Bob 又在玩遊戲，每回合輪流拿走石頭，由 Alcie 先攻。  

- Alice 第一回合需要拿走 10 個石頭。  
- 之後每回合，輪到的人必須拿走的石頭都**比前一人少一個**。  

無法採取行動者即敗北。  

輸入整數 n，若 Alice 能勝利則回傳 true，否則回傳 false。  

## 解法

暴力模擬，拿不了石頭就終止迴圈。  

本題 n 最多 50，而 1+2+..+9 是 55，不會出現有人拿 0 個石頭的情況。  

時間複雜度 O(sqrt(n))。  
空間複雜度 O(1)。  

```python
class Solution:
    def canAliceWin(self, n: int) -> bool:
        alice_turn = True
        cost = 10
        while n >= cost:
            n -= cost
            cost -= 1
            alice_turn = not alice_turn

        return not alice_turn
```
