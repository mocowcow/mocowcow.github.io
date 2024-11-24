---
layout      : single
title       : LeetCode 3363. Find the Maximum Number of Fruits Collected
tags        : LeetCode Hard DP
---
biweekly contest 144。  
這題也非常厲害，使用到的技巧並不難，難在腦子怎麼轉彎。  
雖然我沒在時限內做出來，但還是很喜歡。  

## 題目

有個 n x n 的迷宮遊戲。  

輸入 n x n 矩陣 fruits，其中 fruits[i][j] 代表房間 (i, j) 的水果數量。  
有三個小孩參加遊戲，分別從 (0, 0), (0, n - 1) 和 (n - 1, 0) 的房間出發。  

每個小孩都必須移動**正好** n - 1 次，並且抵達房間 (n - 1, n - 1)：  

- 從 (0, 0) 出發的小孩，位於 (i, j) 時，只能向 (i + 1, j + 1), (i + 1, j) 或 (i, j + 1) 移動。  
- 從 (0, n - 1) 出發的小孩，位於 (i, j) 時，只能向 (i + 1, j - 1), (i + 1, j) 或 (i + 1, j + 1) 移動。  
- 從 (n - 1, 0) 出發的小孩，位於 (i, j) 時，只能向 (i - 1, j + 1), (i, j + 1) 或 (i + 1, j + 1) 移動。  

每當小孩進入一個房間，他會獲得房間內所有水果。  
如果有多個小孩進入同一個房間，只有第一個小孩能得到水果。  

求**最多**共能收集多少水果。  

## 解法

左上的人固定**只能走右下**，否則到不了終點。  
右上的人可以走**左下**、**下**或**右下**。  
左下的人可以走**右上**、**右**或**右下**。  

實際上只要考慮兩個人。  

兩人的移動順序不同，卻有可能在相同步數時停留在相同位置，有**重疊的子問題**，考慮 dp。  
我一開始想到的是 [1463. cherry pickup ii]({% post_url 2022-01-18-leetcode-1463-cherry-pickup-ii %})。  
但兩題的測資範圍有點差距。  

---

本題的核心其實非常簡單，說破就~~不值錢~~當頭棒喝。  

左上的大哥直接走**對角線**，把線上的水果都吃掉了。  
因為步數限制，最遠只能剛好走到對角線。且對角線上也沒水果，到了也沒意義。因此剩下兩位不管怎樣走都**不該走到對角線上**，因此兩人根本不會有交集。  

既然不會有交集，只要分別對兩人都求一個簡單的最大路徑總和，再加上對角線總和即可。  

時間複雜度 O(N^2)。  
空間複雜度 O(N^2)。  

```python
class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        N = len(fruits)

        ans = 0
        for i in range(N):
            ans += fruits[i][i]

        @cache
        def dp1(r, c):  # upper right guy
            if r == N-1 and c == N-1:
                return 0
            if r == N-1 or r == c: # bad dest or diagonal
                return -inf
                
            res = -inf
            for cc in [c-1, c, c+1]:
                if 0 <= cc < N:
                    res = max(res, dp1(r+1, cc))
            return res + fruits[r][c]

        @cache
        def dp2(r, c):  # bottom left guy
            if c == N-1 and r == N-1:
                return 0
            if c == N-1 or r == c: # bad dest or diagonal
                return -inf
                
            res = -inf
            for rr in [r-1, r, r+1]:
                if 0 <= rr < N:
                    res = max(res, dp2(rr, c+1))
            return res + fruits[r][c]

        ans += dp1(0, N-1)
        ans += dp2(N-1, 0)

        return ans
```
