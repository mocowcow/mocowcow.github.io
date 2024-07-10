---
layout      : single
title       : LeetCode 3213. Construct String with Minimum Cost
tags        : LeetCode
---
周賽 405。  
這題也是很神秘，測資範圍 N = 5e4，依我經驗一看就覺得 python 寫很容易出事。  
一般來說測資超過 1e4 之後，O(N^2) 的做法都會超時。  
但因為少了最極端的測資，不少人交 O(N^2) 答案竟然過了，甚至賽後看到官方提示也是叫人家用這種作法。  

如果說本來就預期 O(N^2) 解，那就是測資範圍設錯，誤導作題者。但是 8 分難度好像又配不上。
如果說測資強度太差，有些人交了 O(N sqrt(N)) 正確答案卻又超時，真的是魔法遊戲。  

## 題目

輸入字串 target，字串陣列 words，還有整數陣列 costs。兩個陣列的長度都相同。  

最初存在一個空字串 s。  
你可以執行以下操作任意次：  

- 選擇 [0, words.length - 1] 之間的索引  
- 將 words[i] 加入 s 後方  
- 成本增加 costs[i]  

求使得 s 等於 target 的最小成本。若不可能則回傳 -1。  

## 解法
