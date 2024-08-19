---
layout      : single
title       : LeetCode 3259. Maximum Energy Boost From Two Drinks
tags        : LeetCode Medium DP
---
weekly contest 411。  

## 題目

輸入兩個長度 n 的整數陣列 energyDrinkA 和 energyDrinkB。  
各代表在第 i 小時喝下兩種飲料能提供的能量。  

你每小時只能喝一種飲料，且希望能量**最大化**。  
但是如果你喝的飲料和上次不一樣，則必須先休息一小時，才能改喝另一種 (即下一小時不獲得能量)。  

求 n 小時可以得到的**最大能量**。  

注意：兩種飲料都可以作為初始種類。  

## 解法

方便起見，將兩種飲料包成二維陣列 a。  
其中 a[0] = energyDrinkA, a[1] = energyDrinkB。  

喝完飲料後有兩種選擇：**換**或**不換**。  
當你有 x 罐飲料時，若不換種類，則剩下 x-1 罐飲料要喝；若換種類，跳過一小時，則剩下 x-2 罐飲料要喝。  
不同的選擇策略可能會剩下相同的數量，有**重疊的子問題**，因此考慮 dp。  

定義 dp(i, typ=0/1)：當前喝 typ，在第 [i..n-1] 小時獲得的最大能量。  
轉移：dp(i, typ) = max(dp(i+1, typ) + dp(i+2, other_typ)) + a[typ][i]  
base：當 i >= N，已經沒飲料喝，回傳 0。  

初始飲料可以任選，答案是 dp(0, 0), dp(0, 1) 取最大。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        N = len(energyDrinkA)
        a = [energyDrinkA, energyDrinkB]

        @cache
        def dp(i, typ): # a[typ][i]
            if i >= N:
                return 0
            return max(
                dp(i+1, typ), # keep
                dp(i+2, typ^1) # change
            ) + a[typ][i]

        return max(
            dp(0, 0),
            dp(0, 1)
        )
```

改寫成遞推。  

```python
class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        N = len(energyDrinkA)
        a = [energyDrinkA, energyDrinkB]

        f = [[0]*2 for _ in range(N+2)]
        for i in reversed(range(N)):
            for typ in range(2):
                f[i][typ] = max(
                    f[i+1][typ],
                    f[i+2][typ^1]
                ) + a[typ][i]

        return max(f[0][0], f[0][1])
```

注意到 dp[i] 只會參考到 dp[i+1] 和 dp[i+2]。  
因此只需要保留前兩次的狀態，可以使用滾動陣列優化。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        N = len(energyDrinkA)
        a = [energyDrinkA, energyDrinkB]

        f1, f2 = [0]*2, [0]*2
        for i in reversed(range(N)):
            f0 = [0]*2
            for typ in range(2):
                f0[typ] = max(f1[typ], f2[typ^1]) + a[typ][i]
            f1, f2 = f0, f1

        return max(f1)
```
