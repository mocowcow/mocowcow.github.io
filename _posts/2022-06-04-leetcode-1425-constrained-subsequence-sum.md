--- 
layout      : single
title       : LeetCode 1425. Constrained Subsequence Sum
tags        : LeetCode Hard Array DP SlidingWindow
---
又是隨便抽到的DP，只有推出狀態轉移，但是不知道怎麼優化，看來要化簡轉移還是有點難度。

# 題目
輸入整數陣列nums和整數k，回傳nums**非空**子序列的最大和，且子序列中的每兩個連續整數nums[i]和nums[j]，兩者索引距離不得超過k。  

# 解法
先講一開始的TLE版本。  
試著以每個數字nums[i]，接下來可以選擇num[i+1]\~num[i+k]中的最佳解做為下一個數字。  

定義dp(i)：以nums[i]為起點所能得到的最大和  
轉移方程式：dp(i)=nums[i]+max(0,dp(j) FOR ALL i<j<=i+k)  
base case：當i為nums中最後一個數時，dp(N-1)=nums[N-1]  

但是k跟N最大會到10^5，所以O(N*K)時間是沒辦法過的，必須想辦法化簡。  

```python
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        N=len(nums)
        
        @cache
        def dp(i):
            best=0
            for j in range(i+1,i+k+1):
                if j==N:
                    break
                best=max(best,dp(j))
            return nums[i]+best
        
        return max(dp(i) for i in range(N))
```

看看提示說用queue來優化，多翻了幾篇文章才搞懂意思。  
簡單來說就是維護一個單調遞減佇列q，而q的第一個元素永遠是在k距離中的最佳解。  

改從尾端進行bottom up，從後方往前對每個數字nums[i]做DP：  
每次先將超出k距離的候選人pop掉，然後取最佳解q[0]更新dp[i]的值，將佇列尾端小於dp[i]的值移除，最後將i放入佇列末端。  
回傳dp中最大者就是答案。  

```python
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        N=len(nums)
        dp=[0]*N
        q=deque()

        for i in range(N-1,-1,-1):
            while q and q[0]-i>k:
                q.popleft()
            best=dp[q[0]] if q else 0
            dp[i]=max(best,0)+nums[i]
            while q and dp[i]>=dp[q[-1]]:
                q.pop()
            q.append(i)
            
        return max(dp)
```