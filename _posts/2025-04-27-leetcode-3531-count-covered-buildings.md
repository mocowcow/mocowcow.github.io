---
layout      : single
title       : LeetCode 3531. Count Covered Buildings
tags        : LeetCode Medium Sorting BinarySearch
---
weekly contest 447。  
Q1 又是中等，這還真不太簡單。  

## 題目

<https://leetcode.com/problems/count-covered-buildings/description/>

## 解法

找有幾個格子的四方向都有其他格子。  
注意是某**方向**，不是正好旁邊一格。  

將 (x, y) 以 x 軸分組記做 xs[x] 後排序。  
二分搜找 y 的位置 = xs[idx]，若 idx 第一個 (最後一個) 索引，代表左方 (右方) 有格子。  

y 軸同理，分組後二分搜。  
兩軸都滿足則答案加 1。  

時間複雜度 O(n log n)。  
空間複雜度 O(n)。  

```python
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        xs = [[] for _ in range(n+1)]
        ys = [[] for _ in range(n+1)]
        for x, y in buildings:
            xs[x].append(y)
            ys[y].append(x)

        for idx in range(n+1):
            xs[idx].sort()
            ys[idx].sort()

        ans = 0
        for x, y in buildings:
            idx = bisect_left(xs[x], y)
            if idx == 0 or idx == len(xs[x])-1:
                continue

            idx = bisect_left(ys[y], x)
            if idx == 0 or idx == len(ys[y])-1:
                continue

            ans += 1

        return ans
```
