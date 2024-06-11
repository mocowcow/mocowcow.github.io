---
layout      : single
title       : LeetCode 3180. Maximum Total Reward Using Operations I
tags        : LeetCode Medium Array DP Greedy Sorting
---
周賽 401。又在卡常數，連續兩場都這樣搞，真的會被氣死。  

## 題目

輸入長度 n 的整數陣列 rewardValues，代表每個獎勵的價值。  

最初你的總獎勵為 x = 0，且所有獎勵都是未標記的。  
你可以執行以下操作任意次：  

- 選擇未標記的索引 i  
- 若 rewardValues[i] 大於當前總獎勵 x，則可以使 x 增加 rewardValues[i]，並標記索引 i  

求可以收集的總獎勵**最大值**。  

## 解法

rewardValues 好長，以下簡稱 r。  

首先題目並沒有規定獎勵的收集順序。先來看看怎樣收比較划算。  

設有兩個數 a, b 且 a > b：  

- 先拿 a，總獎勵肯定會超過 b，之後就不能拿 b。  
- 先拿 b，總獎勵不一定超過 a，之後還有機會拿 a。  

得到一個貪心的結論，先拿較小的獎勵更好。  
先將 r 排序。  

---

雖然知道了從小的開始拿，但不到哪些該拿。  
因此考慮 dp，枚舉**選或不選**。  

定義 dp(i, j)：當前總獎勵為 j，在剩餘 r[i..N-1] 可選的情況下，所能得到的最大獎勵。  
轉移：決定當前元素 x = r[i] 選或不選。  

- 選：若滿足 x > j，則 dp(i + 1, j + x) + x
- 不選：dp(i + 1, j)  

base：當 i = N 時，沒有元素可選，回傳 0。  

```python
class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        r = rewardValues
        r.sort()
        N = len(r)
        
        @cache
        def dp(i, j):
            if i == N:
                return 0
            x = r[i]
            # no take
            res = dp(i + 1, j)
            # take
            if x > j:
                res = max(res, dp(i + 1, j + x) + x)
            return res
        
        ans = dp(0, 0)
        dp.cache_clear()
        
        return ans
```
