---
layout      : single
title       : LeetCode 3310. Remove Methods From Project
tags        : LeetCode Medium
---
weekly contest 418。  
這題意描述挺模糊的，原文是真的看不太懂。  

## 題目

你在維護一個專案，其中有 n 個方法，編號分別從 0 到 n - 1。  

輸入兩個整數 n 和 k，還有二維整數陣列 invocations，其中 invocations[i] = [a<sub>i</sub>, b<sub>i</sub>]，代表方法 a<sub>i</sub> 調用方法 b<sub>i</sub>。  

已知方法 k 有 bug。  
方法 k 本身以及其**直接**或**間接**調用的方法，都視作**可疑**的方法，需要把他們都移除掉。  
若一群互相調用的方法**群組**內都是可疑的，才能把他們移除。  

以任意順序回傳移除**可疑方法**後剩餘的方法。若無法移除則**不必**移除。  

## 解法
