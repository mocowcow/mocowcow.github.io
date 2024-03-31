---
layout      : single
title       : LeetCode 3098. Find the Sum of Subsequence Powers
tags        : LeetCode Hard Array DP
---
雙周賽 127。比賽剛開時網站有點卡，本來很希望這次 unrate；結果做完 Q4 發現不到 50 人過，又不希望他 unrate 了。  

## 題目

輸入長度 n 的整數陣列，還有正整數 k。  

一個子序列的**力量**定義為：子序列中**任意**兩元素絕對差的**最小值**。  

求 nums **長度為 k** 的所有子序列的**力量總和**。  
答案可能很大，先模 10^9 + 7 後回傳。  

## 解法

遇到求子序列問題時先排序。  
對陣列求子序列時，都是決定每個元素**選或不選**。而且很多都是 dp。  

子序列中任意兩元素**絕對差**的**最小值**，肯定是由兩個**最接近**的元素所構成。  
基於一開始的排序，正好使得每次**選擇的數**會和**上次選的數**來更新絕對差的最小值。  

---

在枚舉元素選或不選的過程中，除了維護**剩哪些可選**、**要選幾個**之外，還必須知道當前的**最小絕對差**以及**上次選的數**。  

定義 dp(i, need, prev, mn)：上次選的數是 prev，當前最小絕對差為 mn 的情況下，在 nums[i..(N-1)] 之中選擇 need 個元素的所有方案中，所得到的力量總和。  
轉移：nums[i] 選或不選，兩個加起來。  

- 選 nums[i]：dp(i + 1, need - 1, nums[i], new_mn)  
    若 prev 不為空，則以 nums[i] 和 prev 更新 mn，否則沿用 inf  
- 不選 nums[i]：dp(i + 1, need - 1, prev, mn)。視情況計算 new_mn。  

BASE：當 need 為 0，代表選夠 k 個，貢獻 mn 力量；否則若 i = N，沒元素可選了，不合法，回傳 0。  

---

時間複雜度就很尷尬了。  

i, need, prev 這三個變數很明顯各 N 個，這部分是 O(N^3)。  
至於 mn 呢？每個元素都可以和他之前的任意元素配對，有 O(N^2) 個。  
所以總共是 O(N^5)。  

看上去 50^5 會超時的，但其實很多狀態都不會碰到。  
在 k 很小的時候，總狀態個數幾乎是 N^4，這部分沒有問題。  
隨著 k 變大，途中選的元素越多，能夠產生的最小絕對差同時也在減少。  

時間複雜度 O(N^5)。  
空間複雜度 O(N^5)。  

```python
class Solution:
    def sumOfPowers(self, nums: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        N = len(nums)
        nums.sort()
        
        @cache
        def dp(i, need, prev, mn):
            if need == 0:
                return mn
            
            if i == N:
                return 0
            
            # no take
            res = dp(i + 1, need, prev, mn)
            
            # take
            curr = nums[i]
            if prev is None:
                new_mn = inf
            else:
                new_mn = min(mn, curr - prev)
            res += dp(i + 1, need - 1, curr, new_mn)
            return res % MOD
            
        ans = dp(0, k, None, inf)
        dp.cache_clear()
        
        return ans
```
