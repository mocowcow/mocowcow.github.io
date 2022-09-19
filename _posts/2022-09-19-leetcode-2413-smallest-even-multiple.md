--- 
layout      : single
title       : LeetCode 2413. Smallest Even Multiple
tags        : LeetCode Easy 
---
周賽311。不得不說是相對簡單的Q1，比起前一天雙周賽的alice和bob好上一千倍。  

# 題目
輸入正整數n，求最小的整數，其同時是n和2的倍數。  

# 解法
很直覺的看出若n是偶數，那他一定也是2的倍數，不用處理直接回傳；若是奇數則將其乘二。  
但我稍微卡了一下，2乘上0.5等於1，那1是不是2的倍數？  
這時候要回到**倍數**的定義：若n存在一個整數x，使得n\*x=m，則稱m是n的倍數，所以1不是2的倍數。  

```python
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n&1:
            n*=2
        return n
```
