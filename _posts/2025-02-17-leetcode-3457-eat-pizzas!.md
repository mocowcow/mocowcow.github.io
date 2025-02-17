---
layout      : single
title       : LeetCode 3457. Eat Pizzas!
tags        : LeetCode Medium Greedy Sorting
---
weekly contest 437。  
花了半小時才搞出證明，但至少是一次過，還算滿意。  

## 題目

<https://leetcode.com/problems/eat-pizzas/description/>

## 解法

總共要吃 cnt = N / 4 次漢堡。

每次吃 4 個漢堡，兩種操作輪流：  

- 操作一，得到**最大**的分數。  
- 操作二，得到**次大**的分數。  

操作一很直觀，就是選當前最大的，加上三個最小的。  

但操作二就很迷惑，如果選兩個最大的，會讓最大的被浪費。  
有時候似乎可以選擇四個最小的，然後讓下次操作一吃到最大的。  

---

先不管到底怎麼吃，總之操作次數是確定的。  
操作一有 odd =  ceil(cnt / 2) 次，操作二有 even = floor(cnt / 2) 次。  

先把前 odd 最大的漢堡給操作一吃。  
然後剩下都給操作二，挑次大的吃，重複 even 次。  

時間複雜度 O(N log N)。  
空間複雜度 O()。  

```python
class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        cnt = len(pizzas) // 4
        pizzas.sort()
        odd = (cnt+1) // 2
        even = cnt - odd
        ans = 0
        for _ in range(odd):
            ans += pizzas.pop()
        for _ in range(even):
            pizzas.pop()
            ans += pizzas.pop()

        return ans
```
