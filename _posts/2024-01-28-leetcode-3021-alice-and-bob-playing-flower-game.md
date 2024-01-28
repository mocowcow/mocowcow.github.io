---
layout      : single
title       : LeetCode 3021. Alice and Bob Playing Flower Game
tags        : LeetCode Medium Math
---
周賽382。還以為 Alice 這傢伙又要搞什麼神奇遊戲，差點沒嚇死，好險不太困難。  

## 題目

Alice 和 Bob 在一個圓形場地玩遊戲，場地上有一些花。  
Alice 到 Bob 的順時鐘方向上有 x 朵花，逆時鐘方向上有 y 朵花。  

遊戲流程如下：  

- Alice 先攻  
- 每一回合，玩家可以從順 / 逆時鐘方向拿取一朵花  
- 若回合結束，所有花都被拿完，則**當前**玩家勝利  

輸入整數 n 和 m，你的目標是找出有多少數對 (x, y) 滿足以下限制：  

- 使 Alice 獲勝  
- 順時鐘方向上的 x 花數量必須介於 [1, n] 之間  
- 順時鐘方向上的 y 花數量必須介於 [1, m] 之間  

求有多少數對 (x, y) 滿足以上條件。  

## 解法

本來以為是什麼數學題，有點恐慌。  
冷靜一想，花在哪邊根本沒有差，只要花總數是**奇數**，Alice 就會贏。  

暴力枚舉所有 (x, y) 肯定不行。  
退而求其次，枚舉所有 x，試著找合法的 y。  

為了 x + y 是奇數：  

- 若 x 是奇數，則 y 必須是偶數  
- 若 x 是偶數，則 y 必須是奇數  

枚舉 x，直接對答案加上 y 對應的奇偶數即可。  

時間複雜度 O(min(m, n))。  
空間複雜度 O(1)。  

```python
class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        # x + y is odd, then Alice win
        ans = 0
        odd = (m + 1) // 2
        even = m - odd
        for x in range(1, n+1):
            if x % 2 == 0: # even x, odd y
                ans += odd
            else: # odd x, even y
                ans += even
                
        return ans
```

後來再想想，既然都可以直接求 x 的奇偶數，那 y 不也可以？  
根據乘法原理，答案是：  
> **偶數x** \* **奇數y** + **奇數x** \* **偶數y**

時間複雜度 O(1)。  
空間複雜度 O(1)。  

```python
class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        x_even = n // 2
        x_odd = n - x_even
        y_even = m // 2
        y_odd = m - y_even

        return x_even * y_odd + x_odd * y_even
```
