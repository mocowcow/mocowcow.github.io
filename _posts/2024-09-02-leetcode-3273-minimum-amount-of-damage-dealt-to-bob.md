---
layout      : single
title       : LeetCode 3273. Minimum Amount of Damage Dealt to Bob
tags        : LeetCode Hard
---
biweekly contest 138。非常妙的題，答案很好猜，但卻不好證明。  

## 題目

輸入整數 power 和兩個長度 n 的整數陣列 damage 和 health。  

Bob 有 n 個敵人，其中敵人 i 若存活 (health[i] > 0)，則每秒對 Bob 造成 damage[i] 傷害。  
在每秒敵人攻擊 Bob **後**，Bob 可以選擇其中**一個**活著的敵人，並對他造成 power 傷害。  

求 Bob 擊敗**所有**敵人時，**最少**需要承受幾點傷害。  

## 解法

對於多個敵人，必需連續**打同一個敵人**直到擊殺為止。因為分散攻擊只會使敵人的存活時間更長。  
敵人的實際存活時間是 ceil(health[i] / power)。  

再看測資範圍很大，光是維護存活的狀態就很麻煩，也不可能是 dp。  
那肯定有一種規則可以排序。  

---

若有兩個敵人，存活時間和攻擊分別是 t1, d1 和 d2, d2。  

- 方案一：先殺第一個，受到的總傷害是 t1\*d1 + t1\*d2 + t2\*d2。  
- 方法二：先殺第二個，受到的總傷害是 t2\*d1 + t2\*d2 + t1\*d1。  

若方案一優於方案二，則有：  
> t1\*d1 + t1\*d2 + t2\*d2 < t2\*d1 + t2\*d2 + t1\*d1  

整理後得到：  
> t1\*d2 < t2\*d1  

按照此公式可以比較出兩個敵人優先殺誰。  
