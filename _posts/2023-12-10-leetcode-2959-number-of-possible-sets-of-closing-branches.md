---
layout      : single
title       : LeetCode 2959. Number of Possible Sets of Closing Branches
tags        : LeetCode Hard Array Graph BitManipulation Bitmask
---
雙周賽119。好像刷新個人最快AK紀錄，23分32秒。  

## 題目

某公司在國內共有n個支部，其中某些支部之間有道路相連。最初，所有支部之間都存在著可以連通的路徑。  

公司覺得浪費錢，所以想關閉某些支部(也可能不關)。他們想確保所有支部之間的距離**最多**為maxDistance。  
兩間支部的**距離**指的是從某方出發，抵達另一方所需的**最小**移動距離。  

輸入整數n, maxDistance還有輸入二維整數陣列roads，其中roads[i] = [u<sub>i</sub>, v<sub>i</sub>, w<sub>i</sub>]，代表u<sub>i</sub>和v<sub>i</sub>兩個支部之間，存在一條長度為w<sub>i</sub>的**無向**道路。  

求關閉某些支部的可行方案數，其滿足各距離不得超過maxDistance。  

注意：某支部關閉後，連接到該處的所有道路都不可用。  
注意：兩個支部之間可能會有多條道路。  

## 解法

注意到最多n=10個支部，這是比較容易下手的方向。窮舉所有支部關閉或不關閉，總共有2^n = 1024種方案數。  

要找n點之間的最短路徑，會想到Floyd-Warshall最短路，複雜度O(n^3)。  
2^n \* n^3最多約10^6次計算量，答案呼之欲出。  

枚舉關閉方案時，包含被關閉支部的道路都不可用，所以每次都要過濾掉不可用的道路，整個重新建圖。  
而且支部之間存在重邊，初始化相鄰矩陣時要選擇最短邊。  

時間複雜度O(2^n \* n^3)。  
空間複雜度O(n^2)。  

```python
class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        
        def f(mask):
            dp=[[inf]*n for _ in range(n)]
            for i in range(n):
                dp[i][i]=0
                
            # add edges
            for a,b,c in roads:
                if mask&(1<<a) or mask&(1<<b):
                    continue
                if c<dp[a][b]:
                    dp[a][b]=c
                    dp[b][a]=c
            
            # floyd
            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        new_dist=dp[i][k]+dp[k][j]
                        if new_dist<dp[i][j]:
                            dp[i][j]=new_dist
            
            for a in range(n):
                if mask&(1<<a):
                    continue
                for b in range(n):
                    if mask&(1<<b):
                        continue
                    if dp[a][b]>maxDistance:
                        return False
            return True
                    
        ans=0
        for mask in range(2**n):
            if f(mask):
                ans+=1
                
        return ans
```
