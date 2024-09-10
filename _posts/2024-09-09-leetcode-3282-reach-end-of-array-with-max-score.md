---
layout      : single
title       : LeetCode 3282. Reach End of Array With Max Score
tags        : LeetCode Medium Greedy DP
---
weekly contest 414。  
感覺最近常常出這種直覺秒殺題，如果認真思考反而會掉入陷阱。  

## 題目

輸入長度 n 的整數陣列 nums。  

你必需從索引 0 出發並抵達索引 n - 1。  
你只能跳到比當前**更大**的索引。  

從索引 i 跳到索引 j 獲得的**分數**為 (j - i) \* nums[i]。  

求抵達最後一個索引的**最大總分**。  

## 解法

先講講錯誤的思考方向。  

對於每個點 i 都可以跳到更大的 j 去，然後再從 j 繼續跳。  
不同的跳法都有可能跳到同一個 j 點，有**重疊的子問題**，因此考慮 dp。  

定義 dp(i)：從 i 跳到 n-1 的最大總分。  
轉移：dp(i) = max(dp(j) + (j-i) \* nums[i]) FOR ALL i < j < n。  
base：當 i = n-1 時，抵達終點，答案為 0。  

但複雜度是 O(N^2)，對於 N = 1e5 會超時。  

```python
class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        N = len(nums)

        @cache
        def dp(i):
            if i == N - 1:
                return 0
            res = 0
            for j in range(i + 1, N):
                res = max(res, dp(j) + (j - i) * nums[i])
            return res

        return dp(0)
```

本來以為是需要什麼 dp 優化技巧，想半天都沒想出來，沒辦法把轉移的 O(N) 消掉。  
該換個角度去思考看看。  

若真的可以 dp 優化，希望知道的同學能告訴我。  

---

仔細研究分數的公式：  
> (j - i) \* nums[i]  

他所隱含的意思是**跳幾步就得幾個 nums[i] 分**。  
換句話說，只要找到第一個比 nums[i] 更大的 nums[j]，那麼去了 nums[j] 之後能得更多分。  
注意：最後一個位置 nums[N-1] 需要特判，無論大小都必需跳。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        N = len(nums)
        ans = 0
        i = 0
        for j in range(N):
            if nums[j] > nums[i] or j == N - 1:
                ans += (j - i) * nums[i]
                i = j

        return ans
```

用另外一種角度思考，j 可以從最大的 nums[i] 跳過來。  
所以只需要維護 nums[i] 的**前綴最大值**即可。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        ans = 0
        mx = 0
        for x in nums:
            ans += mx
            mx = max(mx, x)
            
        return ans
```
