---
layout      : single
title       : LeetCode 3303. Find the Occurrence of First Almost Equal Substring
tags        : LeetCode Hard
---
biweekly contest 140。  
我搞了半天的 rolling hash 竟然被卡常數，真搞不懂時間限制的標準。  

## 題目

輸入兩個字串 s 和 pattern。  

若一個字串 x 在修改**至多一個**字元後等同於字串 y，則稱 x 和 y **幾乎相等**。  

回傳**最小**的 s 的子字串起始索引，其子字串與 pattern **幾乎相等**。  
若不存在則回傳 -1。  

## 解法

修改 pattern **至多一個**字元，可能的結果有 pattern 本身，或是任意 pattern[i] 修改成任意字母。  
總共 26 \* N = 2e6 種可能。  

透過 rolling hash 將所有可能的子字串加入集合中，最後再枚舉 s 中的子字串，第一個找到的就是答案。  
可惜會超時，只能想想別的辦法。  
