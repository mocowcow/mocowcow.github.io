---
layout      : single
title       : LeetCode 3149. Find the Minimum Cost Array Permutation
tags        : LeetCode
---
周賽 397。同一場竟然有三題都是 dp，根本 dp 大賽。  

## 題目

輸入陣列 nums，他是陣列 [0, 1, 2, ..., n - 1] 的排列。該排列的分數定義為：  

- score(perm) = \|perm[0] - nums[perm[1]]\| + \|perm[1] - nums[perm[2]]\| + ... + \|perm[n - 1] - nums[perm[0]]\|

回傳**分數最小**的排列。若有多種排列的分數相同，則回傳**字典序**最小者。  

## 解法

這種枚舉選擇順序的題型，大多數都可以用 bitmask dp 解決。  
但 score 關係到**上一個數**是什麼，最後一段的甚至要用到**第一個數**。  
使用額外的變數表示狀態，得到 dp(mask, prev, first)。  

但每個狀態轉移需要枚舉 N 個數，共有 (2^N) \* N^2 個狀態，複雜度是 O((2^N) * (N^3))。  
代入 N = 14 的計算量大概是 5e7。乍看之下會超時，但是考慮到一些無效的狀態，好像又不會超時，非常神秘。  

---

以下簡稱 prem 為 p。  
仔細觀察 score，發現他是一個**循環**的關係。試著將 nums 也循環移動看看。  
例如：  
> nums = [0, 1]  
> score = abs(p[0] - nums[p[1]]) + abs(p[1] - nums[p[0]])  
> score = abs(0 - 0) + abs(1 - 1)

把 nums 向右移動一格看看：  
> nums = [1, 0]  
> score = abs(p[0] - nums[p[1]]) + abs(p[1] - nums[p[0]])  
> score = abs(1 - 1) + abs(0 - 0)  

絕對值的內容完全一樣，只是出現順序不同罷了。  
也就是說，每種排法都可以任意**平移出現順序**，而不改變分數。  
因題目要求**最小字典序**，所以**第一個數保證是 0**。  

這樣一來狀態就變成 dp(mask, prev)，複雜度降到 O((2^N) * (N^2))。  
計算量大概是 3e6，直接少掉一個 0。  

---

```python
code here

```
