---
layout      : single
title       : LeetCode 2971. Find Polygon With the Largest Perimeter
tags        : LeetCode Medium Greedy Sorting
---
雙周賽120。

## 題目

輸入長度n的正整數陣列nums。  

**多邊形**指的是一個平面的封閉圖形，且至少擁有三個邊。**最長**的邊**小於**其他邊的總和。  

也就是說，當你有k>=3個邊，邊長分別為a1, a2, a3, ..., ak，滿足a1 <= a2 <= a3 <= ... <= ak，且a1 + a2 + a3 + ... + ak-1 > ak，則**必定**存在由此k個邊組成的多邊型。  

多邊形的**周長**周長等於所有邊長的總和。  

求使用nums中所有整數可組成多邊型的**最大周長**，若無法組成多邊型則回傳-1。  

## 解法

為了使周長越大，用上越多的邊越好。  

在所有邊都使用的情況下，找到最大的邊mx，其餘邊長總和為other。只要滿足mx<other則存在合法多邊型；  
如果mx<=other，則丟棄mx，成為規模更小的子問題，重複直到找到為止。  

時間複雜度O(n log n)。  
空間複雜度O(1)。  

```python
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        other=sum(nums)
        
        while nums:
            mx=nums.pop()
            other-=mx
            if mx<other:
                return mx+other
            
        return -1
```
