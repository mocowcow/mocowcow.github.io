--- 
layout      : single
title       : LeetCode 2443. Sum of Number and Its Reverse
tags        : LeetCode Medium String
---
周賽315。也是很鳥的題目，鳥到我感覺其中有詐，其實並沒有。然後我自己粗心吃一個WA。  

# 題目
輸入一個非負整數num，如果num可以由為任何非負整數及其倒數所組成，則回傳true，否則回傳false。  

例如443可以由172+271組成；或是181可以由140+041組成。  

# 解法
一開始被181=140+041這個例題騙到，一直想41要怎麼倒成140，浪費半天。其實最後掃到140就會倒成041，根本不用管他。  
直接窮舉0\~num的所有數字n，直接拿n和其倒數相加，檢查是否為num。  

nums最多10^5，有6個位數，將整數轉成字串需要6次運算，時間複雜度O(N\*6)。空間複雜度O(1)。  

```python
class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for n in range(num+1):
            if n+int(str(n)[::-1])==num:
                return True
        
        return False
```

不使用字串反轉的寫法，但是有時會TLE，真的是python悲劇，像是java和go都沒事。推測那堆按爛的都是python受害者。  

```python
class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for n in range(num+1):
            r=0
            x=n
            while x:
                r=r*10+x%10
                x//=10
            if n+r==num:
                return True
        
        return False
```