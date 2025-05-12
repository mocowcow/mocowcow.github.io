---
layout      : single
title       : LeetCode 3544. Subtree Inversion Sum
tags        : LeetCode Hard Tree DP
---
biweekly contest 156。  
又是卡 python 的一天。  

## 題目

<https://leetcode.com/problems/subtree-inversion-sum/description/>

## 解法

以 0 為根節點的樹，每個子樹可以選擇**反轉**或**不反轉**，但與上次反轉的位置需間隔 k 步。  
求最大節點和。  

不考慮 k 的話，只需暴力沒舉每個節點子樹要不要反轉而已。  
不同的選法可能有相同的反轉結果，有**重疊的子問題**，考慮 dp。  
以狀態 sign = 1/-1 表示是否反轉過，直接和節點值相乘。  

注意到 k = 50 非常小，只需要額外用一個狀態 cd 紀錄反轉還需多少冷卻時間。  
定義 dp(i, fa, sign, cd)：以 i 為根節點的子樹，反轉狀態為 sign，還需 cd 步才可以反轉的情況下，子樹的最大節點和。  
枚舉所有子節點 j，判斷 j 的選法取最大值加入節點和：  

- 不反轉 j，dp(j, i, sign, max(0, cd-1))  
- 反轉 j，dp(j, i, -sign, k-1)  

---

根節點 0 可**反轉**或**不反轉**。  
答案為 max(dp(0, -1, 1, 0), dp(0, -1, -1, k-1))。  

本題記憶體限制很小氣，用 @cache 會爆 MLE，就算 clear_cache() 也爆。  
要改成手寫記憶化才能過。  

時間複雜度 O(Nk)。  
空間複雜度 O(Nk)。  

```python
class Solution:
    def subtreeInversionSum(self, edges: List[List[int]], nums: List[int], k: int) -> int:
        N = len(edges) + 1
        g = [[] for _ in range(N)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        memo = {}

        def dp(i, fa, sign, cd):
            state = (i, sign, cd)
            if state in memo:
                return memo[state]

            res = sign * nums[i]
            for j in g[i]:
                if j == fa:
                    continue
                t = dp(j, i, sign, max(0, cd-1))
                if cd == 0:  # flip
                    t = max(t, dp(j, i, -sign, k-1))
                res += t
            memo[state] = res
            return res

        ans = dp(0, -1, 1, 0)  # no flip
        ans = max(ans, dp(0, -1, -1, k-1))  # flip root

        return ans
```
