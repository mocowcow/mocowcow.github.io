--- 
layout      : single
title       : LeetCode 2786. Visit Array Positions to Maximize Score
tags        : LeetCode Medium Array DP
---
雙周賽109。雖然一眼就知道是dp，但我卻漏掉base case，沒找出錯誤。最後換了一種奇怪的定義才過。  
這題的定義要解釋清楚還真不容易。  

# 題目
輸入整數陣列nums和正整數x。  

起初你位於位置0，而你依照以下規則去訪問其他位置：  
- 如果你位於位置i，則你可以訪問**任何**滿足 i < j 的位置j  
- 每訪問一個新的位置i，你會獲得nums[i]分數  
- 如果位置i和j的**奇偶性**不同，則會損失x分數  

求可以達到的**最高分數**。  

注意：你的初始分數為nums[0]。  

# 解法
非常重要的關鍵：從nums[0]出發，所以一定要選！  

雖然說要跳到nums[i]有0\~i-1這麼多來源，但我們只要維護分數最高那一個就可以。  
而根據奇偶性分類，對於每個位置i來說，也只有0和1兩種狀態。  

定義dp[i][p]：從0出發，最多可以跳到i，且最後位置奇偶性為p時，可得到的最高分數。  
轉移方程式：nums[i]的奇偶性為p，相反的則為q。若跳到nums[i]，不會改變q的最佳答案，nums[i][q]=nums[i-1][q]+nums[i]；  
而卻可以選擇從p或是q跳到nums[i]，所以dp[i][p]=max(dp[i-1][p],dp[i-1][q]-x)+nums[i]  
base cases：只能從nums[0]出發，nums[0]奇偶性p，則dp[0][p]=nums[0]；dp[0][q]=-inf，是不合法的起點。  

dp[N-1][0]代表最後跳偶數最佳結果，dp[N-1][1]代表最後跳奇數最佳結果，取兩者的最大值就是答案。  

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        N=len(nums)
        dp=[[-inf]*2 for _ in range(N)]
        first=nums[0]
        dp[0][first%2]=first
        
        for i in range(1,N):
            val=nums[i]
            p=val%2
            q=p^1
            dp[i][p]=max(dp[i-1][p],dp[i-1][q]-x)+val
            dp[i][q]=dp[i-1][q]
            
        return max(dp[-1])
```

對於每個dp[i]來說，只會參考到上一次的狀態dp[i-1]，所以可以壓縮掉一個維度。  

時間複雜度O(N)。  
空間複雜度O(1)。  

```python
class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        N=len(nums)
        dp=[-inf]*2
        first=nums[0]
        dp[first%2]=first
        
        for i in range(1,N):
            val=nums[i]
            p=val%2
            q=p^1
            dp[p]=max(dp[p],dp[q]-x)+val
            
        return max(dp)
```

最後是比賽時的奇怪做法。  

定義dp(i,p)：對於子陣列nums[i,N-1]，考慮nums[i]選或不選，且上一個奇偶性是p，可能的最大分數。  
轉移方程式：dp(i,p)=max(選, 不選)，不選=dp(i+1,p)；選=dp(i+1,nums[i]%2)+val，若奇偶不相同則要扣掉x  
base case：當i=N時，沒有位置可以選，可得分數為0。  

為了保證nums[0]被選到，以和其相同的奇偶性作為入口，也就是dp(0,nums[0]%2)。  

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        N=len(nums)
        
        @cache
        def dp(i,p):
            if i==N:
                return 0
            val=nums[i]
            notake=dp(i+1,p)
            take=dp(i+1,val%2)+val
            if val%2!=p:
                take-=x
            return max(take,notake)
        
        return dp(0,nums[0]%2)
```