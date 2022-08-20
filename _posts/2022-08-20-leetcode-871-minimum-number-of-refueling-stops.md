--- 
layout      : single
title       : LeetCode 871. Minimum Number of Refueling Stops
tags        : LeetCode Hard Array DP Greedy Heap
---
每日題。第一眼覺得可以DP，想想發現貪心更好，3分鐘就解決了。後來想用DP來解，想了兩個小時才想通。  

# 題目
有一台車朝著相同的方向前行，直到抵達目的地為止。  

途中有一些加油站。加油站表示為一個陣列stations，其中stations[i] = [positioni,fueli]代表第i個加油站位於positioni英里處，且可以補充fueli公升的汽油。  

假設汽車的油箱容量無限，最初只有startFuel公升油料。每移動1英里消耗1公升汽油。抵達加油站時，可以將所有站內的汽油加進油箱中。  

回傳汽車抵達目的地**最少需要加油幾次**。若無法抵達則回傳-1。  

注意，若抵達加油站時，剩餘油料為0，依然可以加油並繼續。同理，剩餘油量為0抵達目的地視為成功。  

# 解法
要保持最少的加油次數，那就等油不夠的時後在加就好。  
為了降低加油次數，那麼每次加油都要選擇油量最大的站。  

維護變數curr代表目前的距離，考慮到初始的油料，所以直接設為startFuel。  
還有一個max heap記做h，將所有站點以油料多寡遞減排序。  

重覆以下動作直到抵達目的地為止：  
- 把所有可用的加油站放入h中  
- 選擇最多油的站點來加油，次數+1；沒有站點則回傳-1  
- 繼續移動

```python
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        h=[]
        q=deque(stations)
        curr=startFuel
        ans=0
        
        while curr<target:
            while q and q[0][0]<=curr:
                refuel=q.popleft()[1]
                heappush(h,-refuel)
            if not h:
                return -1
            curr+=-heappop(h)
            ans+=1
        
        return ans
```