---
layout      : single
title       : LeetCode 3516. Find Closest Person
tags        : LeetCode Easy Simulation
---
weekly contest 445。

## 題目

<https://leetcode.com/problems/find-closest-person/description/>

## 解法

依照題意比較 abs(x-z) 和 abs(y-z) 的大小。  

時間複雜度 O(1)。  
空間複雜度 O(1)。  

```python
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        d1 = abs(z-x)
        d2 = abs(z-y)

        if d1 < d2:
            return 1
            
        if d1 > d2:
            return 2

        return 0
            
```
