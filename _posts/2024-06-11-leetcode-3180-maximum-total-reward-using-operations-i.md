---
layout      : single
title       : LeetCode 3180. Maximum Total Reward Using Operations I
tags        : LeetCode Medium Array DP Greedy Sorting HashTable
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

---

至於 j 究竟會變得多大？假設 r 之中最大的數字是 R，那麼能選擇 R 所能持有的最大獎勵數為 R - 1。  
所以 j 最大只會變成 R 的兩倍。  

時間複雜度 O(N \* MX)，其中 MX = max(r) \* 2。  
空間複雜度 O(N \* MX)。  

很可惜 python 記憶化又沒辦法通過 2000 \* 4000 的計算量，有夠扯。  

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

改成遞推版本才能過。  

```python
class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        r = rewardValues
        r.sort()
        N = len(r)
        MX = max(r) * 2

        dp = [[0] * (MX) for _ in range(N + 1)]
        for i in reversed(range(N)):
            x = r[i]
            for j in range(MX):
                # no take
                res = dp[i + 1][j]
                # take
                if x > j and j + x < MX:
                    res = max(res, dp[i + 1][j + x] + x)
                dp[i][j] = res
                
        return dp[0][0]
```

觀察發現，dp[i][j] 會重複使用到 dp[i + 1][j] 的值，第一個空間維度可以優化掉。  
這邊就不寫了。  

上述做法都是以子序列的**狀態**為重點的 dp。  

---

也可以將本題視作一個背包問題：  
> 背包初始容量為 j，可以裝入滿足 x > j 的物品 x  
> 求背包最大可以裝多少容量  

需要維護的是**能夠湊出的容量總和**。  
初始容量只有 0 一種，之後每個 x，能夠和能與原有的容量 j 變成新的容量 x + j。  

例如：  
> r = [1,3,4]  
> 最初 dp = {0}  
> x = 1 可以和 0 組成新的容量  
> dp = {0,**1**}  
> x = 3 可以和 0,1 組成新的容量  
> dp = {0,1,**3,4**}  
> x = 4 可以和 0,1,3 組成新的容量  
> dp = {0,1,3,4,**5,8**}  

雖然複雜度一樣沒變，但執行時間從上面的 5000ms 降低到 600ms，效率提高非常多。  

```python
class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        r = rewardValues
        r.sort()
        MX = max(r) * 2
        
        dp = set()
        dp.add(0)
        for x in r:
            for j in list(dp):
                if x > j and x + j < MX:
                    dp.add(x + j)
        
        return max(dp)
```
