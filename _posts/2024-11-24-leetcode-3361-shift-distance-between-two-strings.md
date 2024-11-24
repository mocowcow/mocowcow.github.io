---
layout      : single
title       : LeetCode 3361. Shift Distance Between Two Strings
tags        : LeetCode Medium Simulation
---
biweekly contest 144。  
這鳥題應該只值 4 分，設 5 分真的是抬舉。  

## 題目

輸入兩個相同長度的字串 s 和 t，以及兩個整數陣列 nextCost 和 previousCost。  

每次操作，你可以選擇任意 s[i]，並執行以下動作之一：  

- 將 s[i] 變成字母表中的下一個字母。若 s[i] == 'z'，則變成 'a'。  
    若 s[i] = j，則操作成本為 nextCost[j]。  
- 將 s[i] 變成字母表中的上一個字母。若 s[i] == 'a'，則變成 'z'。  
    若 s[i] = j，則操作成本為 previousCost[j]。  

移動距離指的是將 s 變成 t 的**最小總成本**。  

求 s 變成 t 的移動距離。  

## 解法

要把字元 x 變成 y 只有兩種選擇：  

- 不斷換成前一個字元。
- 不斷換成後一個字元。

回頭一定是繞遠路，只能固定一個方向走。  
一個方向最多走 25 步，而且兩方向加起來至多 26 步。  
枚舉兩個方向的成本取最小值即可。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:

        def f(x, y):
            x, y = ord(x)-97, ord(y)-97
            cost = 0
            while x != y:
                cost += nextCost[x]
                x = (x+1) % 26
            return cost

        def g(x, y):
            x, y = ord(x)-97, ord(y)-97
            cost = 0
            while x != y:
                cost += previousCost[x]
                x = (x-1) % 26
            return cost

        ans = 0
        for x, y in zip(s, t):
            ans += min(f(x, y), g(x, y))

        return ans
```
