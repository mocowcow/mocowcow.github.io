--- 
layout      : single
title       : LeetCode 2402. Meeting Rooms III
tags        : LeetCode Hard Array Simulation Heap
---
周賽309。相似題[1606. find servers that handled most number of requests]({% post_url 2022-05-25-leetcode-1606-find-servers-that-handled-most-number-of-requests %})。沒有排序吃一個WA，好慘。  

# 題目
輸入整數n，代表有n個房間，編號從0\~n-1。  
輸入二維整數陣列meeting，其中meeting[i] = [starti, endi]，表示會議在左閉右開區間[starti, endi)舉行。所有starti的值都是唯一的。  

依照以下規則分配會議室：  
- 優先使用編號最小的空房  
- 如果沒有可用的房間，會議要延遲到有房間空出才舉行，但是持續時間與原本相同  
- 若有多個被延遲的會議，由原定時間最早的會議優先舉行  

求舉行**最多次會議的房間號碼**，若有多個房間相同，則回傳編號較小者。  
左閉右開區間[a, b)指的是包含a\~b-1的區間。

# 解法
這題要處理的細節雖然比較多，但是分開處理都不算太難。  
- 優先使用編號小的空房，可以用min heap  
- 占用的房要依結束時間順序彈出，也是min heap  
- 被延遲的會議，依原定時間順序執行，要排序
- 被延遲的會議，持續時間不變，要求出會議持續時間  

首先將meetings排序，將原本的(開始, 結束)轉換成(開始, 持續時間)。  
而一開始所有房間都是空的，所以將0\~n-1的房間放入最小堆疊heap中；反之busy初始為空。  
還需要一個陣列cnt計算房間使用計數，還有變數time維護當前時間。  

開始模擬開會排隊過程，遍歷排序好的會議：  
- 將時間time更新到會議開始時間  
- 如果沒有空房，也沒有結束的會議，則**將時間快進**到第一個會議結束時間  
- 開始釋放已經結束的會議，把房間放回free  
- 選擇號碼最小的空房，計數+1，算出結束時間丟進busy  

最後從cnt找出使用最多次的房間就好。  

房間n最多100，會議m最多500000。每個會議進出heap共2\*m次，每次複雜度O(log m)。會議室總共也會進出共2\*m次，每次複雜度(log n)。  
加上排序會議的O(m log m)，還有轉換會議時間的O(m)，整體複雜度O(m log m)+O(m)+O(m log(n+m))，應該可以簡化成O(m log m)。  

```python
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        mts=[[s,e-s]for s,e in meetings]
        cnt=[0]*n
        free=[]
        busy=[] # [end, room_id]
        time=0

        for i in range(n):
            heappush(free,i)
        
        for start,cost in mts:
            time=max(time,start)
            if not free and busy[0][0]>time:
                time=busy[0][0]
            # release finished room
            while busy and time>=busy[0][0]:
                ok_room=heappop(busy)[1]
                heappush(free,ok_room)
            # add room
            go_room=heappop(free)
            heappush(busy,[time+cost,go_room])
            cnt[go_room]+=1
            
        ans=None
        mx=-inf
        
        for i,n in enumerate(cnt):
            if n>mx:
                mx=n
                ans=i
                
        return ans
```
