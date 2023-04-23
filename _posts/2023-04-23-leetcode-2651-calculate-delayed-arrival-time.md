--- 
layout      : single
title       : LeetCode 2651. Calculate Delayed Arrival Time
tags        : LeetCode Easy
---
周賽342。史上最簡單的Q1，簡單到以為有鬼。  

# 題目
You are given a positive integer arrivalTime denoting the arrival time of a train in hours, and another positive integer delayedTime denoting the amount of delay in hours.

Return the time when the train will arrive at the station.

Note that the time in this problem is in 24-hours format.

輸入正整數arrivalTime代表火車的抵達時刻，而正整數delayedTime代表火車延後的時間。  

求火車實際抵達的時間點。  

注意：時間以24小時制表示。  

# 解法
直接拿預計時間加上延後時間。有可能會超過24小時，記得對24取餘數。  

時間複雜度O(1)。空間複雜度O(1)。  

```python
class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime+delayedTime)%24
```
