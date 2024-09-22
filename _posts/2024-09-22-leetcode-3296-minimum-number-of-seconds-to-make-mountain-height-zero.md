---
layout      : single
title       : LeetCode 3296. Minimum Number of Seconds to Make Mountain Height Zero
tags        : LeetCode Medium
---
weekly contest 416。  
滿有趣的二分二分題。  

## 題目

輸入整數陣列 mountainHeight，代表一座山的高度。  
另外還有整數陣列 workerTimes，代表每個工人的工作耗時 (以秒計)。  

所有工人**同時**進行挖山工程。對於工人 i：  

- 若想將山的高度減少 x，則須 workerTimes[i] + workerTimes[i] \* 2 + ... + workerTimes \* x 秒。例如：  
  - 減少高度 1，需要 workerTimes[i] 秒。  
  - 減少高度 2，需要 workerTimes[i] + workerTimes[i] \* 2秒，以此類推。  

求將山的高度減少至 0 所需的**最小秒數**。  

## 解法

關鍵字：工人**同時**工作。  
若有數個工人分別耗時 x1, x2, x3,.. 秒，則總工程耗時為 max(x1, x2, x3,..)，以**最大者**為準。  

而為了使最大時間盡可能小，即**最大值最小化**，根據經驗通常可以**二分答案**。  
並且，若在 x 秒可以完成工作，則 x+1 秒也可以；若 x 不行，則 x-1 也不行。  
答案具有單調性，確定可以二分答案。  

---

維護含數 ok(limit)，判斷能否在 limit 秒內完成工作。  
需要遍歷每個工人，分別算出他們在 limit 秒內**能夠減少的高度**。  
若減少總高度 cnt 大於等於 mountainHeight 則合法。  

另一個問題來了，怎麼知道工人在特定時間內可以減多少高度？  

---

答案還是二分。  

工人的耗時公式是**等差級數和**，再乘上其基本耗時。  
若在 limit 秒內能減少高度 x，則減少 x-1 肯定也合法；反之，x 不合法，則 x+1 也不合法。  
答案具有單調性，可以二分。  

注意：兩次二分的**邊界更新邏輯不同**，取中位數時注意補 1。  
