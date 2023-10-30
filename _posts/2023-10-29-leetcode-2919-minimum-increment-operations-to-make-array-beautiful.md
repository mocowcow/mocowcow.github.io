---
layout      : single
title       : LeetCode 2919. Minimum Increment Operations to Make Array Beautiful
tags        : LeetCode Medium Array DP
---
周賽369。

## 題目

輸入長度n的整數陣列nums，還有一個整數k。  

你可以執行以下**增量**操作**任意次**：  

- 選擇介於[0, n-1]的索引i，並使得nums[i]增加1  

若一個陣列中，所有長度大於等於3的子陣列的**最大值**都超過至少k，則稱為**美麗的**。  

求使得nums成為**美麗的陣列**所需的最少操作次數。  

## 解法

長度為size的子陣列必定包含長度size-1的子陣列，故只要保證所有長度為3的子陣列的最大值都至少k。  

對於大小為3，且右端點i的子陣列，在[i-2, i-1, i]三者之間任意一個滿足k即可。  
換個角度說，只要nums[i]滿足了k，那麼接下來的i+1和i+2都可以不用增量。  

本想貪心的滿足第一個需要增量的索引i，但是發現以下例子不合法：  
> nums = [4,0,1,0], k = 5  
> 使nums[0]增量1，[5,0,1]滿足k  
> 但[0,1,0]不合法，需要增量  
> 使nums[2]增量4，[0,5,0]滿足k  
> 共增量5次  

但最佳答案應是直接在nums[2]增量4。  
發現nums[i]並沒有一定的標準決定增量或不增量，因此朝dp去考慮。  
每當nums[i]滿足k，則接下來兩個索引可以**免費**選擇不增量的。  

定義dp(i,free)：當前還有free次不增量的機會，使得子陣列nums[i, N-1]美麗的最小操作次數。  
轉移方程式：dp(i,free) = min( dp(i+1,free-1), dp(i+1,2)+cost )，其中cost為使nums[i]變成k的成本。  
base cases：當free次數小於0，操作次數不足，回傳inf；若i=N，則所有子陣列都處理完，回傳0。  

根據定義，dp(i,free)是以i為子陣列右邊界。所以對於子陣列nums[0,2]來說，只要nums[2]滿足k即可。  
但在nums = [1,0,0], k = 2的例子中，選擇nums[0]增量明顯是更好的選擇，因此前三項都有可能作為起點。  

時間複雜度O(N)，將子陣列長度3視為常數。  
空間複雜度O(N)。  

```python
class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        N=len(nums)
        
        @cache
        def dp(i,free):
            if free<0:
                return inf
            if i==N:
                return 0
            cost=max(0,k-nums[i])
            res=cost+dp(i+1,2) # take
            res=min(res,dp(i+1,free-1)) # no take
            return res
        
        ans=inf
        for i in range(3):
            ans=min(ans,dp(i,0))
            
        return ans
```

改寫成遞推版本。  

```python
class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        N=len(nums)
        dp=[[inf]*3 for _ in range(N+1)]
        for free in range(3):
            dp[N][free]=0
        
        for i in reversed(range(N)):
            for free in range(3):
                cost=max(0,k-nums[i])
                res=cost+dp[i+1][2] # take
                if free>0: # no take
                    res=min(res,dp[i+1][free-1])
                dp[i][free]=res
                
        ans=inf
        for i in range(3):
            ans=min(ans,dp[i][0])
            
        return ans
```

上面的dp(i,free)定義是有幾次**不增量的機會**。還有其他定義方式。  

定義dp(i,step)：使得nums[0,i]子陣列美麗的最小增量次數，且nums[i+step]處不滿足k。  
轉移方程式：dp(i,step) = min( dp(i-1,step)+cost, dp(i-1,step+1) )  
base cases：當step>=3，已經無法變得美麗，回傳inf；當i<0，陣列處理完畢，回傳0。  

遞迴的入口只剩下一個dp(N-1,0)，比起前一種定義好像方便不少。  

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        N=len(nums)
        
        @cache
        def dp(i,step):
            if step>=3:
                return inf
            if i<0:
                return 0
            cost=max(0,k-nums[i])
            res=dp(i-1,0)+cost # take
            res=min(res,dp(i-1,step+1)) # no take
            return res
        
        return dp(N-1,0)
```

改成遞推版本。  

```python
class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        N=len(nums)
        dp=[[0]*3 for _ in range(N+1)]
        
        for i,x in enumerate(nums):
            for step in range(3):
                cost=max(0,k-x)
                res=dp[i][0]+cost
                if step<2:
                    res=min(res,dp[i][step+1])
                dp[i+1][step]=res
        
        return dp[N][0]
```

每個dp[i]只會參考到dp[i-1]，可以使用滾動陣列，只保留上一次結果。  
反正也只有0,1,2三種距離，直接寫成變數更方便。  

只需要常數空間，而且運行時間只需要其他版本的50%不到，非常簡潔有力。  

時間複雜度O(N)。  
空間複雜度O(1)。  

```python
class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        dp0=dp1=dp2=0
        for i,x in enumerate(nums):
            cost=max(0,k-x)
            take=dp0+cost
            dp0=min(take,dp1)
            dp1=min(take,dp2)
            dp2=take
            
        return dp0
```
