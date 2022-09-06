--- 
layout      : single
title       : LeetCode 2398. Maximum Number of Robots Within Budget
tags        : LeetCode Hard Array SlidingWindow SortedList MonotonicQueue
---
雙周賽86。一開始想到了單調堆疊來找到各個chargeTimes[i]的左右邊界，後來發現是錯的。  
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
每個元素進出窗口最多共2次，每次進出sorted list成本為O(log N)，整體複雜度為O(N log N)。  

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

一開始想到的**單調**算是對了一半，只不過是用**單調佇列**維護區間最大值。  

單調遞減佇列mx用來維護區間最大值，要怎麼做？當窗口右方新加入一個值chargeTimes[i]，他比窗口內所有元素都還要大，那麼至少在他出去為止，最大值都不會比他還小。所以左邊如果有比他小的元素，通通都可以丟掉了。這時候佇列的第一個元素將會是區間最大值。  

現在每個元素最多都只會進出共兩次，整體複雜度優化到O(N)。  

```python
class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        ans=0
        left=0
        sm=0
        mx=deque()
        for right,(time,cost) in enumerate(zip(chargeTimes,runningCosts)):
            sm+=cost
            # monotonic decreasing
            while mx and time>=chargeTimes[mx[-1]]:
                mx.pop()
            mx.append(right)
            while mx and chargeTimes[mx[0]]+(right-left+1)*sm>budget:
                if left==mx[0]:mx.popleft()
                sm-=runningCosts[left]
                left+=1
            ans=max(ans,(right-left+1))

        return ans
```