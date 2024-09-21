---
layout      : single
title       : LeetCode 45. Jump Game II
tags        : LeetCode Medium
---

比賽有碰到這題的強化版，趕快來補題解。  

## 題目

輸入長度 n 的整數陣列 nums。你最初位於 nums[0]。  

每個元素 nums[i] 代表你最多可以從 i 跳躍的步數。  
也就是說，若你位於 nums[i]，則可以跳到任意 nums[i + j]，滿足：  

- 0 <= j <= nums[i]  
- 且 i + j < n  

求跳到 nums[n - 1] 所需的**最少步數**。  
題目保證一定能抵達 nums[n - 1]。  

## 解法
