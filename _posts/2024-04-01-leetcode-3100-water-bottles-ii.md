---
layout      : single
title       : LeetCode 3100. Water Bottles II
tags        : LeetCode Medium Simulation Math
---
周賽 391。又是模擬題。  

## 題目

輸入兩個整數 numBottles 和 numExchange。  

numBottles 代表你最初擁有多少裝滿的瓶裝水。  
每次操作，你可以選擇以下之一：  

- 喝掉任意瓶水，並得到相同數量的空瓶  
- 將 numExchange 兌換一瓶新的水。之後 numExchange 會增加 1  

注意：每次兌換只能換到一瓶新的水。  
例如 numExchange = 1 時，無論你有多少空瓶，都只能拿一個空瓶換一瓶水。  

求最多可以喝幾瓶水。  

## 解法

方便起見，有水就喝。而且要喝就一次喝完，節省時間。  
沒水再去拿空瓶換，沒得換就停。  

---

邏輯實現非常簡單，複雜度分析就比較有趣了。  
每次喝水都是直接喝完，計算幾次主要和**空瓶兌換**幾次有關。  

numExchange 從 1 開始，兌換要求會是 1, 2, 3..，是**等差級數**。  
兌換 a 次，共需要 a \* (a + 1) / 2 個空瓶。  

把最初的 numBottles 瓶水代入：  
> numBottles >= a \* (a + 1) / 2  
> 2 \* numBottles >= a \* (a + 1)  
> sqrt(numBottles) >= a  

差不多比開根號再多一點點。  

時間複雜度 O(sqrt(numBottles))。  
空間複雜度 O(1)。  

```python
class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        full = numBottles
        empty = 0
        ans = 0
        
        while True:
            # drink all
            if full > 0:
                ans += full
                empty += full
                full = 0
            # get free one
            elif empty >= numExchange:
                full += 1
                empty -= numExchange
                numExchange += 1
            else:
                break
                
        return ans
```
