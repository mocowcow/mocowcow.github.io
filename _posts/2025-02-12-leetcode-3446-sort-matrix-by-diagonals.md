---
layout      : single
title       : LeetCode 3446. Sort Matrix by Diagonals
tags        : LeetCode Medium Simulation Sorting
---
weekly contest 436。  
好像是首次 Q1 放中等題。  

## 題目

<https://leetcode.com/problems/sort-matrix-by-diagonals/description/>

## 解法

位於同一條對角線格子 (i, j) 來說，其 i-j 會是相同的。  
按照 i-j 將所有元素分類後排序，然後再回填。  

---

題目要求左下角要遞增，右上角要遞減。  

- i >= j 會在左下角，得到 i-j 是正數或 0。  
- i < j 會在右下角，得到 i-j 是負數。  

注意：方便起見直接拿 list 的 pop() 取出元素，所以要再反轉一次。  

時間複雜度 O(N^2 log N)。  
空間複雜度 O(N^2)。  

```python
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        N = len(grid)
        d = defaultdict(list)
        for i in range(N):
            for j in range(N):
                d[i-j].append(grid[i][j])

        for k, v in d.items():
            if k >= 0:
                v.sort(reverse=True)
            else:
                v.sort()
            v.reverse()

        for i in range(N):
            for j in range(N):
                grid[i][j] = d[i-j].pop()

        return grid
```
