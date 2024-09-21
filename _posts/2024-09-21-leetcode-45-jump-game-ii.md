---
layout      : single
title       : LeetCode 45. Jump Game II
tags        : LeetCode Medium DP
---
比賽有碰到這題的強化版，趕快來補題解。  

## 題目

輸入長度 n 的整數陣列 nums。你最初位於 nums[0]。  

每個元素 nums[i] 代表你最多可以從 i 跳躍的步數。  
也就是說，若你位於 nums[i]，則可以跳到任意 nums[i + j]，滿足：  

- 0 <= j <= nums[i]  
- 且 i + j < n  

求跳到 nums[n - 1] 所需的**最小步數**。  
題目保證一定能抵達 nums[n - 1]。  

## 解法

不同的跳躍順序，有可能跳到同一個位置上，有**重疊的子問題**，因此考慮 dp。  

定義 dp(i)：從 nums[i] 跳到 nums[N-1] 的最小步數。  
轉移： dp(i) = min(dp(j) + 1) FOR ALL i < j <= min(N-1, i+j)。  
base：當 i = N-1 時，抵達終點，答案為 0。  

答案入口為 dp(0)，即從 nums[0] 出發。  

時間複雜度 O(N \* MX)，其中 MX = max(nums)。  
空間複雜度 O(N)。  

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        
        @cache
        def dp(i):
            if i == N-1:
                return 0
            res = inf 
            for j in range(i+1, min(i+nums[i], N-1) + 1):
                res = min(res, dp(j) + 1)
            return res

        return dp(0)
```
