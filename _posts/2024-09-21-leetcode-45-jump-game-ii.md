---
layout      : single
title       : LeetCode 45. Jump Game II
tags        : LeetCode Medium DP BFS Greddy
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

把 dist 陣列打印出來看，會發現他是呈現**嚴格遞增**的。  
長的類似這樣：[0,1,1,1,2,2,3,3,3,..]。  

這些相鄰的數字可以看做是**特定步數可抵達的範圍**。  
似乎暗示著每次跳躍都會**向右擴展**可達範圍？  

---

仔細研究看看範例 1：  
> nums = [2,3,1,1,4]  

在最初跳 0 步時，可能的起跳位置只有 0。  
從 0 起跳，只有跳到 [1, 2] 兩個選擇。  

- 方案一：跳到 1，則第二步可以從 1 跳到 [2,4]。  
- 方案二：跳到 2，則第二步只能從 2 跳到 [3,3]。  

方案二能抵達的地方，方案一全部也都能抵達，甚至能跳更遠。因此方案一優於方案二。  
也就是說，要貪心地選擇**讓下次跳更遠的位置**。  

---

維護變數 next_r，代表**下次能跳的最遠的位置**。  
枚舉當前步數的可能起跳位置 [l,r] 間的所有點 i，以 i + nums[i] 更新 next_r。  
然後步數加 1，更新起跳區間為 [r+1, next_r]。  

最初只可能位於 nums[0]，故初始化 l = r = 0。  
重複上述步驟直到可達終點 N-1 為止。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

注意：本題保證能抵達終點，故不須檢查跳躍失敗的特例。  
否則 next_r <= r 代表無法跳到更遠的位置。  

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        ans = 0
        l = r = 0
        while r < N-1:
            # find best postision
            next_r = 0
            for i in range(l, r + 1):
                next_r = max(next_r, i + nums[i])

            # cannot jump more
            # if next_r <= r:
            #     return -1

            # jump
            ans += 1
            l, r = r + 1, next_r

        return ans
```
