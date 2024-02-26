---
layout      : single
title       : LeetCode 3049. Earliest Second to Mark Indices II
tags        : LeetCode
---
周賽386。看起來上一題有點像，但邏輯幾乎不一樣。  

## 題目

輸入**索引從 1 開始**的整數陣列 nums 和 changeIndices，兩者大小分別為 n 和 m。  

起初，nums 中的所有索引都是**未標記**的，而你必須要標記他們。  
依序從 1\~m 中的第 s 秒，你可以執行以下操作**之一**：  

- 選擇 [1, n] 之間的索引 i，並使 nums[i] 減 1  
- 將 nums[changeIndices[s]] 設成任意的**非負**整數  
- 選擇 [1, n] 之間的索引 i，如果 nums[i] 等於 0，則標記索引 i
- 不做任何事  

求 [1, m] 之間的一個整數，代表在最佳情況下，能夠標記**所有**索引的**最早秒數**。若無法全部標記則回傳 -1。  

## 解法

```python
code here

```
