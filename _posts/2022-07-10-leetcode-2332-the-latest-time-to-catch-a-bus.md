--- 
layout      : single
title       : LeetCode 2332. The Latest Time to Catch a Bus
tags        : LeetCode Medium Array HashTable
---
雙周賽82。區區一個Q2卡了超過一小時，剩下時間根本不夠弄Q3、Q4，這次排名完蛋了。  
提交AC率也才13%，這題是真的兇殘。  

# 題目
輸入長度為n整數陣列buses，其中bus[i]表示第i台車的出發時間。還有長度為m整數陣列passengers，其中passengers[j]表示第j個乘客的抵達時間。所有車的發車時間和乘客的底達時間都是獨一無二的。  
整數capacity代表每輛公車的最大載客數。  

如果乘客在y分抵達，巴士在x分出發，若y<=x則可以上車。越早抵達的乘客越優先上車。  
求最晚何時要抵達公車站，才能順利上車。其他乘客的抵達時間已經固定，你**不能選擇跟其他人同樣的時間**到達。  

# 解法
這個問題很麻煩，本來看到passengers[i]高達10^9，想說要二分搜，但是每一台公車又不一定裝得滿人，很難實現。  
雖然buses和passengers都是10^5，但是實際上受限於乘客數，均攤分析後複雜度還是10^5，那麼就可以直接模擬上車過程。  

公車和乘客都是無序的，必須先手動排序。  
乘客裝入佇列p方便取用，另外維護集合used來記錄那些時間點已經被占用。  
因為其他乘客最早抵達時間是2，所以ans初始化為1。  

開始遍歷每台車，每車有capacity個位置，若有排隊的乘客就讓他上車，直到坐滿或是沒乘客。每當有人在temp時間點上車，先將其標記為已占用，再檢查temp-1是否被占用，若否則代表可以在他前方插隊，更新ans為temp-1。  
如果車沒有坐滿人，最後一刻也沒被占用，那最後一刻抵達就好，更新ans為最後出發時間。  

```python
class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        p=deque(passengers)
        used=set()

        ans=1
        for time in buses:
            k=capacity
            while k and p and p[0]<=time:
                k-=1
                temp=p.popleft()
                used.add(temp)
                if temp-1 not in used:
                    ans=temp-1
            if k>0 and time not in used:
                ans=time
        
        return ans
```
