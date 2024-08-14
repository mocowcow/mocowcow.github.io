---
layout      : single
title       : LeetCode 3250. Find the Count of Monotonic Pairs I
tags        : LeetCode Hard DP PrefixSum
---
weekly contest 410。  

## 題目

輸入長度 n 的正整數陣列 nums。  

一組**單調**的**非負**整數陣列 (arr1, arr2) 滿足：  

- 兩陣列長度都為 n。  
- arr1 是單調**非遞減**，也就是 arr1[0] <= arr1[1] <= ... <= arr1[n - 1]。  
- arr2 是單調**非遞增**，也就是 arr2[0] >= arr2[1] >= ... >= arr2[n - 1]。  
- 對於所有 0 <= i <= n - 1，都有 arr1[i] + arr2[i] == nums[i]。  

求有多少**單調**陣列組。  
答案可能很大，先模 10^9 + 7 後回傳。  

## 解法

注意到 arr1[i] + arr2[i] == nums[i] 這條恆等式。  
我們只需要枚舉 arr1[i] 或是 arr2[i] 的其中一個值，就可以推算出另一半。  

假設我們從左往右枚舉 arr2[i]，為了知道能填入值的限制，還需要額外的變數表示上一個 arr2[i-1] 的值，記做 prev2。  
同理，可以由恆等式推算出 prev1 = arr1[i-1] 的值。  

設 curr1 = arr1[i], curr2 = arr2[i], x = nums[i]。  
知道 prev1 和 prev2 後，就可以枚舉位置 i 分別要填入什麼值。  
因為 prev2 <= curr2，所以從 prev2 開始向上枚舉，直到超過 x 為止。  
過程中透過 curr2 求出 curr1，若同時滿足 prev1 >= curr1，則代表當前 curr1, curr2 填法是合法的。  

---

位置 i 的限制只受到 i-1 值的影響。在更之前的位置填的方式不同，都有可能在 i 處得到同樣的 prev2。  
有**重疊的子問題**，因此考慮 dp。  

定義 dp(i, prev2)：在 arr2[i-1] 的值為 prev2 時，使得子陣列 [i..N-1] 滿足**單調**的填法數量。  
轉移：dp(i, prev2) = sum(dp(i+1, curr2)) FOR ALL (prev1 <= curr1 且 prev2 >= curr2)  
base：i = N 時，已經全部填完，回傳 1。  

i = 0 的位置並沒有受到任何限制，隨便填什麼都可以。  
因此答案為 sum(dp(1, curr2)) FOR ALL 0 <= curr2 <= nums[0]

時間複雜度 O(N \* M^2)，其中 M = max(nums)。  
空間複雜度 O(N \* M)。  

```python
MOD = 10 ** 9 + 7
class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        N = len(nums)

        @cache
        def dp(i, prev2):
            if i == N:
                return 1
            x = nums[i]
            prev1 = nums[i-1] - prev2
            res = 0
            for curr2 in range(min(prev2, x) + 1):
                curr1 = x - curr2
                if curr1 >= prev1:
                    res += dp(i+1 ,curr2)
            return res % MOD

        ans = 0
        for curr2 in range(nums[0] + 1):
            ans += dp(1, curr2)

        return ans % MOD
```

對於 Q4 更大的測資則會超時，得想辦法優化。  
首先改寫成遞推。  

```python
MOD = 10 ** 9 + 7
class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        N = len(nums)
        MX = max(nums) + 1
        f = [[0] * MX for _ in range(N + 1)]
        for prev2 in range(MX):
            f[N][prev2] = 1

        for i in reversed(range(1, N)):
            x = nums[i]
            for prev2 in range(nums[i-1] + 1):
                prev1 = nums[i-1] - prev2
                res = 0
                for curr2 in range(min(prev2, x) + 1):
                    curr1 = x - curr2
                    if curr1 >= prev1:
                        res += f[i+1][curr2]
                f[i][prev2] = res % MOD

        ans = 0
        for curr2 in range(nums[0] + 1):
            ans += f[1][curr2]

        return ans % MOD
```

仔細觀察，對於同一個 i 來說，隨著 prev2 的增加，curr2 所能容許的範圍也越大；同樣地，prev1 也同步減少，對於 curr1 的容許範圍也增加。  

以範例 2 的 nums = [5,5] 為例，討論 i = 0 時 (curr2, curr1) 的情況：  
> curr2 = 0, curr1 = 5  
> 可填 (0,5)  
> curr2 = 1, curr1 = 4  
> 可填 (0,5), (1,4)  
> ...  
> curr2 = 4, curr2 = 1  
> 可填 (0,5), (1,4), (2,3), (3,2), (4,1)  
> curr2 = 5, curr2 = 0  
> 可填 (0,5), (1,4), (2,3), (3,2), (4,1), (5,0)  

他們的轉移來源幾乎是相同的，而且只增不減，故可用**前綴和**進行優化，每次轉移只需要 O(1)。  

```python
MOD = 10 ** 9 + 7
class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        N = len(nums)
        MX = max(nums) + 1
        f = [[0] * MX for _ in range(N + 1)]
        for prev2 in range(MX):
            f[N][prev2] = 1

        for i in reversed(range(1, N)):
            x = nums[i]
            ps = 0
            curr2 = 0
            curr1 = x
            for prev2 in range(nums[i-1] + 1):
                prev1 = nums[i-1] - prev2
                # update prefix sum
                if curr2 <= prev2 and curr1 >= prev1:
                    ps += f[i+1][curr2]
                    ps %= MOD
                    curr2 += 1
                    curr1 -= 1
                f[i][prev2] = ps

        ans = 0
        for curr2 in range(nums[0] + 1):
            ans += f[1][curr2]

        return ans % MOD
```
