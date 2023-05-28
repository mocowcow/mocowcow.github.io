--- 
layout      : single
title       : LeetCode 2706. Buy Two Chocolates
tags        : LeetCode Easy Array Sorting
---
雙周賽105。

# 題目
輸入整數陣列prices，代表商店中每塊巧克力的價錢。另外還有整數money，代表你一開始持有的錢。  

你必須購買兩塊不同的巧克力，總價格越小越好，但不能超過你持有的錢。  

回傳買完巧克力後剩下的錢。如果買不起則回傳money。  

# 解法
直接排序，前面兩個就是最小和次小的價格。  
如果不超過money從money中扣除，否則直接回傳money。  

時間複雜度O(N log N)。  
空間複雜度O(1)。  

```python
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        mn=prices[0]+prices[1]

        if mn>money:
            return money

        return money-mn
```

不需要排序也可以找到前兩小的價格。  

時間複雜度O(N)。  
空間複雜度O(1)。  

```python
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        x1=x2=inf
        for p in prices:
            if p<x1:
                x2=x1
                x1=p
            elif p<x2:
                x2=p
                
        if x1+x2>money:
            return money
        
        return money-x1-x2
```