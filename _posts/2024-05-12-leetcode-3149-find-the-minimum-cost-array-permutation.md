---
layout      : single
title       : LeetCode 3149. Find the Minimum Cost Array Permutation
tags        : LeetCode Hard Array DP Bitmask BitManipulation
---
周賽 397。同一場竟然有三題都是 dp，根本 dp 大賽。  

## 題目

輸入陣列 nums，他是陣列 [0, 1, 2, ..., n - 1] 的排列。該排列的分數定義為：  

- score(perm) = \|perm[0] - nums[perm[1]]\| + \|perm[1] - nums[perm[2]]\| + ... + \|perm[n - 1] - nums[perm[0]]\|

回傳**分數最小**的排列。若有多種排列的分數相同，則回傳**字典序**最小者。  

## 解法

這種枚舉選擇順序的題型，大多數都可以用 bitmask dp 解決。  
但 score 關係到**上一個數**是什麼，最後一段的甚至要用到**第一個數**。  
使用額外的變數表示狀態，得到 dp(mask, prev, first)。  

但每個狀態轉移需要枚舉 N 個數，共有 (2^N) \* N^2 個狀態，複雜度是 O((N^3) \* (2^N))。  
代入 N = 14 的計算量大概是 5e7。乍看之下會超時，但是考慮到一些無效的狀態，好像又不會超時，非常神秘。  

---

以下簡稱 perm 為 p。  
仔細觀察 score，發現他是一個**循環**的關係。試著將 nums 也循環移動看看。  
例如：  
> nums = [0, 1]  
> score = abs(p[0] - nums[p[1]]) + abs(p[1] - nums[p[0]])  
> score = abs(0 - 0) + abs(1 - 1)

把 nums 向右移動一格看看：  
> nums = [1, 0]  
> score = abs(p[0] - nums[p[1]]) + abs(p[1] - nums[p[0]])  
> score = abs(1 - 1) + abs(0 - 0)  

絕對值的內容完全一樣，只是出現順序不同罷了。  
也就是說，每種排法都可以任意**平移出現順序**，而不改變分數。  
因題目要求**最小字典序**，所以**第一個數保證是 0**。  

這樣一來狀態就變成 dp(mask, prev)，複雜度降到 O((N^2) \* (2^N))。  
計算量大概是 3e6，直接少掉一個 0。  

---

定義 dp(mask, prev)：以 mask 表示可選數，且上一個數是 prev 時的最大分數。  
轉移：dp(mask, prev) = max(dp(new_mask, j) + abs(prev - nums[j])) FOR ALL 未使用的數 j  
base：當 mask = (2^N) - 1 時，所有數都選完了，要補算 p[N-1] 和 nums[p[0]] 的分數，也就是 abs(prev - nums[0])。  

既然知道第一個數是 0，那答案的入口就是 dp(mask=1, prev=1)。  
記得額外維護每個狀態的轉移來源 fa[mask][prev]，最後從 0 開始填入答案。  

時間複雜度 O((N^2) \* (2^N))。
空間複雜度 O(N \* (2^N))。  

```python
class Solution:
    def findPermutation(self, nums: List[int]) -> List[int]:
        N = len(nums)
        fa = [[-1] * N for _ in range(1 << N)] # track transition source
        
        @cache
        def dp(mask, prev):
            if mask == (1 << N) - 1: # |perm[n - 1] - nums[perm[0]]|
                return abs(prev - nums[0])
            res = inf
            for j in range(N):
                if mask & (1 << j) == 0: # perm[i] = j
                    new_mask = mask | (1 << j)
                    t = dp(new_mask, j) + abs(prev - nums[j])
                    if t < res: # update max score
                        res = t
                        fa[mask][prev] = j
            return res
        
        dp(1, 0) # calc max score and track route
        ans = [0]
        mask = 1
        prev = 0
        while len(ans) < N:
            j = fa[mask][prev]
            ans.append(j)
            prev = j
            mask |= (1 << j)
            
        return ans
```
