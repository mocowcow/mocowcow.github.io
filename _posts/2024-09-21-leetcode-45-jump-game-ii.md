---
layout      : single
title       : LeetCode 45. Jump Game II
tags        : LeetCode Medium DP BFS
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

改成遞推寫法。  

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        f = [inf] * N
        f[-1] = 0
        for i in reversed(range(N-1)):
            for j in range(i+1, min(i+nums[i], N-1) + 1):
                f[i] = min(f[i], f[j] + 1)
        
        return f[0]
```

另外一種思路是 BFS。  
從 0 開始跳，紀錄每個索引第一次抵達時花了幾步。  

時間複雜度 O(N \* MX)，其中 MX = max(nums)。  
空間複雜度 O(N)。  

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        dist = [-1] * N
        q = deque()
        q.append(0)
        step = 0
        while q:
            for _ in range(len(q)):
                i = q.popleft()
                if dist[i] != -1: # visited
                    continue

                dist[i] = step
                for j in range(i+1, min(i+nums[i], N-1) + 1):
                    q.append(j)
            step += 1

        return dist[-1]
```
