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
