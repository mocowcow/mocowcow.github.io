---
layout      : single
title       : LeetCode 3310. Remove Methods From Project
tags        : LeetCode Medium Graph DFS
---
weekly contest 418。  
這題意描述挺模糊的，原文是真的看不太懂。  

## 題目

你在維護一個專案，其中有 n 個方法，編號分別從 0 到 n - 1。  

輸入兩個整數 n 和 k，還有二維整數陣列 invocations，其中 invocations[i] = [a<sub>i</sub>, b<sub>i</sub>]，代表方法 a<sub>i</sub> 調用方法 b<sub>i</sub>。  

已知方法 k 有 bug。  
方法 k 本身以及其**直接**或**間接**調用的方法，都視作**可疑**的方法，需要把他們都移除掉。  
若一群互相調用的方法**群組**內都是可疑的，才能把他們移除。  

以任意順序回傳移除**可疑方法**後剩餘的方法。若無法移除則**不必**移除。  

## 解法

方法之間的調用關係是**有向圖**。  
建圖後，從 k 開始 dfs 就可以找到所有可疑的方法。  

然後再次遍歷所有調用，若有 a 不可疑且 b 可疑，則無法移除；否則移除所有可疑方法。  

時間複雜度 O(N + M)。  
空間複雜度 O(N + M)。  

```python
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for a, b in invocations:
            g[a].append(b)

        def dfs(i):
            if i in sus:
                return 
            sus.add(i)
            for j in g[i]:
                dfs(j)

        sus = set()
        dfs(k)
        for a, b in invocations:
            if a not in sus and b in sus: # cannont remove
                return set(range(n))

        return set(range(n)) - sus
```
