---
layout      : single
title       : LeetCode 2864. Maximum Odd Binary Number
tags        : LeetCode Easy Array String Greedy
---
周賽364。

## 題目

輸入**二進位**字串s，其中至少包含一個'1'。  

你必須將這些位元**重排列**，使得其成為可能的**最大奇數**。  

回傳重排列後的最大奇數二進位字串。  

注意：字串可以擁有前導零。  

## 解法

二進位每個位元所代表的是1, 2 ,4 ...，只要第一個位元是1，則這個數字一定是奇數。  
題目保證至少有一個1，所以先把第一個位元填上1。  

假設長度N的字串中有one個1，有一個要填到最後面。剩下one-1個，還有zero = N-one個0要填。  
為了使數值較大，則優先把剩下的1都填到左邊，剩下的0放中間。  

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        N=len(s)
        one=s.count("1")
        zero=N-one
        
        one-=1
        
        return "1"*one + "0"*zero +"1"
```

也可以先建立長度N的陣列，初始都是0。  
填上最右邊的1，然後從左邊開始填剩下的1。  

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        N=len(s)
        a=["0"]*N
        a[-1]="1"
        
        for i in range(s.count("1")-1):
            a[i]="1"
            
        return "".join(a)
```
