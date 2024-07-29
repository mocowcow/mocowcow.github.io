---
layout      : single
title       : LeetCode 3232. Find if Digit Game Can Be Won
tags        : LeetCode Easy Simulation
---
weekly contest 408。  

## 題目

輸入正整數陣列 nums。  

Alice 和 Bob 在玩遊戲。  
Alice 可以選擇 nums 中所有一位數的數字，**或是**所有兩位數的數字。而沒選中的都給 Bob。  
如果 Alice 的數字總和**嚴格大於** Bob 的數字總和，則 Alice 獲勝。  

若 Alice 可以獲勝則回傳 true，否則回傳 false。  

## 解法

nums 中的數可以分成兩種：  

- 一位數 (x <= 10)  
- 二位數 (10 <= x <= 99)  

按照題意模擬，將數分成兩份。  
只要兩份不相等，則 Alice 可以選擇總和較大者獲勝；否則平手。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        a = b = 0
        for x in nums:
            if x < 10:
                a += x
            else:
                b += x

        return a != b
```
