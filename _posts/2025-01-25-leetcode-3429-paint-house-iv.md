---
layout      : single
title       : LeetCode 3429. Paint House IV
tags        : LeetCode Medium DP
---
weekly contest 433。
有點小心機的 dp 題。  

## 題目

<https://leetcode.com/problems/paint-house-iv/>

## 解法

不同顏色的選法，有可能在剩餘房子數相同時，產生相同花費。有重疊的子問題，因此考慮 dp。  
為了避免與**前一個**顏色相同，需要狀態 p 紀錄上次顏色。  

---

但是又限制**等距**的房子顏色不同，即 i 與 N-1-i 不同色。  
如果從左到右依序上色，對於右半的房子來說沒有辦法知道他**等距**的房子顏色，很難處理。  

房子顏色至多三種，可以考慮從這方面下手。  
考慮房子 i 時，同時考慮 j = N-1-i 的顏色，枚舉兩房子顏色選法共 3 \* 3 種。  
為了考慮 i, j 都與相鄰顏色不同，需要將 prev 改成 pi, pj，分別記錄上次顏色。  
枚舉 i, j 的顏色選法，並以合法的選法更新答案。  

---

定義 dp(i, p1, p2)：編號 [i, N-1-i] 房子的最小上色成本，其中 i 的相鄰顏色是 p1，且 N-1-i 的相鄰顏色是 p2。  
轉移：min(cost + dp(i+1, new_p1, new_p2) FOR ALL (new_p1, new_p2))。其中 new_p1, new_p2 為合法的顏色選法。  
base：當 i = N/2 時，上色完成，回傳 0。  

第 0 棟房子顏色任意，隨便填一個不會出現的顏色即可。  
答案入口 dp(0, -1, -1)。  

時間複雜度 O(N \* k^4)，其中 k = 3。  
空間複雜度 O(N \* k^2)。  

```python
class Solution:
    def minCost(self, n: int, cost: List[List[int]]) -> int:

        @cache
        def dp(i, pi, pj):
            if i*2 == n:
                return 0
                
            j = n-1-i
            res = inf
            for c1 in range(3):
                if c1 == pi:
                    continue
                for c2 in range(3):
                    if c2 == pj or c1 == c2:
                        continue
                    t = cost[i][c1] + cost[j][c2] + dp(i+1, c1, c2)
                    res = min(res, t)
            return res

        return dp(0, -1, -1)
```
