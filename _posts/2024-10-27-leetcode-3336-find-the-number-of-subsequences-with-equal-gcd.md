---
layout      : single
title       : LeetCode 3336. Find the Number of Subsequences With Equal GCD
tags        : LeetCode Hard DP
---
weekly contest 421。  
一眼 dp，但很神奇做出來的人偏少，不太確定為什麼。  

## 題目

輸入整數陣列 nums。  

你的目標是找到有多少對**非空**子序列 (seq1, seq2) 滿足以下條件：  

- 子序列 seq1, seq2 **不相交**，即不共享同一個索引的元素。  
- seq1, seq2 擁有相同的 GCD。  

回傳滿足條件的子序列對數量。  
答案可能很大，先模 10^9 + 7 後回傳。  

## 解法

子序列問題常常是考慮**選或不選**，不同選法有可能得到相同的結果，有**重疊的子問題**，考慮 dp。  

而同時維護兩個子序列，且要保證**不相交**，有三種情況：  

- seq1 選。  
- seq2 選。  
- 都不選。  

只要選了，就和當前子序列求 gcd。  

---

定義 dp(i, seq1, seq2)：在子序列 gcd 分別為 seq1, seq2 時，剩餘 nums[i..] 的合法選法數量。  
轉移：dp(i, seq1, seq2) = sum(seq1 選, seq2 選, 都不選)。  

- seq1 選 = dp(i+1, gcd(seq1, nums[i]), seq2)。  
- seq1 選 = dp(i+1, seq1, gcd(seq2, nums[i]))。  
- seq1 選 = dp(i+1, seq1, seq2)。  

base：當 i = N 時，沒有剩餘元素，若兩者 gcd 都不為 0 且相等則回傳 1；否則回傳 0。  

0 是任何整數的因數，有 gcd(x, 0) = x。  
因此答案入口為 dp(0, 0, 0)。  

時間複雜度 O(N \* MX^2 \* log MX)，其中 MX = max(nums)。  
空間複雜度 O(N \* MX^2)。  

老實說 N 和 MX 都是 200，光是狀態數就有大概 8e6，老實說有點危險。  
不過考慮到 gcd 只增不減，而且有些數根本不會出現，實際上無效狀態還不少。  

```python
MOD = 10 ** 9 + 7
class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        N = len(nums)

        @cache
        def dp(i, seq1, seq2):
            if i == N:
                if seq1 != 0 and seq1 == seq2:
                    return 1
                return 0
            
            res = dp(i+1, gcd(seq1, nums[i]), seq2)
            res += dp(i+1, seq1, gcd(seq2, nums[i]))
            res += dp(i+1, seq1, seq2)
            return res % MOD

        return dp(0, 0, 0)
```

預處理 gcd，然後改成遞推。  
雖然複雜度下降，但實際耗時反而增加。  

時間複雜度 O(N \* MX^2)，其中 MX = max(nums)。  
空間複雜度 O(N \* MX^2)。  

```python
MOD = 10 ** 9 + 7
MX = 200
GCD = [[0] * (MX+1) for _ in range(MX+1)]
for i in range(MX+1):
    for j in range(MX+1):
        GCD[i][j] = gcd(i, j)

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        N = len(nums)
        MX = max(nums)

        @cache
        def dp(i, seq1, seq2):
            if i == N:
                if seq1 != 0 and seq1 == seq2:
                    return 1
                return 0
            
            res = dp(i+1, GCD[seq1][nums[i]], seq2)
            res += dp(i+1, seq1, GCD[seq2][nums[i]])
            res += dp(i+1, seq1, seq2)
            return res % MOD

        f = [[[0] * (MX+1) for _ in range(MX+1)] for _ in range(N+1)]
        for seq1 in range(1, MX+1):
            f[N][seq1][seq1] = 1

        for i in reversed(range(N)):
            for seq1 in range(MX+1):
                for seq2 in range(MX+1):
                    res = f[i+1][GCD[seq1][nums[i]]][seq2]
                    res += f[i+1][seq1][GCD[seq2][nums[i]]]
                    res += f[i+1][seq1][seq2]
                    f[i][seq1][seq2] = res % MOD

        return f[0][0][0]
```
