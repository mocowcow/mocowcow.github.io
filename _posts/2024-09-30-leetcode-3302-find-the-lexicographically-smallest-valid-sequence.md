---
layout      : single
title       : LeetCode 3302. Find the Lexicographically Smallest Valid Sequence
tags        : LeetCode Medium
---
biweekly contest 140。  

## 題目

輸入兩個字串 word1 和 word2  

若一個字串 x 在修改**至多一個**字元後等同於字串 y，則稱 x 和 y **幾乎相等**。  

若一個索引序列 seq 滿足以下條件，則稱為**合法**：  

- 索引是遞增排序。  
- 將 word1 中這些索引對應的字元**依序**串接起來，可得到一個與 word2 **幾乎相等**的字串。  

回傳長度為 word2.length 的陣列，代表一個**字典序最小**的**合法**索引序列。若不存在則回傳空陣列。  

注意：答案是回傳索引序列，而不是其對應的字串。  

## 解法

