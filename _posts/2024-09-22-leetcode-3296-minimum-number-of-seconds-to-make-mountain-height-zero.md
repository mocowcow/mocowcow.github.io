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
