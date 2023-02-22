--- 
layout      : single
title       : LeetCode 2572. Count the Number of Square-Free Subsets
tags        : LeetCode Medium Array BitManipulation Bitmask DP HashTable
---
周賽333。這題有夠難，根本是hard等級的，最近真的越來越誇張。  

# 題目
輸入正整數陣列nums。  

如果nums的一個子集合的乘積是**無平方因子數**，則該子集合為**無平方子集**。  

**無平方因子數**指的是不能被1以外的**平方數**所整除的整數。  

求nums總共有多少**非空**子集合是**無平方子集**。答案可能很大，先模10^9+7後回傳。  

# 解法
題目要的是**子集乘積**不可被1以外的平方數整除，這句話其實等價於**每個質因數只能出現一次**。  

而nums[i]最大為30，所以質因數p只會有[2,3,5,7,11,13,17,19,23,29]共十種。這些質因數的**冪集**共有2^n種集合，扣掉空集合剩下(2^n)-1個。  

我們可以把每個質因數映射到不同的位元上，以bitmask表示那些質因數出現過。如"1101"代表子集[2,3,7]。  
之後靠dp求出各組合出現的次數，一邊計算一邊更新答案。但有些數字一開始就有重複的質因數，如[4,8,12,25]等，需要特別判定不處理。  

維護雜湊表dp，表示各組合出現次數，並初始化dp[0]=1，因為空集合永遠只有一種。  
遍歷nums中的數字n，若合法則遍歷已出現過的組合k，若n與k沒有共通的質因數，則n可以和所有的k組成dp[k]個新的子集合，將dp[k]加入答案。為避免重複計算，要等處理完所有組合k後，再將新產生的組合加回dp中。  

質數有P=10種，共2^P種組合，每次處理nums[i]都需要遍歷，時間複雜度O(N \* 2^P)。dp只需要兩個雜湊表保存所有組合，空間複雜度O(2^P)。  

```python
class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        MOD=10**9+7
        p=[2,3,5,7,11,13,17,19,23,29]
        
        def ok(n):
            for x in [4,9,16,25]:
                if n%x==0:
                    return False
            return True
        
        dp=Counter()
        dp[0]=1
        ans=0
        
        for n in nums:
            if not ok(n):continue
            t=Counter()
            mask=0
            for i in range(len(p)):
                if n%p[i]==0:
                    mask|=(1<<i)
                    
            for k,v in dp.items():
                if not mask&k:
                    t[mask|k]+=v
                    ans=(ans+v)%MOD
            dp+=t
                
        return ans
```
