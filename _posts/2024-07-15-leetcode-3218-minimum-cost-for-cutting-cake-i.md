---
layout      : single
title       : LeetCode 3218. Minimum Cost for Cutting Cake I
tags        : LeetCode
---
周賽 406。

## 題目

有個 m x n 的蛋糕需要切成數塊 1 x 1 的小塊。  

輸入整數 m, n，還有兩個陣列：  

- 大小為 m - 1 的 horizontalCut，其中 horizontalCut[i] 代表在第 i 條水平線分割的成本  
- 大小為 n - 1 的 verticalCut，其中 verticalCut[j] 代表在第 j 條垂直線分割的成本  

每次操作，你可以任選一塊不為 1 x 1 大小的蛋糕，並且：  

- 在第 i 條水平線分割，成本為 horizontalCut[i]  
- 在第 j 條垂直線分割，成本為 verticalCut[j]  

每次分割操作後，蛋糕都會變成兩塊獨立的小蛋糕，且分割成本不會改變。  

求把所有蛋糕切成 1 x 1 的**最低成本**。  

## 解法
