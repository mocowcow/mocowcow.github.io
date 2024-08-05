---
layout      : single
title       : LeetCode 3238. Find the Number of Winning Players
tags        : LeetCode Easy Simulation
---
biweekly contest 136。  
看到不少人說這題很難，有點沒搞懂難點在哪。或許是沒注意到顏色有限？  

## 題目

輸入整數 n，代表有 n 個玩家在比賽。  
另外還有二維整數陣列 pick[i] = [x<sub>i</sub>, y<sub>i</sub>]，代表第 x<sub>i</sub> 個玩家得到一顆顏色為 y<sub>i</sub> 的球。  

若玩家 i 擁有相同顏色的球**超過** i 顆則**獲勝**。也就是說：  

- 玩家 0 有球就獲勝  
- 玩家 1 有至少 2 顆相同顏色的球就獲勝  
- 玩家 i 有至少 i+1 顆相同顏色的球就獲勝  

求有多少玩家獲勝。  

## 解法

注意到顏色最多只有 11 種，開二維陣列統計各玩家擁有的各色球數後，球數最大值大於編號 i 即可。  

```python
class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        cnt = [[0] * 11 for _ in range(n)]
        for x, y in pick:
            cnt[x][y] += 1

        return sum(max(cnt[i]) > i for i in range(n))
```
