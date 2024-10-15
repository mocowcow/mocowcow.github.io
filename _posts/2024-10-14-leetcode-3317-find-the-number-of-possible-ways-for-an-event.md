---
layout      : single
title       : LeetCode 3317. Find the Number of Possible Ways for an Event
tags        : LeetCode Hard Math DP
---
biweekly contest 141。  
看到排列組合我就受不了了，直接等別人題解。  

## 題目

輸入三個整數 n, x 和 y。  

一個活動共有 n 個表演者。  
每個表演者都會被安排到 x 個隊伍其中之一，有可能有隊伍沒有表演者。  

所有隊伍都表演結束後，評審會給每個隊伍打分，分數界於 [1, y] 之間的整數。  

求有幾種不同的活動方案數。  
答案可能很大，先模 10^9 + 7 後回傳。  

注意，若兩個活動滿足以下條件之一，則視為**不同的**：  

- 存在任一表演者在不同的隊伍中  
- 存在任一隊伍的分數不同  

## 解法

看一堆題解講什麼斯特林數，我直接爆炸。  
最後找到幾個只用排列組合的方式，分享給數學和我一樣爛的同學。  

---

首先看打分方式，每組都有 y 種分數可以打。  
很明顯乘法原理，若有 j 組就是 pow(y, j) 種方案。  

---

在來，每個人都必須有組，所以**至少有 1 組**，至多 x 組。  

定義 f(i, j)：將 i 個人分到 j 個組的方案數。  
答案是 sum(f(n, j) \* pow(y, j)) for 1 <= j <= x。  

---

那 f(i, j) 如何推算？有兩種可能：  

- 在 i-1 人分到 j 組時，隨便加入 j 個**有人組**中之一。  
    即 dp(i-1, j) \* j。  
- 在 i-1 人分到 j-1 組時，隨便加入 (x-(j-1)) 個**無人組**中之一。  
    即 dp(i-1, j-1) \* (x-(j-1))。  

那遞迴要在何時結束？  
當 i = j = 0 時，人與組別都剛好分完，合法方案數 1。  
否則若有**人**或**組別**其中一者提早分完，是不合法的分組方式，方案數 0。  

注意到不同的選法會參考到同樣的狀態，有**重疊的子問題**，因此需要記憶化 (即 dp)。  

時間複雜度 O(nx)，因 y 受限於 x，故不影響複雜度。  
空間複雜度 O(nx)。  

```python
MOD = 10 ** 9 + 7
class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        
        @cache
        def dp(i, j): # i ppl for j groups
            if i == 0 and j == 0: 
                return 1
            if i == 0 or j == 0:
                return 0
            res = dp(i-1, j) * j # i-th ppl join old group
            res += dp(i-1, j-1) * (x-(j-1)) # i-th ppl create new group
            return res % MOD

        ans = 0
        score_ways = 1
        for j in range(1, x + 1): # at least 1 group
            score_ways *= y 
            ans += dp(n, j) * score_ways # j group for y score
            ans %= MOD
        dp.cache_clear() # prevent MLE

        return ans 
```
