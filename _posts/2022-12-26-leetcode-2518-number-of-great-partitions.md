--- 
layout      : single
title       : LeetCode 2518. Number of Great Partitions
tags        : LeetCode Hard Array DP
---
周賽325。又死在DP上，只能想到O(k^2\*N)的方法，當然是沒過。開始懷疑我是不是真的會DP。  

# 題目
輸入由**正整數**組成的陣列nums，以及正整數k。  

將陣列**分割**成兩個有序的**組別**，令每個元素恰好屬於其中一組。若兩組別的元素和都大於等於k，則稱其為**好的分割**。  

求**不同**的**好分割**數量，答案可能很大，先模10^9+7後回傳。  

若有兩種分割方式，其中nums[i]被分到不同的組別，則視為**不同的分割**。  

# 解法
將nums分成兩組，其實可以看做01背包問題：拿的話就放在A組，不拿就放在B組。兩組總和都超過k就是**好的分割**。  
但是nums[i]非常大，隨便都超過k，非常難算。乾脆反過來找**不好的分割**，用總分割數扣掉不好的分割就是答案。  

設nums總和為sm，若兩組總和都要超過k，則sum必須大於等於k*2；否則一個都不可能成功，答案為0。  
對於每個nums[i]只有拿或不拿兩種選擇，分割總共有2^N種方式。  

首先找到所有總和小於k的分割方式，定義dp[i][j]：總和為j的分組方式。  
轉移方程式：dp[i][j]=dp[i-1][j]+dp[i-1][j-nums[i]]  
base case：完全不拿也是一種選擇，dp[0][0]=1  

因為每次疊代新的元素之後，只會參考到上一次的DP結果，所以可以壓縮成一維陣列。  

時間複雜度O(Nk)。空間複雜度O(k)。  

```python
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD=10**9+7
        N=len(nums)
        
        if sum(nums)<k*2:return 0
        
        dp=[0]*k
        dp[0]=1
        for n in nums:
            for i in reversed(range(k)):
                if i>=n:
                    dp[i]=(dp[i]+dp[i-n])%MOD

        return (pow(2,N,MOD)-sum(dp)*2)%MOD
```
