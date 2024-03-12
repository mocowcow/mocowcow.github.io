--- 
layout      : single
title       : LeetCode 2478. Number of Beautiful Partitions
tags        : LeetCode Hard String DP
---
周賽320。本來用python寫個O(k\*N^2)的dp解，可能沒睡醒才覺得又是py時間太嚴格，一氣之下跑去用go寫一次就過了。後來想想才發現不對，O(k\*N^2)將近10^9次運算，再怎樣都不會是正確答案，看來是golang執行快到一個誇張。  

# 題目

輸入一個只包含字元'1'\~'9'的字串s，以及兩個整數k和minLength。  

一個**美麗的分割方式**必須符合一下條件：  

- s必須分割成k個沒有交集的子字串  
- 每個子字串長度至少為minLength  
- 每個子字串必需要以**質數**開頭，以**非質數**結尾  

只有'2', '3', '5'和'7'是質數，其餘為非質數。  

求s有多少**美麗的分割方式**。答案很大，先模10^9+7後回傳。  

# 解法

自己還真想不出如何壓縮到O(Nk)，大部分的人都用bottom up，不太好理解，最後總算找到一個比較合電波的[top down題解](https://leetcode.com/problems/number-of-beautiful-partitions/discuss/2833126/C%2B%2B-Python-Short-DP-explained)。  

定義dp(i,k,is_start)：從索引i開始的s的子字串，要再拆分成k個子字串的拆分方法數。is_start代表i是否為子字串的開頭，若為真則s[i]必需要是質數。  
轉移方程式很難寫，依照我自己的理解將順序稍微整理一下：  

1. 若i是開頭
    - s[i]不為質數則不合法，回傳0  
    - 否則向後跳minLength-1個索引，使得子字串滿足長度  
2. 若i不是開頭  
    - 把s[i]歸到當前子字串，而i+i開始的子字串一樣需要分割成k塊  
    - 若s[i]不是質數，則可以當作結尾。答案加上以i+1開始的子字串分割成k-1塊的方法數  

base cases：  

- 當i=N時，如果k也為0，代表成功分割，回傳1；否則代表分割的子字串數量不夠，回傳0  
- 當i>N時，為非法的分割點，回傳0  
- 當k=0但i<N，已經分割成k塊，但還有剩餘字元沒有用到，為非法分割，回傳0  

is_start只有兩種狀態，可以當作常數。每個子問題最多轉移兩次，也當常數，所以時空間複雜度都是O(NK)。  

```python
class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        MOD=10**9+7
        N=len(s)
        prime=set("2357")
        
        @cache
        def dp(i,k,is_start):
            if i==N:return int(k==0)
            if i>N:return 0
            if k==0:return 0
            if is_start:
                if s[i] not in prime:return 0
                # append s[i] until length enough
                return dp(i+minLength-1,k,False)
            else:
                # append s[i]
                ans=dp(i+1,k,False)
                # end with s[i] and split new substring
                if s[i] not in prime:
                    ans=(ans+dp(i+1,k-1,True))%MOD
                return ans
        
        return dp(0,k,True)
```

補充另一種更通用的劃分型 dp 解法。  
對於當前陣列 s[i..]，枚舉**合法的分割點** j，並從 j+1 繼續分割。  

定義 dp(i, z)：從子陣列 nums[i..N-1] 中，求出 z 個不相交子陣列的最大值。  
轉移：dp(i, need_grp) = max( dp(j+1, z-1 )...) FOR ALL i+minLength-1 <= j < N  
BASE：當 i = N 時，若同時滿足 z = 0 代表正好分割完 k 個，回傳 1；否則不合法，回傳 0。  

時間複雜度 O(N^2 \* k)。  
空間複雜度 O(Nk)。  

這樣會超時，需要進一步優化。  

```python
prime = set("2357")
MOD = 10**9 + 7

class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        N = len(s)
        
        # first char must be prime
        if s[0] not in prime:
            return 0
        
        # last char must not be prime
        if s[-1] in prime:
            return 0
        
        def is_end(j):
            return s[j] not in prime and (j+1 == N or s[j+1] in prime)

        @cache
        def dp(i, z):
            if i == N and z == 0:
                return 1
            if i == N:
                return 0
            res = 0
            for j in range(i+minLength-1, N):
                if is_end(j):
                    res += dp(j+1, z-1)
            return res % MOD
        
        return dp(0, k)
```
