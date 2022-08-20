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

最多需要將N個加油站放入heap，每次O(log N)，整體時間複雜度O(N log N)，空間(N)。  

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

雖然說DP可以解這題，但複雜度O(N^2)，而且個人認為不太直觀，基於學習心態還是來做做看。  

定義dp(i,refuel)：到第i個加油站為止，共加refuel次油可以抵達的最遠距離。  
轉移方程式：每個加油站可以選擇加或不加。不加的話就是dp(i-1,refuel)；加的話要確認上次位置dp(i-1,refuel-1)，能夠抵達第i站才加上第i站的油料。  
base cases：加油次數為0，代表初始油量，回傳startFuel；加油次數大於加油站數，為非法狀態，回傳-inf確保答案不被使用。  

總共有N個站點，所以可以選擇加0次\~N次油。遍歷0\~N，若可以抵達target則回傳該加油次數；都沒辦法的話回傳-1。  

```python
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        N=len(stations)
        
        @cache
        def dp(i,refuel):
            if refuel==0:return startFuel
            if refuel>i+1:return -inf
            best=dp(i-1,refuel)
            last=dp(i-1,refuel-1)
            if last>=stations[i][0]:
                best=max(best,last+stations[i][1])
            return best
        
        for i in range(N+1):
            if dp(N-1,i)>=target:
                return i
            
        return -1
```