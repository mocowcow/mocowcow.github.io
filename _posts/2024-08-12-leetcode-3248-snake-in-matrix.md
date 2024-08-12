---
layout      : single
title       : LeetCode 3248. Snake in Matrix
tags        : LeetCode Easy Simulation Matrix
---
weekly contest 410。  

## 題目

輸入 n \* n 的正整數矩陣 grid，每個格子的邊號為 grid[i][j] = (i \* n) + j。  

有一隻蛇，可以在矩陣中往四個方向移動。  
他的初始位置在格子 0，並接收一連串移動指令陣列 commands。  

指令 command[i] 可能是 "UP", "RIGHT", "DOWN" 或 "LEFT"。保證移動一定會在矩陣內。  

求執行所有移動指令後，蛇所在格子的編號。  

## 解法

模擬題。  
竟然還保證不會越界，真的很佛心。  

python 3.10 終於加入了類似 switch 的語法，總算不需寫一堆 elif。  

時間複雜度 O(M)，其中 M = len(commands)。  
空間複雜度 O(1)。  

```python
class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        r = c = 0
        for cmd in commands:
            match cmd:
                case "UP":
                    r -= 1
                case "DOWN":
                    r += 1
                case "LEFT":
                    c -= 1
                case "RIGHT":
                    c += 1

        return r * n + c
```
