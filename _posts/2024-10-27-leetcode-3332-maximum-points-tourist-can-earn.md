---
layout      : single
title       : LeetCode 3332. Maximum Points Tourist Can Earn
tags        : LeetCode Medium DP
---
biweekly contest 142。  
非常裸的題，幾乎直接告訴你怎麼寫了。  

## 題目

輸入兩個整數 n 和 k，還有兩個整數陣列 stayScore 和 travelScore。  

一個遊客在某個有 n 個城市的國家旅遊，每座城市都**直接**與其他所有城市相連。  
此遊客的行程**正好** k 天 (索引由 0 開始)，且可以選擇**任意**城市作為起點。  

對於每天行程，他有兩種選擇：  

- 停留在當前城市：在第 i 天留在當前城市 curr，獲得 stayScore[i][curr] 分數。  
- 前往其他城市：從城市 curr 前往城市 dest，獲得 travelScore[curr][dest] 分數。  

求遊客可以獲得的**最多**點數。  

## 解法

遊客每天都要決定去哪，也就是**枚舉選哪個**。  
不同的行程也可能在相同天數抵達相同城市，有**重疊的子問題**，考慮 dp。  

定義 dp(i, curr)：目前在城市 curr，決定第 i 天之後行程的最大分數。  
轉移：dp(i, curr) = max(停留, 移動)。  

- 停留 = dp(i+1, curr) + stayScore[i][curr]。  
- 移動 = max(dp(i+1, curr) + travelScore[curr][dest] FOR ALL dest != curr)。  

base：當 i = k 時，旅途結束無法繼續得分，回傳 0。  

每座城市都可以作為出發點，所以答案是 max(dp(0, curr) FOR ALL 0 <= curr < n)。  

時間複雜度 O(k \* n^2)。  
空間複雜度 O(kn)。  

k = n = 200 代入 O(kn^2) 運算量大約 8e6，有點緊張。  
而且 python 取 max 比較慢，竟然跑了 11000ms 好險沒超時。  

```python
class Solution:
    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:
        
        @cache
        def dp(i, curr):
            if i == k:
                return 0
            # stay
            res = dp(i+1, curr) + stayScore[i][curr]
            # move
            for dest in range(n):
                if dest != curr:
                    res = max(res, dp(i+1, dest) + travelScore[curr][dest])
            return res 
        
        return max(dp(0, curr) for curr in range(n))
```

改成遞推，加速到 7600ms 上下。  
再壓縮一個空間維度，加速到 7000ms，差不多。  
最重要的還是手寫 max，直接剩下 2800ms。  

時間複雜度 O(k \* n^2)。  
空間複雜度 O(n)。  

```python
class Solution:
    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:
        f = [0]*n
        for i in reversed(range(k)):
            f2 = [0]*n
            for curr in range(n):
                # stay
                res = f[curr] + stayScore[i][curr]
                # move
                for dest in range(n):
                    if dest != curr:
                        t = f[dest] + travelScore[curr][dest]
                        if t > res:
                            res = t
                f2[curr] = res
            f = f2
        
        return max(f[curr] for curr in range(n))
```
