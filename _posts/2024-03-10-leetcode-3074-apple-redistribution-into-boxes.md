---
layout      : single
title       : LeetCode 3074. Apple Redistribution into Boxes
tags        : LeetCode Easy Array Sorting Greedy
---
周賽388。

## 題目

輸入長度 n 的整數陣列 apple，還有長度 m 的整數陣列 capacity。  

總共有 n 袋蘋果，其中 apple[i] 代表第 i 袋裡面個蘋果數。  
箱子有 m 個，其中 capacity。[i] 代表第 i 箱可容納的蘋果的數。  

求**最少**需要幾個箱子，才能把所有蘋果都裝箱。  

注意：來自同一袋子蘋果可以分裝到不同箱子。  

## 解法

先看有多少蘋果。  
把箱子排序，從最大的箱子開始裝即可。  

時間複雜度 O(n + m log m)。  
空間複雜度 O(1)。  

```python
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        need = sum(apple)
        capacity.sort()
        
        ans = 0
        while need > 0:
            need -= capacity.pop()
            ans += 1
            
        return ans
```
