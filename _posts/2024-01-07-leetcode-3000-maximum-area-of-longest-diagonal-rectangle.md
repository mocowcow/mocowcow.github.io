---
layout      : single
title       : LeetCode 3000. Maximum Area of Longest Diagonal Rectangle
tags        : LeetCode Easy Array Simulation
---
周賽379。變數名稱太長就容易打錯，這時候不用宣告就成了python缺點，賦值時拼錯字也不會報錯。
更要命的是範例的答案竟然還剛好一樣，喜提一隻BUG。  

## 題目

輸入二維整數陣列dimensions。  

對於 0 <= i < dimensions.length 中的所有索引i，其中dimensions[i][0]代表第i個長方形的長度，而dimensions[i][1]代表寬度。  

求擁有**最長對角線**的長方形的**面積**。如果有多個長方形的對角線並列最長，則選擇面積最大者。  

## 解法

暴力模擬。  
直接算每個長方形的對角線，選擇對角線最長/面積最大者。  

時間複雜度O(N)。  
空間複雜度O(1)。  

```python
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        ans=0
        mx_side=0
        for a,b in dimensions:
            area=a*b
            side=(a*a+b*b)**0.5
            if side>mx_side:
                mx_side=side
                ans=area
            elif side==mx_side and area>ans:
                ans=area
                
        return ans
```

python 一行版本。

在比較大小時，有兩個關鍵字：**對角線**和**面積**。  
先比對角線，再比面積。直接把這兩個做成 tuple 或 list 比較。  

```python
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        return max([x**2 + y**2, x * y] for x, y in dimensions)[1]
```
