---
layout      : single
title       : LeetCode 3560. Find Minimum Log Transportation Cost
tags        : LeetCode Easy Math
---
weekly contest 451。  
閱讀理解測驗題。  

## 題目

<https://leetcode.com/problems/find-minimum-log-transportation-cost/description/>

## 解法

要看清楚，有兩根木頭，**三台卡車**。  
每台卡車只能裝一根木頭，且木頭長度至多 k。  

雖然沒有明說可切幾刀，但是題目最下方有保證卡車一定能裝得下木頭，反推出**至多只有一根木頭要切**。  
設 x = max(n, m)，若 x <= k 則不切，答案 0。  

否則將 x 切成兩段木頭，長度分別為 len1 = y, len2 = (x-y)，成本公式為 len1 \* len2。  
代入公式得：  
> y \* (x-y)  
> -(y^2) + xy  

y 越大成本越小，取 y = k。  
最小成本為 k \* (x-k)。  

時間複雜度 O(1)。  
空間複雜度 O(1)。  

```python
class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        x = max(n, m)
        if x <= k:
            return 0

        return k * (x-k) 
```
