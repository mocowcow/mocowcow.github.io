---
layout      : single
title       : LeetCode 2902. Count of Sub-Multisets With Bounded Sum
tags        : LeetCode Hard Array DP Math
---
雙周賽115。花了好多天才搞懂，這題細節也不少。  

## 題目

輸入非負整數陣列nums，還有兩個整數l和r。  

求nums有多少**子多重集合**，其子集元素總和正好落在區間[l, r]中。  
答案很大，先模10^9+7後回傳。  

**子多重集合**指的是一個**無序**的元素集合，其中元素x最多可以出現occ[x]次，而occ[x]是x在nums中的出現次數。  

注意：  

- 若兩個子多重集合排序後相同，則視為同個子多重集合
- **空**集合的總和為0  

## 解法

**子多重集合**看起來很囉嗦，其實就是多重背包問題。  
元素x有cnt[x]個，看你要選幾個，最後求總和落在[l, r]中的選法有幾種。  

這題測資範圍很奇妙，說nums長度上限2\*10^4，然後S=sum(nums)和max(nums)上限也都是2\*10^4。  
只有在nums[i]全部都是1或0或2的情況下，才能達到nums的長度上限。  
那如果nums[i]的元素全都是不同的，必須滿足1+2+...+a <= sum(nums)，能有sqrt(sum(nums))種，大概是一百多。  

樸素版本的多重背包問題很簡單就能寫出來。  

定義dp(i,j)：在剩餘前i種元素時，湊出總和為j的選法有幾種。  
轉移方程式：dp(i,j) = sum( dp(i-1,j-k\*x) FOR ALL 0<=k<=cnt)，其中k\*x不可超過j。  
base case：當i<0時，沒有剩餘元素可選，只有空集合一種選擇。如果總和要求j剛好為0，答案為1；否則不合法，回傳0。  

共有min(sqrt(S),N)種元素，總和有min(S,r)種。每個狀態轉移最多N次。  
時間複雜度O(min(sqrt(S),N) \* min(S,r) \* N)。  
空間複雜度O(min(sqrt(S),N) \* min(S,r))。  

計算量隨隨便便都10^8，嚴重TLE。  

```python
class Solution:
    def countSubMultisets(self, nums: List[int], l: int, r: int) -> int:
        MOD=10**9+7
        d=Counter(nums)
        keys=list(d)
        N=len(d)
        
        @cache
        def dp(i,j):
            if i<0:
                return int(j==0)
            res=0
            x=keys[i]
            for k in range(d[x]+1):
                if x*k>j:
                    break
                res+=dp(i-1,j-x*k)
            return res%MOD
     
        ans=0
        for i in range(l,r+1):
            ans+=dp(N-1,i)

        return ans%MOD
```
