---
layout      : single
title       : LeetCode 3288. Length of the Longest Increasing Path
tags        : LeetCode Hard
---
biweekly contest 139。  
這題就有點坐牢，沒做過原題大概想不出來，做過直接秒殺。  

## 題目

輸入長度 n 的二維整數陣列 coordinates，還有整數 k。其中 0 <= k < n。  
coordinates[i] = [x<sub>i</sub>, y<sub>i</sub>] 代表二維平面中的一個點。  

一條長度 m 的遞增路徑由點 (x1, y1), (x2, y2), (x3, y3), ..., (xm, ym) 組成，滿足：  

- 對於所有滿足 1 <= i < m 的 i 都有 x<sub>i</sub> < x<sub>i+1</sub> 且 y<sub>i</sub> < y<sub>i+1</sub>。  
- 對於所有 1 <= i <= m 的點 i 的座標 (x<sub>i</sub>, y<sub>i+1</sub>) 都在 coordinates 中。  

求包含座標 coordinates[k] 的**最長上升路徑**。  

## 解法

