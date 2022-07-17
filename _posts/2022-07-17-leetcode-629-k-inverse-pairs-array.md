--- 
layout      : single
title       : LeetCode 629. K Inverse Pairs Array
tags        : LeetCode Hard DP
---
每日題。這題比今天整個周賽都還要難，搞了半天還是沒搞懂怎麼優化的，最後抄了個答案。  

# 題目
對於整數陣列nums來說，**逆對**指的是一對整數[i, j]，符合0<=i<j<nums.length，且nums[i]>nums[j]。  

輸入兩個整數n和k，求由1到n所組成，且正好有k個**逆對**的陣列數量。答案可能很大，先模10^9+7後回傳。  

# 解法
看到n和k上限是都1000，心裡大概有個底，需要O(n\*k)的演算法。但我怎麼想也只想得出O(n\*k^2)，當然是TLE。  

先列出幾個基本情況：  
- n=0時，不是合法的長度，回傳0  
- k=0時，只有完全遞增一種排法，回傳1  
- k<0時，逆對不可為負數，回傳0  

否則對於長度n的陣列來說，有n-1個位置可以插入新的數字來使k值減少。  
例：  
> [1,2,3]要插入4  
> [1,2,3,**4**]可以使k減少0  
> [1,2,**4**,3]可以使k減少1  
> [1,**4**,2,3]可以使k減少2  
> [**4**,1,2,3]可以使k減少3  

對所有可以插入的位置可能數加總後回傳。  

```python
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD=10**9+7
        
        @cache
        def dp(n,k):
            if n==0:
                return 0
            if k==0:
                return 1
            if k<0:
                return 0
            ans=0
            for i in range(n):
                ans=(ans+dp(n-1,k-i))%MOD
            return ans
            
        return dp(n,k)
```
