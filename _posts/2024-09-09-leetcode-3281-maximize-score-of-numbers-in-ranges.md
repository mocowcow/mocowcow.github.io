---
layout      : single
title       : LeetCode 3281. Maximize Score of Numbers in Ranges
tags        : LeetCode Medium
---
weekly contest 414。  

## 題目

輸入整數陣列 start，還有整數 d，代表有 n 個區間 [start[i], start[i] + d]。  

對於每個區間，你必需選擇一個區間內的整數。  
所選整數中任意兩者的**最小**絕對差則叫做**分數**。  

求可能的**最大**分數。  

## 解法

start 長度上限 1e5，要暴力枚舉肯定不可能。  

有以下幾個線索：  

- 根據經驗，**最小值最大化**通常適用**二分搜**。  
- start[i] 的選擇順序並不影響答案，可以排序。  
- 若 score = x 合法，則必定可以找到不小於 x 的合法分數，答案具有**單調性**。  

因此考慮**二分答案**。  

---

維護函數 ok(score) 判斷是否存在分數**大於等於** score 的選法。  

絕對差的最小值為 0，下界為 0。  
在 d = start[i] 上限 1e9 時，所能選擇的最大整數為 2e9，上界為 2e9。  
若 mid 不合法，嘗試更小的分數，更新上界為 mid - 1；若合法則更新下界為 mid。  
