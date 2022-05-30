--- 
layout      : single
title       : LeetCode 2285. Maximum Total Importance of Roads
tags        : LeetCode Medium Array Sorting
---
雙周賽79。最近幾次最簡單的Q3之一，抓到重點很快就能寫出來。

# 題目
輸入整數n，代表城市數量。城市的編號從0到n-1。  
還有二維陣列road，其中road[i] = [a, b]表示連接城市a和b的雙向道路。  
你要為每個城市定義價值，從1~n中選擇，且每個數字只能使用一次。  
而**道路重要度**定義為它連接的兩個城市的價值總和。  

求在最佳分配情況下，所有**道路的最大重要度總和**。

# 解法
看到例圖還以為要建立graph，結果根本不用。  
與其關注每條道路可以產生多少重要度，不如改想**每座城市能提供多少重要度**。  
一座城市所連接的道路越多，那他就可以產生更大的重要度。  
遍歷roads，將兩端城市的道路計數+1。再將道路數排序，分配給1\~n的價值，兩兩相乘後加總即可。  

```python
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        conn=[0]*n
        for a,b in roads:
            conn[a]+=1
            conn[b]+=1
            
        return sum(i*x for i,x in enumerate(sorted(conn),1))
```
