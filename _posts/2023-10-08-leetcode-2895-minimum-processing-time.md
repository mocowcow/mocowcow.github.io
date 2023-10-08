---
layout      : single
title       : LeetCode 2895. Minimum Processing Time
tags        : LeetCode Medium Array Sorting Greedy Stack
---
周賽366。有點像之前某次Q4的什麼花園種花題。  

## 題目

你有n個處理器，每個處理器各有4個核心，還有n \* 4個任務等你分配，每個核心只需要處理**一個**任務。  

輸入整數陣列processorTime，代表各處理器變為可用的時間點。  
整數陣列tasks則代表各任務所需的執行時間。  

求執行完所有任務的**最小時間**。  

## 解法

為了盡早完成所有任務，耗時較長的任務則應較早執行。  
將兩個陣列都排序。  

一個處理器有4核心，所以可以解4個任務，以開始時間+耗時更新答案。  

時間複雜度O(N log N)。  
空間複雜度O(1)。  

```python
class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        pt=processorTime
        pt.sort()
        tasks.sort()
        ans=0
        
        for x in pt:
            for _ in range(4):
                ans=max(ans,x+tasks.pop())
                
        return ans
```
