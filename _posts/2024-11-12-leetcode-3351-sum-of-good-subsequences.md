---
layout      : single
title       : LeetCode 3351. Sum of Good Subsequences
tags        : LeetCode Hard DP
---
weekly contest 423。  
一次寫出正確答案還滿爽的，可惜當天有事沒參賽。  

## 題目

輸入整數陣列 num。  

一個**好的**子序列中，**任意兩個**相鄰元素的差都**正好**是 1。  

求 nums 的所有**好的子序列**的總和。  
答案可能很大，先模 10^9 + 7 後回傳。  

## 解法

注意本題求的是子序列總和，**不是個數**。  
但計算總和還是依賴於個數。  

在這種子序列計數 dp 問題，通常考慮某個元素**選或不選**對答案造成的影響。  
每考慮一個新的元素 x，有四種情形：  

- 不選 x。  
- 自成一個新的子序列 [x]。  
- 追加到 x-1 結尾的子序列後方。  
- 追加到 x+1 結尾的子序列後方。  

---

設 cnt[x] 代表以 x 結尾的子序列數量。  
每次考慮新的 x，則 cnt[x] 的方案有：  

- 不選 x，保有 cnt[x] 個。  
- 自成一個新的子序列 [x]，增加 1 個。  
- 追加到 x-1 結尾的子序列後方，增加 cnt[x-1] 個。  
- 追加到 x+1 結尾的子序列後方，增加 cnt[x+1] 個。  

那子序列總和怎麼算？  
設 val[x] 代表以 x 結尾的子序列總和。  
每次考慮新的 x，則 val[x] 的總和有：  

- 不選 x，保有 val[x] 個。  
- 自成新的子序列，增加 x。  
- 追加到 x-1 結尾的子序列後方，增加 val[x-1] + cnt[x-1] * x。  
- 追加到 x+1 結尾的子序列後方，增加 val[x+1] + cnt[x+1] * x。  

同時更新 cnt 和 val 的值，最後把所有 val[x] 加起來就是答案。  

---

時間複雜度 O(N^2)。  
空間複雜度 O(N^2)。  

注意此記憶化寫法會超時，必須繼續優化。  

```python
MOD = 10 ** 9 + 7
class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        N = len(nums)

        @cache
        def cnt(i, x):
            if i == N:
                return 0
            res = cnt(i+1, x)
            if nums[i] == x:
                inc = 1 + cnt(i+1, x-1) + cnt(i+1, x+1)
                res += inc
            return res % MOD

        @cache
        def val(i, x):
            if i == N:
                return 0
            res = val(i+1, x)
            if nums[i] == x:
                inc = x
                inc += val(i+1, x-1) + cnt(i+1, x-1) * x
                inc += val(i+1, x+1) + cnt(i+1, x+1) * x
                res += inc
            return res % MOD

        ans = 0
        for x in set(nums):
            ans += val(0, x)

        return ans % MOD
```

注意到每當考慮一個新元素 x 時，對於所有 cnt[i][x] 和 val[i][x] 只有在 nums[i] = x 時會改變，其餘都維持不變。  
因此使用遞推寫法可以沿用前一次的結果，只更新 x 對應的值，每次轉移只需要 O(1)。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
MOD = 10 ** 9 + 7
class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        cnt = Counter()
        val = Counter()
        for x in nums:
            # update sum
            inc = x
            inc += val[x-1] + cnt[x-1] * x
            inc += val[x+1] + cnt[x+1] * x
            val[x] += inc
            val[x] %= MOD
            # update freq
            cnt[x] += cnt[x-1] + cnt[x+1] + 1
            cnt[x] %= MOD
            
        return sum(val.values()) % MOD
```
