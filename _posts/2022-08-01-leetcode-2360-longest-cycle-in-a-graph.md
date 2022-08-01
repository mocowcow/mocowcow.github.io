--- 
layout      : single
title       : LeetCode 2360. Longest Cycle in a Graph
tags        : LeetCode
---
周賽304。跟Q3內容幾乎一樣，還以為是我看錯。當時第一個想法是**時間戳**，可惜時間剩下5分鐘，不夠我做出來。  
後來確認這方法確實可行，代表我有在前幾次的周賽中吸收到新知，算是有成長。  

# 題目
輸入一個n節點的有向圖，節點編號從0到n-1，每個節點最多有一條出邊。  
另有長度為n的整數陣列edges，其中edges[i]代表節點i的到edges[i]存在一條有向出邊。若沒有出邊則edges[i]為-1。  

求圖中最長循環的長度。如果無循環則回傳-1。  

循環指的是在同一點出發與結束的路徑。  

# 解法
之前在[2322. minimum score after removals on a tree]({% post_url 2022-06-28-leetcode-2322-minimum-score-after-removals-on-a-tree %})使用的時間戳，在這次也派上用場。  

維護陣列time_in紀錄各節點首次訪問的時間點，以及變數time表示當前時間。  
遍歷每個節點i，若尚未訪問過則進行dfs：  
- 首先將dfs開始時間點start設為當前時間time，以判斷節點是否以前就處理過  
- 從i開始不斷往下走，直到沒路或是抵達訪問過的節點時停止  
- 若抵達訪問過的節點，則檢查當前節點curr的首次訪問時間是否大於等於start。若為真則代表發現循環，以循環大小更新答案

```python
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        N=len(edges)
        ans=-1
        time=0
        time_in=[-1]*N
        
        for i in range(N):
            if time_in[i]!=-1:
                continue
            start=time
            curr=i
            while curr!=-1: 
                if time_in[curr]!=-1:
                    if time_in[curr]>=start:
                        ans=max(ans,time-time_in[curr])
                    break
                time_in[curr]=time
                time+=1
                curr=edges[curr] 

        return ans
```

用continue和break有點醜，將條件整理之後變得比較好看。  

```python
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        N=len(edges)
        ans=-1
        time=0
        time_in=[-1]*N
        
        for i in range(N):
            start=time
            curr=i
            while curr!=-1 and time_in[curr]==-1: 
                time_in[curr]=time
                time+=1
                curr=edges[curr]
            if curr!=-1 and time_in[curr]>=start:
                ans=max(ans,time-time_in[curr])
                          
        return ans
```
