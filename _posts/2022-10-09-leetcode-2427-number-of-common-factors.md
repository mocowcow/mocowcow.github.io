--- 
layout      : single
title       : LeetCode 2427. Number of Common Factors
tags        : LeetCode Easy Math Simulation
---
周賽313。才開始上班電腦就壞掉，上次雙周賽不好容易四題，結果Q1還被rejude掉，多災多難。  

# 題目
輸入兩個正整數a和b，求a和b有多少公因數。  
如果x同時整除a和b，則整數x是a和b的公因數。  

# 解法
照個題目做就行，可以取a和b較小值，也可以直接取測資範圍1000。只要某數i同時整除，則答案+1。  

時空間複雜度O(min(a,b))。  

```python
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        ans=0
        for i in range(1,min(a,b)+1):
            if a%i==0 and b%i==0:
                ans+=1
                
        return ans
```

python一行版本。

```python
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        return sum(a%i==0 and b%i==0 for i in range(1,min(a,b)+1))
```
