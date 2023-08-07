---
layout      : single
title       : LeetCode 2811. Check if it is Possible to Split Array
tags        : LeetCode Medium Array DP PrefixSum
---
周賽357。最近Q2出dp頻率越來越高，而且這題還不少小細節。  

## 題目

輸入長度n的陣列nums，還有整數m。  
你必須判斷能否將nums分割成n個**非空**陣列。  

每次操作，你必須選擇一個現有陣列(有可能是之前分割出的)，其**長度至少為2**，將其分割成兩個子陣列。而分割出的每個子陣列至少需要滿足以下**任一**條件：  

- 子陣列長度為1  
- 子陣列元素和大於等於m  

若能分割成n個陣列則回傳true，否則回傳false。  

## 解法

長度n的陣列要分割成n個，也就是每個元素都要自成一戶。  

定義dp(i,j)：nums[i,j]能不能合法分割。  
轉移方程式：只要存在介於[i,j-1]之間的索引k，滿足dp(i,k)和dp(k+1,j)，則為true；否則為false。  
base cases：若i=j，代表長度1子陣列，為true；若子陣列長度大於1且總和不足m，回傳false。  

但是題目是說**分割出**的子字串要滿足條件，所以初始nums的總和不足m也沒關係。 例如：  
> nums = [1,1], m = 3  
> 答案true  

所以我枚舉n-1個分割點k，將nums分割成nums[0,k] + nums[k+1,N-1]兩部分。只要兩個都是true，代表可以分割。  
若nums長度為1，不存在分割點，但本身就是合法的，記得特殊判定。  

求nums[i,j]總和可以預處理前綴和，雖然不會降低複雜度，但應該會稍微快一些。  

dp有兩種狀態，i和j分別有N種。每個狀態需要轉移N次。  
時間複雜度O(N^3)。  
空間複雜度O(N^2)。  

```python
class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        N=len(nums)
        
        if N==1:
            return True
        
        ps=list(accumulate(nums,initial=0))
        
        @cache
        def dp(i,j):
            if i==j:
                return True
            
            sm=ps[j+1]-ps[i]
            if sm<m:
                return False
            
            for k in range(i,j):
                if dp(i,k) and dp(k+1,j):
                    return True
            return False
        
        for k in range(0,N-1):
            if dp(0,k) and dp(k+1,N-1):
                return True
            
        return False
```
