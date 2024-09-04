---
layout      : single
title       : LeetCode 3277. Maximum XOR Score Subarray Queries
tags        : LeetCode Hard
---
weekly contest 413。看到位運算我就往**拆位**的方向去思考。方向錯誤當然是沒想出答案。  

## 題目

輸入長度 n 的整數陣列 nums，還有長度 q 的二維整數陣列 queries，其中 queries[i] = [l<sub>i</sub>, r<sub>i</sub>]。  

每次查詢，你必需找到 nums[l<sub>i</sub>..r<sub>i</sub>] 的任意**子陣列**的**最大 XOR 分數**。  

**XOR 分數**指的是一個陣列 a 不斷執行以下操作，直到剩下一個元素，該元素就是分數：  

- 除了最後一個 a[i] 以外，同時將所有 a[i] 的值改成 a[i] XOR a[i + 1]。  
- 刪除 a 的最後一個元素。  

回傳長度 q 的陣列 answer，其中 answer[i] 是第 i 次查詢的答案。  

## 解法
