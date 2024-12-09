---
layout      : single
title       : LeetCode 3376. Minimum Time to Break Locks I
tags        : LeetCode Medium Simulation
---
biweekly contest 145。  
這題好像有點爭議，暴力枚舉聽說會卡常數，狀壓 dp 好像不該出現在 Q2，非常尷尬。  

## 題目

Bob 被關在迷宮裡，需要破壞 n 個鎖才能出去，但是破壞鎖需要**能量**。  
輸入整數陣列 strength，其中 strength[i] 代表破壞第 i 個鎖需要的能量。  

Bob 有一把劍，特徵如下：  

- 能量初始值為 0。  
- 能量恢復速率 X 初始值為 1。  
- 每分鐘，劍的能量會增加 X。  
- 想打開第 i 個鎖，**至少**需要能量 strength[i]。  
- 每破壞一個鎖，能量都會歸零，但是 X 會增加 K。  

求打開 n 個鎖需要的**最少**時間。  

## 解法

n 上限為 8，可以直接枚舉 8! = 40320 種排列，每種排列需要 O(n) 模擬。  

若開鎖需要能量 req，則需要等待 ceil(req/x) 分鐘恢復能量，然後才開鎖。  
注意：開鎖不需要花費時間。  

時間複雜度 O(n! \* n)。  
空間複雜度 O(n)。  

```python
class Solution:
    def findMinimumTime(self, strength: List[int], K: int) -> int:
        ans = inf
        for p in permutations(strength):
            time = 0
            x = 1
            for req in p:
                time += (req+x-1) // x # wait energy
                x += K
            ans = min(ans, time)

        return ans
```
