--- 
layout      : single
title       : LeetCode 2575. Find the Divisibility Array of a String
tags        : LeetCode Medium String Math
---
周賽334。把word.length<=10^5看成word<=10^5，吃一發WA，好慘。  

# 題目
輸入由n個數字組成的的字串word，還有正整數m。  

div是word的**可除性陣列**，長度為n，且符合：  
- 如果word[0,..,i]的的子字串轉成數字後可被m整除，則div[i] = 1  
- 否則div[i] = 0  

回傳word的**可除性陣列**。  

# 解法
我們要在某個值val後面加上新的數字n，這個動作就是val*10+n。  
初始化val為0，遍歷word中每個數字c，將c加到val尾端後檢查是否能被m整除，可以則為1；否則為0。  

但是word中最多10^5個數字，很快就會使val溢位。  

以例題二來看：  
> word = "1010", m = 10  
> 1%10==1, div[0]=0  
> 10%10==0, div[1]=1  
> 101%10==1, div[2]=0  
> 1010%10==0, div[3]=1  

1除10時=0餘1，之後不管**商數0**變成多少倍，一定都可以被m整除，因此只要保留餘數做處理。  
> word = "1010", m = 10  
> 1%10==1, r=1, div[0]=0  
> 10%10==1, r=0, div[1]=1  
> 1%10==1, r=1, div[2]=0  
> 10%10==0, r=0, div[3]=1 

時間複雜度O(N)。忽略答案陣列，空間複雜度O(1)。  

```python
class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        ans=[]
        val=0
        
        for c in word:
            val=(val*10+int(c))%m
            if val%m==0:
                ans.append(1)
            else:
                ans.append(0)
                
        return ans
```
