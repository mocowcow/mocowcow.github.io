---
layout      : single
title       : LeetCode 365. Water and Jug Problem
tags 		: LeetCode Medium BFS
---
臭狗今天食慾超級好，晚上吃了1.5罐頭、一堆雞胸肉、地瓜葉、壽桃、快半碗飯，不給吃還不行，一直亂叫。  

# 題目
jug1Capacity, jug2Capacity代表兩個罐子的容量，求有沒有辦法讓兩罐子的水量剛好達到targetCapacity。  
可以進行以下動作：  
1. 將任意罐子裝滿
2. 將任意罐子清空
3. 以任意罐子的水倒往另一罐，到目的罐裝滿為止

# 解法
好久以前看過，覺得是神奇數學題就不碰了，今天給我在graph學習計畫中碰到，命運給我開了另一扇窗。  
照著題目描述BFS暴力窮舉，一共三種行動，分別來自兩個罐子，每1個狀態會繼續產生6個可能狀態。  
初始數對為(0,0)代表兩罐都是空的，試著加水、清空、移動，直到某次兩罐容量剛好為targetCapacity。  
因為只能在兩個罐子內儲水，若目標大於兩罐總量的話可以直接回傳false。

```python
class Solution:
    def canMeasureWater(self, j1: int, j2: int, target: int) -> bool:
        if j1+j2 < target:
            return False
        q = [(0, 0)]
        visited = set()

        while q:
            t = []
            for w1, w2 in q:
                if (w1, w2) in visited:
                    continue
                if w1+w2 == target:
                    return True
                visited.add((w1, w2))
                t.append((j1, w2))  # fill 1
                t.append((w1, j2))  # fill 2
                diff2 = j2-w2
                delta = min(w1, diff2)
                t.append((w1-delta, w2+delta))  # 1 to 2
                diff1 = j1-w1
                delta = min(w2, diff1)
                t.append((w1+delta, w2-delta))  # 2 to 1
                t.append((0, w2))  # empty1
                t.append((w1, 0))  # empty2
            q = t

        return False

```
