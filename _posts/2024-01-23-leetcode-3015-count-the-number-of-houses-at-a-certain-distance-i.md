---
layout      : single
title       : LeetCode 3015. Count the Number of Houses at a Certain Distance I
tags        : LeetCode Medium Array Graph
---
周賽381。

## 題目

輸入三個正整數 n, x 和 y。  

城市中，有 n 棟房子，編號分別從 1\~n，且有 n 條道路連接房子。  
對於滿足 1 <= i <= n - 1 的所有房子 i，都存在一條道路連接第 i 和第 i+1 棟房子。  
剩下最後一條道路是連接第 x 和第 y 棟房子。  

對於所有滿足 1 <= k <= n 的整數 k，你必須找到存在幾組房子(house1, house2)，從 house1 出發到 house2 所經過的最小道路數正好為 k。  

回傳長度 n，且索引從 1 開始的陣列 result，其中 result[k] 代表有多少組房子的最小街道數為 k。  

注意：x, y 可能相等。  

## 解法

其實一組房子所需經的**最小道路數**，就是兩點之間的**最短距離**，每條道路的距離都是 1。  
然後還要求任意兩點的最短距離，基本上就知道可以用 Floyd-Warshall 了。  

按照題意，依照每條道路建立雙向且距離為 1 的邊。  
執行 Floyd-Warshall，再枚舉所有組合，統計最短距離的出現頻率即可。  

時間複雜度 O(n^3)。  
空間複雜度 O(n^2)。  

```python
class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        fw = FloydWarshall(n)
        for i in range(1, n):
            fw.add(i, i-1, 1)
            fw.add(i-1, i, 1)
            
        fw.add(x-1, y-1, 1)
        fw.add(y-1, x-1, 1)
        fw.build()
       
        ans = [0]*n
        a = fw.dp
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                k = a[i][j]
                ans[k-1] += 1
                
        return ans
        
class FloydWarshall:
    def __init__(self, n):
        self.n = n
        self.dp = [[inf]*n for _ in range(n)]
        for i in range(n):
            self.dp[i][i] = 0

    def add(self, a, b, c):
        if c < self.dp[a][b]:
            self.dp[a][b] = c

    def get(self, a, b):
        return self.dp[a][b]

    def build(self):
        for k in range(self.n):
            for i in range(self.n):
                if self.dp[i][k] == inf:  # pruning
                    continue
                for j in range(self.n):
                    new_dist = self.dp[i][k]+self.dp[k][j]
                    if new_dist < self.dp[i][j]:
                        self.dp[i][j] = new_dist
```
