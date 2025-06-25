---
layout      : single
title       : LeetCode 3592. Inverse Coin Change
tags        : LeetCode Medium DP
---
weekly contest 455。  
最近在 CF 刷了破百的構造題，結果碰到這還是當機。  
構造題永遠是我大哥。  

## 題目

<https://leetcode.com/problems/inverse-coin-change/description/>

## 解法

相似題 [518. coin change 2]({% post_url 2022-02-10-leetcode-518-coin-change-2 %})。  
只是改成從結果逆推輸入。  

方便起見，把 numWays 左邊加一個 0。改變 numWays[i] 定義為總額為 i 的方法數。  

---

回想我們計算完全背包問題時，是**逐一加入硬幣面額**的。  
每加入一個面額 i，就會更新所有總額小於等於 i 的方法數。  

定義 dp[j]：代表總額為 j 的方法數。  
每加入面額 i，則 dp[j] 可由 dp[j-i] 的方法加上一個 i 組成。  
這是一個遞迴關係，在更新 dp[j] 之前，必須保證 dp[j-i] 更新過，所以要從小到大枚舉更新 j。  

---

先看範例 1，numWays[1] = 0，代表沒有總額為 1 的方法。所以沒有硬幣 1；  
範例 2，numWays[1] = 1，代表總額為 1 的方法有 1 種。所以必須有硬幣 1。  
這在提示說單個硬幣面額可以正好等於總額。  

按照 dp[i] 與 numWays[i] 的關係分類討論：  

- dp[i] = numWays[i]，沒有面額 i。  
- dp[i] = numWays[i] - 1，有面額 i。  
- 否則都是不可能出現的情況，直接回傳 -1。  

若有面額 i，則按照上述方式更新每個 dp[j]，並將面額 i 保存到答案中。  

時間複雜度 O(N^2)。  
空間複雜度 O(N)。  

```python
class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:
        N = len(numWays)
        numWays = [0] + numWays

        coins = []
        dp = [0] * (N+1)
        dp[0] = 1
        for i in range(1, N+1):
            # check if has coin i
            if dp[i] == numWays[i]:  # no
                continue
            elif dp[i] == numWays[i] - 1:  # has i
                coins.append(i)
            else:  # invalid ways
                return []

            # update ways with new coin i
            for j in range(i, N+1):
                dp[j] += dp[j-i]

        return coins
```
