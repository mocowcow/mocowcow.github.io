---
layout      : single
title       : LeetCode 2938. Separate Black and White Balls
tags        : LeetCode Medium String Greedy TwoPointers
---
周賽372。

## 題目

桌上有n個球，球只能是白或黑色。  

輸入長度n的二進位字串s，其中1代表黑球，而0代表白球。  
每次操作，你可以將兩個相鄰的球交換位置。  

求**最少**需要幾次操作，才能使得所有白球都在左半邊，且所有黑球都在右半邊。  

## 解法

白左黑右，最終會呈現00..11這樣子。  

我們只要將白色往左移動，黑色自然會被排擠到右邊去。  
例如：  
> 11**0**  
> 將0移動到最左，需要兩次操作
> 得到**0**11  

為了避免某些字元被無意義的移動，從左到右遍歷s，碰到0，就把他移到左半邊。  
每次移動0，只要移動到第一個**非0的位置**，這樣最省步驟。  

時間複雜度O(N)。  
空間複雜度O(1)。  

```python
class Solution:
    def minimumSteps(self, s: str) -> int:
        ans=0
        i0=0
        for i,c in enumerate(s):
            if c=="0":
                ans+=i-i0
                i0+=1
        
        return ans
```

提供另一種思考方法。  

當s=11010，要把第一個0移到左邊，需要越過兩個1，然後變成01110。  
01110要把第二個0移到左邊，又要越過三個1，最後變成00111。  

每次移動0，移動次數就是左方1的個數。  

時間複雜度O(N)。  
空間複雜度O(1)。  

```python
class Solution:
    def minimumSteps(self, s: str) -> int:
        ans=0
        cnt1=0
        for i,c in enumerate(s):
            if c=="0":
                ans+=cnt1
            else:
                cnt1+=1
        
        return ans
```
