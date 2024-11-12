---
layout      : single
title       : LeetCode 3350. Adjacent Increasing Subarrays Detection II
tags        : LeetCode Medium BinarySearch
---
weekly contest 423。  

## 題目

輸入長度 n 的整數陣列 nums。  
找到 k 的**最大值**，使得存在兩個長度為 k 的**相鄰**的**嚴格遞增子陣列**。  

具體的說，檢查是否存在索引由 a 和 b 開始的子陣列 (a < b)，滿足以下條件：  

- 兩個子陣列 nums[a..a + k - 1] 和 nums[b..b + k - 1] 都是**嚴格遞增**。  
- 兩個子陣列相鄰，即 b = a + k。  

求可能的 k 的**最大值**。  

## 解法

在 Q1 的時候說過：  
> 長度為 x 的遞增子序列，還可以分割成若干個小於等於 x 的子陣列。  

若找到某個合法的 k，則小於 k 的值都合法；反之，若 k 不合法，則大於 k 的值都不合法。  
也就是說 k 具有**單調性**，可以**二分答案**。  

```python
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        N = len(nums)

        subs = []
        i = 0
        while i < N:
            j = i
            while j+1 < N and nums[j] < nums[j+1]:
                j += 1
            subs.append(j-i+1) # size of increasing subarray
            i = j+1

        def ok(sz):
            for a, b in pairwise(subs):
                if a >= sz and b >= sz:
                    return True
            return mx_subs >= sz*2

        mx_subs = max(subs)
        lo = 1
        hi = N // 2
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if not ok(mid):
                hi = mid - 1
            else:
                lo = mid

        return lo
```

不過 Q1 也把答案的兩種情形討論出來了：  

- 兩個相鄰子陣列都提供 k。  
- 一個子陣列分割成兩個 k。  

其實可以直接轉換成：  

- 枚舉相鄰子陣列取較小值。  
- 子陣列大小除 2。  

並取其中最大值便是答案。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        N = len(nums)

        ans = 1
        pre = 0 # size of previous subarray
        i = 0
        while i < N:
            j = i
            while j+1 < N and nums[j] < nums[j+1]:
                j += 1

            cur = j-i+1 # size of current subarray
            ans = max(ans, min(pre, cur), cur // 2)

            pre = cur
            i = j+1

        return ans
```
