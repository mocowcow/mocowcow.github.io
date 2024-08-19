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
