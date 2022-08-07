--- 
layout      : single
title       : LeetCode 2365. Task Scheduler II
tags        : LeetCode Medium HashTable Simulation
---
雙周賽84。總感覺這題放到Q2比較合適，畢竟就只是照題目說的做。

# 題目
輸入正整數陣列tasks，表示需要**依序**完成的任務，其中tasks[i]表示第i個任務的類型。  
另外還有整數space，代表完成某任務後，必須間隔的最少天數，才能再次進行相同類型的任務。  

每一天你可以：  
- 完成當前的任務  
- 或是休息一天  

求完成所有任務所需的最少天數。  

# 解法
本來還想說要自己調整工作順序，結果只能循序，那就簡單多了。  

維護雜湊表d，紀錄每類型工作要等到哪天之後才能進行。因為一開始都沒有冷卻，所以初始值都是0。  
變數day代表當前天數。遍歷tasks中所有任務t，若當前天數無法進行t類工作，則直接休息到可以做的那天為止。  
然後更新t類間隔時間，進入下一天。遍歷完之後，直接回傳day就是答案。  

```python
class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        d=Counter()
        day=0
        
        for t in tasks:
            day=max(day,d[t])
            d[t]=day+space+1
            day+=1
            
        return day
```

