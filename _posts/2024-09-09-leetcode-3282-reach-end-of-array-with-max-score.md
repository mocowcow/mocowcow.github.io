---
layout      : single
title       : LeetCode 3282. Reach End of Array With Max Score
tags        : LeetCode Medium
---
weekly contest 414。  
感覺最近常常出這種直覺秒殺題，如果認真思考反而會掉入陷阱。  

## 題目

輸入長度 n 的整數陣列 nums。  

你必需從索引 0 出發並抵達索引 n - 1。  
你只能跳到比當前**更大**的索引。  

從索引 i 跳到索引 j 獲得的**分數**為 (j - i) \* nums[i]。  

求抵達最後一個索引的**最大總分**。  

## 解法
