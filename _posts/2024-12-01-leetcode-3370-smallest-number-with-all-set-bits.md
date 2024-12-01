---
layout      : single
title       : LeetCode 3370. Smallest Number With All Set Bits
tags        : LeetCode Easy BitManipulation
---
weekly contest 426。
python 神題。  

## 題目

輸入正整數 n。  

找到**最小**的數 x，滿足 x **大於等於** n，且其二進制表示中只有**設置位** (1 位元)。  

## 解法

暴力構造所有都是 1 位元組成的數字，直到大於等於 n 為止。  

時間複雜度 O(log n)。  
空間複雜度 O(1)。  

```python
class Solution:
    def smallestNumber(self, n: int) -> int:
        x = 1
        while x < n:
            x = (x << 1) | 1

        return x
```

其實相當於把 n 個每個位都改成 1。  
直接構造出和 n 的二進制長度相同的數即可。  

時間複雜度 O(1)。  
空間複雜度 O(1)。  

```python
class Solution:
    def smallestNumber(self, n: int) -> int:
        return (1 << n.bit_length()) - 1
```
