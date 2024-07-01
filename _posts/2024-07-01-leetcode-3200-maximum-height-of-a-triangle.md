---
layout      : single
title       : LeetCode 3200. Maximum Height of a Triangle
tags        : LeetCode Easy Simulation Math
---
周賽 404。

## 題目

輸入兩個整數 red 和 blue，分別代表兩種顏色的球的數量。  
你必須將這些球排成三角形，第一列有 1 顆球、第二列有 2 顆球，以此類推。  

除此之外，同一列中的球都必須是相同顏色，且相鄰的兩列顏色需不同。  

求三角形的最大高度。  

## 解法

枚舉紅藍或是藍紅的順序，之後暴力模擬。  

為了達到紅藍交替 (奇偶交替) 的效果，維護一個變數 parity，將層數的奇偶性和顏色對應。  
每次操作後 parity 和 1 做 XOR，即可實現 0, 1, 0, 1,.. 循環。  

時間複雜度 O(sqrt(red) + sqrt(blue))。  
空間複雜度 O(1)。  

```python
class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        
        def f(parity):
            cnt = [red, blue]
            need = 1
            res = 0
            while cnt[parity] >= need:
                cnt[parity] -= need
                res += 1
                need += 1
                parity ^= 1
            return res
        
        return max(f(0), f(1))
```
