--- 
layout      : single
title       : LeetCode 2532. Time to Cross a Bridge
tags        : LeetCode Hard Array Simulation Heap
---
周賽327。這題是真的麻煩，~~拖到最後10分鐘才解決~~。又被rejudge掉，好慘啊。  

# 題目
有k個工人要將n個箱子從舊倉庫搬到新倉庫。有一條河將倉庫分隔，新倉庫在左側，舊倉庫在右側，中間只有一座橋能夠通行。  

輸入整數n和k，還有一個二維整數陣列time，其中time[i] = [leftToRight<sub>i</sub>, pickOld<sub>i</sub>, rightToLeft<sub>i</sub>, putNew<sub>i</sub>]。    

一開始所有工人都在左岸等待。每個工人若要搬運箱子，必須：  
- 從左側過橋到右側，耗時leftToRight<sub>i</sub>  
- 從舊倉庫找箱子，耗時pickOld<sub>i</sub>  
- 從右側過橋回到左側，耗時rightToLeft<sub>i</sub>  
- 把箱子放到新倉庫，耗時putNew<sub>i</sub>  

若滿足以下任一條件，則認為工人i的**效率低於**工人j：  
- leftToRight<sub>i</sub> + rightToLeft<sub>i</sub> > leftToRight<sub>i</sub> + rightToLeft<sub>i</sub>  
- leftToRight<sub>i</sub> + rightToLeft<sub>i</sub> == leftToRight<sub>i</sub> + rightToLeft<sub>i</sub> 且 i > j  

工人過橋時需要遵循以下規則：  
- 一次只能有一個人過橋，其他人需要在橋邊等待  
- 若橋上沒人，右側的人優先。若右側有多人，則以**效率最低**者優先  
- 若橋上沒人，右側也沒人在等，則輪到左側的人座橋。若左側有多人，則以**效率最低**者優先  

所有n個箱子都要搬到新倉庫，求最後一個工人**抵達左側的時間**。  

# 解法
這名詞和變數真的是很多，統一整理一下重點：
1. 左側=新倉庫、右側=舊倉庫  
2. 搬一次要從左往右、再從右往左回來  
3. 一次只能一人過橋  
4. 右邊有人的話優先  

有兩個容易忽略的陷阱：  
1. 答案要的是最後一個工人**抵達時間**，不必等他放完箱子  
2. 工人是以**效率低**者優先，不是先來先搬  

對於每一側需要兩個heap，一個維護所有閒置的工人，以低效率者優先。另一個維護正在搬箱子的工人，以結束時間較早者優先。  
開始循環直到右方沒有箱子，也沒有任何人為止：  
1. 在左側倉庫忙完的工人，讓他回去左側排隊  
2. 在右側倉庫忙完的工人，讓他回去右側排隊  
3. 如果右側有人在排隊，則讓右側**最低效率者**先走  
4. 如果右側沒人，左側有，就讓左側**最低效率者**先走    
5. 如果兩側都沒人排隊，代表所有工人都在倉庫裡面忙，直接把時間快進，讓兩側**最早忙完**的人出來  

在工人過橋時，直到他抵達為止，橋都是不可用的，直接把當前直接快進到其**抵達時間**。  
而左側往右邊走時，需直接將箱子數減一，避免多餘的人走過去；右側往回走時，直接以抵達時間更新答案。  

時間複雜度O(n log k)。空間複雜度O(k)。  

```python
class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        left=[]
        right=[]
        left_busy=[]
        right_busy=[]
        ans=0
        curr_time=0
        
        for i in range(k):
            heappush(left,[-time[i][0]-time[i][2], -i]) # [efficiency, idx]
        
        while n>0 or right or right_busy:
            
            while left_busy and left_busy[0][0]<=curr_time:
                t=heappop(left_busy)
                heappush(left,t[1])
                
            while right_busy and right_busy[0][0]<=curr_time:
                t=heappop(right_busy)
                heappush(right,t[1])
                
            if right:
                worker=heappop(right)
                idx=-worker[1]
                arrive=curr_time+time[idx][2]
                ans=arrive
                curr_time=arrive
                busy_time=arrive+time[idx][3]
                heappush(left_busy,[busy_time,worker])
                continue
                
            if n>0 and left:
                n-=1
                worker=heappop(left)
                idx=-worker[1]
                arrive=curr_time+time[idx][0]
                curr_time=arrive
                busy_time=arrive+time[idx][1]
                heappush(right_busy,[busy_time,worker])
                continue
            
            r_time=right_busy[0][0] if right_busy else inf
            l_time=left_busy[0][0] if left_busy else inf
            curr_time=min(r_time,l_time)

        return ans
```
