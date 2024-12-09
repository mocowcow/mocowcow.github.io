---
layout      : single
title       : LeetCode 3377. Digit Operations to Make Two Integers Equal
tags        : LeetCode Medium Graph Math BFS Heap
---
biweekly contest 145。  
看到不少人說題目有瑕疵，沒有提及**前導零**。  
但個人覺得沒差，因為整數修改修出前導 0 後會損失數位個數，不可能加回來，不影響答案。  

## 題目

輸入整數 n 和 m，兩者具有**相同**的數位個數。  

你可以執行以下操作任意次：  

- 選擇 n 的任意非 9 數位，並將其**增加** 1。  
- 選擇 n 的任意非 0 數位，並將其**減少** 1。  

n 在整個過程中都不可以是**質數**，包括初始值以及最終結果。  

將 n 進行數字若干次操作的成本為變化過程的**所有值**之和。  

求將 n 變成 m 的**最小成本**。若不可能則回傳 -1。  

## 解法

把所有非質數當成圖上的節點，問題轉換成：  
> 求 n 到 m 的最小路徑成本  

相似題 [752. Open the Lock](https://leetcode.com/problems/open-the-lock/)。  

---

總之先預處理質數表，以供 O(1) 判斷。  

求最短路問題，因為邊權不同，需使用 dijkstra。  
從 n 出發，初始成本為 n。
枚舉當前節點 curr 的鄰居 adj，移動到 adj 的成本為 adj。  

圖中至多有 O(N) 個頂點。  
一個頂點至多 log N 位數，也就是 E = 2 log N 條邊。  

時間複雜度 O(E log E)。
空間複雜度 O(E)。  

```python
def prime_table(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return sieve

@cache
def neighbors(x):
    cand = []
    t = x
    mult = 1
    while t > 0:
        r = t % 10
        if r < 9:
            cand.append(x+mult)
        if r > 0 and (t >= 10 or r != 1):
            cand.append(x-mult)
        t //= 10
        mult *= 10
    return cand

is_prime = prime_table(10000+5)

class Solution:
    def minOperations(self, n: int, m: int) -> int:
        if is_prime[n] or is_prime[m]:
            return -1

        vis = set()
        vis.add(n)
        h = []
        heappush(h, [n, n]) # [cost, curr]
        while h:
            cost, curr = heappop(h)
            if curr == m:
                return cost
                
            for adj in neighbors(curr):
                if adj not in vis and not is_prime[adj]:
                    vis.add(adj)
                    heappush(h, [cost+adj, adj])

        return -1
```
