---
layout      : single
title       : LeetCode 3154. Find Number of Ways to Reach the K-th Stair
tags        : LeetCode Hard Math DP
---
周賽 398。近來最簡單 Q4，可能很多人都是數學解。  

## 題目

輸入非負整數 k。有個無限層數的樓梯，最低層編號為 0。  

Alice 擁有一個初始值為 0 整數 jump。  
Alice 要從第 1 層出發，透過任意次操作抵達第 k 層。  
當位於第 i 層時，可以：  

- 前往第 i - 1 層。此操作不可連續使用，也不可在第 0 層使用  
- 前往 i + 2^jump 層。移動後 jump 會變成 jump + 1  

求 Alice 共有幾種抵達 k 層的方案數。  

注意：Alice 可以抵達 k 層後透過某些操作又再次回到 k 層，此視作不同方案。  

## 解法

jump 只增不減，每次上樓的步數都會變成兩倍。  
而 k 最大只到 10^9，最多只能上樓 30 次。

下樓不能連續，而且每次只能往下一層，也就是大概只能往下 30 層。  
往下的層數非常少，根本沒辦法影響上樓次數的上限。  

實際上能停留樓層大概只有 30 \* 30 種左右而已。  

---

試舉從起點上樓 2 次、下樓 1 次的方法：  

- 下上上  
- 上下上  
- ...

移動順序不同，但是最終停留的樓層、jump 值和下樓限制都相同。  
有重疊的子問題，因此考慮 dp。  

---

定義 dp(i, jump, back = 0/1)：已上樓次數為 jump，從 i 層出發抵達 k 層的方案數。back 為 1 代表可以下樓。  
轉移：若 i = k 則答案加 1。除此之外還得加上下樓兩種操作：  

- 上樓：j = i + (2 ^ jump)，因為不可連續下樓，限制 j <= k + 1，否則不可能抵達終點。
    dp(j, jump + 1, 1)
- 下樓：back 必須為 1 才能下樓。  
    dp(i - 1, jump, 0)  

出發點固定是 1 層，答案入口為 dp(1, 0, 1)。  

時間複雜度 O((log k) ^ 2)。  
空間複雜度 O((log k) ^ 2)。  

```python
class Solution:
    def waysToReachStair(self, k: int) -> int:
        
        @cache
        def dp(i, jump, back): # back = 0/1
            res = 1 if i == k else 0
            
            # up
            j = i + (1 << jump)
            if j <= k + 1: 
                res += dp(j, jump + 1, 1)
                
            # back
            if i > 0 and back == 1:
                res += dp(i - 1, jump, 0)
            return res
        
        return dp(1, 0, 1)
```
