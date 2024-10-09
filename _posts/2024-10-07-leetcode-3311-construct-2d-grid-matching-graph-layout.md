---
layout      : single
title       : LeetCode 3311. Construct 2D Grid Matching Graph Layout
tags        : LeetCode Hard
---
weekly contest 418。  

## 題目

輸入二維整數陣列 edges，代表 n 節點的無向圖，其中 edges[i] = [u<sub>i</sub>, v<sub>i</sub>]，代表 u<sub>i</sub> 和 v<sub>i</sub> 之間存在一條邊。

構造一個滿足以下條件的二維矩陣：  

- 矩陣中每個格子正好對應 0 倒 n - 1 的所有節點  
- **若且唯若**兩個節點在 edges 中有連邊，則對應的兩個格子在舉陣中相鄰 (**橫豎皆可**)  

題目保證至少有一個矩陣可以滿足條件。  
回傳任意一種滿足條件的矩陣。  

## 解法
