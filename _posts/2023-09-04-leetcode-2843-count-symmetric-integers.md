---
layout      : single
title       : LeetCode 2843. Count Symmetric Integers
tags        : LeetCode Easy String Simulation
---
周賽361。

## 題目

輸入兩個正整數low和high。  

若一個整數x由2\*n個數位組成，且前n個數位總和等於後n個數位總和，則稱為**對稱的**。奇數位的數字則不可能是對稱。  

求[low, high]之間有多少個對稱整數。  

## 解法

直接寫一個函數判斷對稱。  
轉成字串後，先判斷奇偶，再把前n個數位扣掉後n個數位，總和0代表對稱。  

時間複雜度O(high log high)。  
空間複雜度O(log high)。  

```python
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        
        def ok(x):
            s=str(x)
            N=len(s)
            if N%2==1:
                return False
            sm=0
            for i in range(N//2):
                sm+=int(s[i])-int(s[N-1-i])
            return sm==0
        
        ans=0
        for i in range(low,high+1):
            if ok(i):
                ans+=1
                
        return ans
```
