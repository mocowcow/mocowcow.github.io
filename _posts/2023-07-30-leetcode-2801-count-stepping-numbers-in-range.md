--- 
layout      : single
title       : LeetCode 2801. Count Stepping Numbers in Range
tags        : LeetCode Hard String DP
---
周賽356。第一眼就知道是數位dp，意外的是做出來的人竟然不多，明明前幾次才考過。  
相似題[2719. count of integers]({% post_url 2023-06-06-leetcode-2719-count-of-integers %})。  

## 題目

輸入兩個正整數字串low和high，找到有多少**步進數**介於閉區間[low, high]之間。  

若一個整數，其所有相鄰數位絕對差都正好是1，則稱為**步進數**。  

求有多少**步進數**介於閉區間[low, high]。答案很大，先模10^9+7後回傳。  

注意：**步進數**不可以有前導零。  

## 解法

f(x)代表[low, high]間的步進數的個數。  
要找[low, high]間的步進數，先求出f(high)再扣掉f(low-1)。  
但是有些語言不方便對字串數字進行修改，可以改f(high) - f(low)，然後單獨判定low是否為步進數。  

定義dp(i,is_limit,is_num,prev)：前一個數選prev的情況下，從i\~N-1共有幾種步進數。  
is_limit代表當前數字是否受限於s[i]；而is_num代表是否已經是有效數字。  
轉移方程式：如果is_num為false，代表左方數字都是0，這時候隨便選什麼都可以；否則只能選擇prev+1或是prev-1，如果is_limit為true，還不可以超過s[i]。  
base cases：當i=N時，已經沒東西可選。如果is_num為true，代表前方選的數有效，可以和空字串組成答案，回傳1；否則回傳0。  

雖然有四個狀態，但是is_limit和is_num都只有兩種情形，可以忽視。  
i共有N種，prev最多10種。每個狀態轉移10次。  
時間複雜度O(N \* D^2)，其中N為high長度，D為10種數字。  
空間複雜度O(N \* D)。  

```python
class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        MOD=10**9+7
        
        def f(s):
            N=len(s)

            @cache
            def dp(i,is_limit,is_num,prev):
                if i==N:
                    return int(is_num)
                up=int(s[i]) if is_limit else 9
                down=0 if is_num else 1
                ans=0
                if not is_num:
                    ans=dp(i+1,False,False,prev)
                for j in range(down,up+1):
                    if not is_num or abs(j-prev)==1:
                        new_limit=is_limit and j==up
                        ans+=dp(i+1,new_limit,True,j)
                return ans%MOD

            return dp(0,True,False,0)

        
        ans=f(high)-f(low)
        ok=True
        for a,b in pairwise(low):
            if abs(ord(a)-ord(b))!=1:
                ok=False
                break
        
        if ok:
            ans+=1
            
        return ans%MOD
```
