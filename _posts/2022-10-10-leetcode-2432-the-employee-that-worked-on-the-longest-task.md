--- 
layout      : single
title       : LeetCode 2432. The Employee That Worked on the Longest Task
tags        : LeetCode Easy Array Greedy
---
周賽314。沒看清楚題目WA了一次，尷尬。  

# 題目
有n個員工，員工id分別為0\~n-1。  

輸入一個2D整數陣列logs ，其中logs[i] = [idi, leaveTimei]，且：  
- id<sub>i</sub>是從事第i個任務的員工id，且  
- leaveTime<sub>i</sub>是員工完成第i個任務的時間。所有leaveTime<sub>i</sub>的值都是**唯一的**  

注意，第i個任務在第(i-1)個任務結束後立即開始，而第0個任務在時間0開始。  
求完成任務時間最長的員工的id。如果有多個員工之間存在平局，則回傳其中的最小id。  

# 解法
總覺得題目描述有點爛，我是直接看例題才搞懂在幹嘛。  

每個員工都是循序排隊進行工作的，第一個員工從時間0開始，結束後，下一位員工馬上無縫接軌。  
只要當前工作時間大於先前最大值，又或是時間相同、但id較小，則更新答案。  

時間複雜度O(N))，空間複雜度O(1)。  

```python
class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        curr=0
        mx=0
        ans=None
        
        for id,end in logs:
            t=end-curr
            curr=end
            if t>mx or (t==mx and id<ans):
                ans=id
                mx=t
            
        return ans
```
