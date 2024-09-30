---
layout      : single
title       : LeetCode 3307. Find the K-th Character in String Game II
tags        : LeetCode Hard
---
weekly contest 417。  

## 題目

Alice 和 Bob 在玩遊戲。最初 Alice 有一個字串 word = "a"。  

輸入正整數 k，還有整數陣列 operations，其中 operations[i] 代表第 i 次操作的種類。

Bob 要求 Alice 依序執行所有操作：  

- 若 operations[i] = 0，將 word 的**副本**附加至原始的 word。  
- 若 operations[i] = 1，將 word 的每個字元**替換**成英文字母表中**下一個**來生成新字串，並將其**附加**至原始的 word。  

例如："c" 操作後得到 "cd"；zb" 操作後得到 "zbac"。  
注意：第二種操作中，字元 'z' 替換後會變成 'a'。  

在執行操作後，回傳 word 中第 k 個字元。  

## 解法
