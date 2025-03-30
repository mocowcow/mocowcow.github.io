---
layout      : single
title       : LeetCode 3502. Minimum Cost to Reach Every Position
tags        : LeetCode Easy Greedy
---
weekly contest 443。  
閱讀理解題，很有 CF 的感覺。  

## 題目

<https://leetcode.com/problems/minimum-cost-to-reach-every-position/description/>

## 解法

跟左邊的人換位置要付錢，跟右邊的換位置免費。  
一開始你在最右邊，求到每個 i 的最少費用。  

想到 i，可以直接付費 cost[i]。  
或是隨便某個 j < i 的 cost[j]，然後在免費到 i。  
所以到 i 的最小費用就是 min(cost[..i])。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        mn = inf
        ans = []
        for x in cost:
            mn = min(mn, x)
            ans.append(mn)

        return ans
```
