---
layout      : single
title       : LeetCode 3578. Count Partitions With Max-Min Difference at Most K
tags        : LeetCode Medium DP PrefixSum SlidingWindow TwoPointers SortedList
---
weekly contest 453。  
最近難度分數標準大概也壞了，至少絕對不是 5 分中等題。  

## 題目

<https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/description/>

## 解法

看到**劃分**又看到 mod，直覺就是劃分型 dp。  

每次從 nums 最左邊切掉一段，得到更小的子陣列。  
不同的切法可能得到相同的剩餘結果，有**重疊的子問題**，考慮 dp。  

定義 dp(i)：將 nums[i..] 分割成若干個極值差不超過 k 的子陣列，所需最小分割次數。  
轉移：dp(i) = sum(dp(j+1) FOR ALL diff(nums[i..j]) <= k)  
base：當 i = N，劃分完成，答案 1。  

對於每個 dp(i)，枚舉右端點 j 並維護最大最小值，若滿足限制則將 dp(j+1) 加入答案。  
時間複雜度 O(N^2)。  

```python
@cache
def dp(i):
    if i == N:
        return 1
    mx = -inf
    mn = inf
    res = 0
    for j in range(i, N):
        mx = max(mx, nums[j])
        mn = min(mn, nums[j])
        if mx - mn > k:
            break
        res += dp(j+1)
    return res % MOD

return dp(0)
```

---

對於本題 N = 5e4 來說 O(N^2) 會超時，找找看可以優化的地方。  

注意到子陣列的性質：長度越大，極值差**只增不減**。  
例如以 i 為左端點，最遠的合法右端點可到 j。  
那麼以 i-1 為左端點，最遠的合法右端點也不可能超過 j。而且很可能因為 nums[i-1] 改變了極值，使得右端點左移而小於 j。  

轉移來源 j 是一個連續的區間，隨著 i 變小，j 也只會變小或不變。  
可改成遞推加上前綴和 (滑動窗口) 優化，使 dp(i) 沿用 dp(i+1) 的轉移來源。  

維護右端點 j 以及轉移來源總數 sm。若 nums[i..j] 極值差大於 k 則將 dp(j+1) 刪除，並縮減右端點。  
為了維護 nums[i..j] 的極值，可用 sorted list 或是單調隊列。此處使用前者。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
from sortedcontainers import SortedList as SL

MOD = 10**9 + 7


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        N = len(nums)
        f = [0] * (N+1)
        f[-1] = 1
        sl = SL()  # 窗口內元素，用於求極值差
        j = N-1  # 窗口右端點
        sm = 0  # 轉移來源總數
        for i in reversed(range(N)):
            sl.add(nums[i])
            sm += f[i+1]
            while sl[-1] - sl[0] > k:  # 極值差過大，縮減右端點
                sm -= f[j+1]
                sl.remove(nums[j])
                j -= 1
            f[i] = sm % MOD

        return f[0]
```
