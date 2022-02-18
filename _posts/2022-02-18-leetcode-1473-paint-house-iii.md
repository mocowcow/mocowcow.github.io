---
layout      : single
title       : LeetCode 1473. Paint House III
tags 		: LeetCode Hard DP
---
DP教學系列。這絕對是我碰過最噁的DP題目之一，光是題目就夠臭夠長。

# 題目
輸入整數陣列houses表示房屋目前顏色、二維整數陣列cost表示把某房屋改成某色的價格，整數target表示社區數量。  
房屋有[0..m-1]共m個，顏色有[1..n]共n種。  
若houses[i]=0，代表還未上色，可以改成任何顏色；已有顏色的房屋則不可以改動。
cost[i][j]表示把第i房改成第j色的花費。  
定義一串連續且相同顏色的房子為同社區，如[1,2,2,3,3,2,1,1]形成五個社區[[1], [2,2], [3,3], [2], [1,1]]。  
求改造成正好target社區的最低成本方式，若不可能改造成功，則回傳-1。

# 解法
一開始我還真想不出這要怎麼寫，直到看了提示二：  
> Define dp[i][j][k] as the minimum cost where we have k neighborhoods in the first i houses and the i-th house is painted with the color j.

那就開始DP吧。

>步驟1：定義狀態  

dp(i,j,k)代表從0到第i個房屋全部總共形成k個社區，且houses[i]顏色為j。

>步驟2：找出狀態轉移方程式  

dp(i,j,k)可能來自於兩種狀況：
- i-1的顏色和i一樣，社區數不變
- i-1顏色和i不同，社區數會比當前少1
  
故求以上所有可能之最小值，最後記得檢查當前房屋需不需要改色開銷，就是結果。  
方程式為：  
dp(i,j,k)=min(dp(i-1,j,k),dp(i-1,last,k-1) FOR ALL 1<=last<=n 且 last!=j) + cost[i][j-1] 若 houses[i]=0。

>步驟3：處理base cases

當i<0時不存在房屋要改，成本為0。  
當k>=(i+1)時，社區數比房屋數還多，根本不可能，回傳inf。  
當k<1，沒有社區是什麼鬼，也不可能，回傳inf。
若houses[i]已經有顏色了，且跟目標顏色不同，一樣不可能，回傳inf。  

我在寫的時候把條件搞混，卡了一好陣子。這題真的不好弄。  
從(最後一棟房子的任意顏色 組成target個社區)找最小值就是答案。

```python
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:

        @lru_cache(None)
        def dp(i, j, k):
            if i < 0:
                return 0
            if k > i + 1 or k < 1:
                return math.inf
            if houses[i] != 0 and houses[i] != j:
                return math.inf

            best = dp(i-1, j, k)  # same color as last
            for last in range(1, n+1):  # for all diff colors
                if last != j:
                    best = min(best, dp(i-1, last, k-1))

            if houses[i] == 0:
                best += cost[i][j-1]

            return best

        ans = math.inf
        for j in range(1, n+1):
            ans = min(ans, dp(m-1, j, target))

        return -1 if ans == math.inf else ans

```
