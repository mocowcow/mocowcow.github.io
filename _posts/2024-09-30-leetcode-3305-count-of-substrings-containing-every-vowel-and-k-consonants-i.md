---
layout      : single
title       : LeetCode 3305. Count of Substrings Containing Every Vowel and K Consonants I
tags        : LeetCode Medium
---
weekly contest 417。  

## 題目

輸入字串 word 和非負整數 k。  

求有多少**子字串**滿足每個母音出現**至少**一次，且有**正好** k 個子音。  

## 解法

看到**子字串**就會想到**滑動窗口**。  

上週的滑窗問題 [3297. count substrings that can be rearranged to contain a string i]({% post_url 2024-09-22-leetcode-3297-count-substrings-that-can-be-rearranged-to-contain-a-string-i %})。  
該題是求**至少**滿足某些條件。枚舉右端點 right，並在條件滿足時收縮左端點 left。  
因為只有在**滿足時才收縮 left**，因此 left-1 肯定是合法的。故 [0, left-1] 都是合法的左端點。  

但本題還有**正好** k 個子音的限制，雖然能確定 left-1 合法，但卻不知道 left-2 是母音還是子音，不確定是否合法。  
