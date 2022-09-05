--- 
layout      : single
title       : LeetCode 2398. Maximum Number of Robots Within Budget
tags        : LeetCode
---
雙周賽86。一開始想到了單調佇列來找到各個chargeTimes[i]的左右邊界，後來發現是錯的。  
後來及時想到二分搜+滑動窗口，但是二分搜寫到一半突然開竅：直接滑動不就得了嗎？  

# 題目
你有n個機器人。輸入兩個長度同為n的整數陣列chargeTimes和runningCosts。第i個機器人的充電成本為chargeTimes[i]單位，運行成本為runningCosts[i]單位。還有一個整數budget。  

運行k個機器人的總成本等於max(chargeTimes) + k\*sum(runningCosts)，其中max(chargeTimes)是k個機器人中最大的充電成本，sum(runningCosts)是所有k個機器人之間運行成本的總和。  

你必須選擇**連續相鄰的機器人**來運行，求總成本不超過預算的情況下，最多可以運行幾個。

# 解法
為什麼滑動窗口可以成立，有一個很大的關鍵：陣列中的值都是正數，子陣列增大，不可能得到更小的成本。  
假設子陣列[A,B]已經超過預算，這時再加入一個C，不可能使充電時間或運行成本降低，那麼[A,B]絕對無法後方的機器人一起運行。  

確定使用滑動窗口之後，除了簡單的窗口內運行成本總和，還需要想辦法找到窗口內的充電時間最大值。  
想要找極值，又要刪除元素，這時候又輪到sorted list了。維護sorted list變數mx，為把充電時間丟進去，最後一個元素就是最大值。  

那麼開始將窗口往右滑，如果總成本超過預算，就把窗口左邊界縮減。縮減完後，mx的長度正好為窗口大小，以窗口大小更新答案。  

```python
from sortedcontainers import SortedList

class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        ans=0
        left=0
        sm=0
        mx=SortedList()
        for right,(time,cost) in enumerate(zip(chargeTimes,runningCosts)):
            sm+=cost
            mx.add(time)
            while mx and mx[-1]+len(mx)*sm>budget:
                mx.remove(chargeTimes[left])
                sm-=runningCosts[left]
                left+=1
            ans=max(ans,len(mx))

        return ans
```
