---
layout      : single
title       : LeetCode 3473. Sum of K Subarrays With Length at Least M
tags        : LeetCode Medium DP PrefixSum
---
weekly contest 439。  
這題是真的離譜，前綴和優化 dp 肯定該標 hard。  

再加上這該死的測資，對於 python 來說卡得要死，記憶化直接 TLE。  
很佩服我在最後 30 秒寫出遞推版本成功晉升三題仔。  

結果比賽後再拿 TLE 的記憶化版本提交幾次，發現竟然又能 AC。  
太無語了。  

## 題目

<https://leetcode.com/problems/sum-of-k-subarrays-with-length-at-least-m/description/>

## 解法

從 nums 中選出 k 的不重疊的子陣列。有點類似於**分割**，但不要求子陣列相連，所以某些 nums[i] 可以不選。  
對於 nums[i..] 找 k 個子陣列，不選 nums[i] 的話，變成 nums[i+1..]，找 k 個子陣列；  
選的話，可以選滿足 j-i+1 >= m 的 nums[i..j]，變成 nums[j+1..] 找 k-1 個子陣列。  

不同的選法會得到**重疊的子問題**，考慮 dp。  

---

定義 dp(i, rem)：從 nums[i..] 找出 rem 個大小至少 m 的子陣列最大和。  
轉移：  

- 不選：dp(i+1, rem)。  
- 選：sum(dp(j+1, rem-1) + sum(nums[i..j]) FOR ALL i+m-1 <= j < N-1)。  

BASE：當 k = 0 時，分割完成，回傳 0；否則當 i+m > N 時，無法繼續分割，回傳 -inf。  

1 <= m <= 3，這使得每個狀態都需要轉移 O(N) 次。  
時間複雜度 O(N^2 \* k)，會 TLE。  

```python
ps = list(accumulate(nums, initial=0))          

@cache
def dp(i, rem):
    if rem == 0:
        return 0
    if i+m > N:
        return -inf

    res = dp(i+1, rem)  # skip
    for j in range(i+m-1, N):
        sm = ps[j+1] - ps[i]
        res = max(res, dp(j+1, rem-1) + sm)
    return res
```

觀察 dp(i, rem) 的轉移來源：  
> dp(i+m, rem-1) + sum(nums[i..i+m-1])  
> dp(i+m+1, rem-1) + sum(nums[i..i+m])  
> dp(i+m+2, rem-1) + sum(nums[i..i+m+1])  
> ..
> dp(N, rem-1) + sum(nums[i..N-1])  

再觀察 dp(i+1, rem) 的轉移來源：  
> dp(i+m+1, rem-1) + sum(nums[i+1..i+m])  
> dp(i+m+2, rem-1) + sum(nums[i+1..i+m+1])  
> dp(i+m+3, rem-1) + sum(nums[i+1..i+m+2])  
> ..
> dp(N, rem-1) + sum(nums[i+1..N-1])  

發現有大部分都是相似的。  
dp(i, rem) 只比 dp(i+1, rem) 多一個新來源 dp(i+m, rem-1) + sum(nums[i..i+m-1])。  
其餘都是舊來源加上 nums[i] 而已。  
可以用**前綴和優化**轉移來源，這樣轉移只要 O(1)。  

時間複雜度 O(Nk)。  
空間複雜度 O(Nk)。  

```python
class Solution:
    def maxSum(self, nums: List[int], k: int, m: int) -> int:
        N = len(nums)
        ps = list(accumulate(nums, initial=0))

        @cache
        def dp_ps(i, rem):
            if rem == 0:
                return 0
            if i+m > N:
                return -inf
            res = dp_ps(i+1, rem) + nums[i]
            sm = ps[i+m] - ps[i]
            res = max(res, dp(i+m, rem-1) + sm)
            return res

        @cache
        def dp(i, rem):
            if rem == 0:
                return 0
            if i+m > N:
                return -inf

            res = dp(i+1, rem)  # skip
            res = max(res, dp_ps(i, rem))
            return res

        ans = dp(0, k)
        dp.cache_clear() # prevent MLE
        dp_ps.cache_clear() # prevent MLE

        return ans
```

改成遞推寫法。  
複雜度不變，但執行時間從 15000ms 降到 6000ms，快了非常多。  

```python
class Solution:
    def maxSum(self, nums: List[int], k: int, m: int) -> int:
        N = len(nums)
        ps = list(accumulate(nums, initial=0))

        dp = [[-inf] * (k + 1) for _ in range(N + 1)]
        dp_ps = [[-inf] * (k + 1) for _ in range(N + 1)]
        for i in range(N + 1):
            dp[i][0] = 0
            dp_ps[i][0] = 0

        for i in reversed(range(N)):
            for rem in range(1, k + 1):
                dp_ps[i][rem] = dp_ps[i+1][rem] + nums[i]
                if i + m <= N:
                    sm = ps[i+m] - ps[i]
                    dp_ps[i][rem] = max(dp_ps[i][rem], dp[i+m][rem-1] + sm)
                dp[i][rem] = max(dp[i+1][rem], dp_ps[i][rem])

        return dp[0][k]
```
