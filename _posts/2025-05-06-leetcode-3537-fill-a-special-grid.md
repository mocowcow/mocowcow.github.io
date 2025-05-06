---
layout      : single
title       : LeetCode 3537. Fill a Special Grid
tags        : LeetCode Medium Simulation DevideAndConquer
---
weekly contest 448。  
好像很久沒有看過這種遞迴題。  

## 題目

<https://leetcode.com/problems/fill-a-special-grid/description/>

## 解法

求邊長 2^n 的正方形，每格都填入不同的數字。  
若邊長不為 0，則可拆分成四個邊長 2^(n-1) 的正方形。  

每個正方形需滿足：  

- 右上的值都小於右下的值  
- 右下的值都小於左下的值  
- 左下的值都小於左上的值  

發現就是由四個規模更小的子問題組成。  
順序為：右上、右下、左下、左上。  
維護全局變數 val 進行遞迴即可。  

定義 f(x, y, sz)：填充左上角為 (x, y)，邊長 sz 的正方形。  
答案入口 f(0, 0, 2^n)。  

時間複雜度 O(2^n \* 2^n)，或 O(4^n)。  
空間複雜度 O(n)，遞迴堆疊空間。答案空間不計入。  

```python

class Solution:
    def specialGrid(self, n: int) -> List[List[int]]:
        sz = 2 ** n
        ans = [[-1]*sz for _ in range(sz)]
        val = 0

        def f(x, y, sz):
            nonlocal val
            if sz == 1:
                ans[x][y] = val
                val += 1
                return

            half = sz // 2
            f(x, y+half, half)
            f(x+half, y+half, half)
            f(x+half, y, half)
            f(x, y, half)

        f(0, 0, sz)

        return ans
```
