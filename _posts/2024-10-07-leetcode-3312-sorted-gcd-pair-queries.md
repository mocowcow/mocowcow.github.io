---
layout      : single
title       : LeetCode 3312. Sorted GCD Pair Queries
tags        : LeetCode Hard
---
weekly contest 418。  

## 題目

輸入長度 n 的整數陣列 nums，還有整數陣列 queries。  

gcdPairs 陣列是由 nums 中所有滿足 0 <= i < j < n 的數對 (nums[i], nums[j]) 的 gcd 升序排序而成。  

對於每個查詢 queries[i]，你必須找到 gcdPairs 中索引為 queries[i] 的元素。  

回傳整數陣列 answer，其中 answer[i] 為 gcdPairs[queries[i]] 的值。  

## 解法
