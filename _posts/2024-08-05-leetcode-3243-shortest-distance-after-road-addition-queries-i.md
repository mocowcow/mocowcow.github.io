---
layout      : single
title       : LeetCode 3243. Shortest Distance After Road Addition Queries I
tags        : LeetCode Medium Graph DP
---
weekly contest 409。  

## 題目

輸入整數 n 以及二維整數陣列 queries。  

有 n 個城市，編號分別由 0 到 n - 1。  
最初，所有編號滿足 0 <= i < n - 1 的城市 i，都存在一條通往城市 i + 1 的**無向**道路。  

queries[i] = [u<sub>i</sub>, v<sub>i</sub>] 代表**新增**一條 u<sub>i</sub> 往 v<sub>i</sub> 的**無向**道路。  
對於每次查詢，你必須在新增道路後，查詢城市 0 到城市 n - 1 的最短距離。  

回傳陣列 answer，其中 answer[i] 代表第 i 次查詢的結果。  

## 解法

初始化建圖，每次查詢先加入新的邊後再求最短路。  

走不同邊的路徑可能會抵達同樣的城市，有**重疊的子問題**，因此考慮 dp。  
定義 dp(i)：從城市 i 到 n-1 的最短距離。  
轉移：dp(i) = max(dp(j) FOR ALL j in g[i]) + 1  
base：當 i = n-1，抵達終點，回傳 0。  

最初邊數是 n-1，每次查詢會多一條新邊，至多約 n + Q = 1000 條邊。  
每次查詢的複雜度是 O(n + Q)

時間複雜度 O(Q \* (n + Q))，其中 Q = 查詢次數。  
空間複雜度 O(n + Q)。  

```python
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for i in range(n - 1):
            g[i].append(i + 1)

        ans = []
        for x, y in queries:
            @cache
            def dp(i):
                if i == n - 1:
                    return 0
                return min(dp(j) for j in g[i]) + 1

            g[x].append(y)
            ans.append(dp(0))

        return ans
```
