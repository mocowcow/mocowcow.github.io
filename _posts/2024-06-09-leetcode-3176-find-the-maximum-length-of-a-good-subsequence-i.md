---
layout      : single
title       : LeetCode 3176. Find the Maximum Length of a Good Subsequence I
tags        : LeetCode Medium Array DP
---
雙周賽 132。

## 題目

輸入整數陣列 nums 和非負整數 k。  

若一個整數序列 seq 滿足在索引範圍 [0, seq.length - 2] 中，存在**最多 k 個**索引滿足 seq[i] != seq[i + 1]，則稱其為**好的**序列。  

求 nums 的**好的子序列**的最大長度。  

## 解法

經典的**相鄰相關**子序列 dp。  
除了當前第 i 個元素**選或不選**之外，還需要紀錄上次選的元素 prev，以及**相鄰不同**的次數 j。  

定義 dp(i, j, prev)：在 nums[i..N-1] 的子陣列中，找出的最大好的子序列長度，且當前不同次數為 j，前一個元素為 prev。  
轉移：dp(i, j, prev) = max(選, 不選)  

- 選，根據 nums[i] 和 prev 的關係判斷：  
  - 若 prev = -1 或 nums[i] = prev，則 dp(i + 1, j, nums[i]) + 1  
  - 否則若 j < k，則 dp(i + 1, j + 1, nums[i]) + 1  
- 不選：dp(i + 1, j, prev)  

base：當 i = N 時，代表沒元素可選，回傳 0。  

答案入口為 dp(0, 0, -1)。  

時間複雜度 O(N^2 \* k)。  
空間複雜度 O(N^2 \* k)。  

```python
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        N = len(nums)
        
        @cache
        def dp(i, j, prev):
            if i == N:
                return 0
            # no take
            res = dp(i + 1, j, prev)
            # take
            if nums[i] == prev or prev == -1: # same or frist
                res = max(res, dp(i + 1, j, nums[i]) + 1)
            elif j < k: # different
                res = max(res, dp(i + 1, j + 1, nums[i]) + 1)
            return res
        
        ans = dp(0, 0, -1) 
        dp.cache_clear() # prevent MLE
        
        return ans
```
