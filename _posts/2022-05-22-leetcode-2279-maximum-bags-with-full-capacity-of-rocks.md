--- 
layout      : single
title       : LeetCode 2279. Maximum Bags With Full Capacity of Rocks
tags        : LeetCode Medium Array Sorting Greedy
---
周賽294。照著描述就能過的模擬題，相當友善。

# 題目
你有n個袋子，編號從0到n-1。  
輸入兩個索引從0開始的整數陣列capacity和rocks，代表第i個袋子可以裝capacity[i]塊石頭，且目前已經裝了rocks[i]塊石頭。  
你還有additionalRocks顆石頭，可以塞到任意袋子中。求最多能有幾袋**裝滿的袋子**。

# 解法
先遍歷所有袋子，若已經滿了，則full加1；沒滿的袋子算出還需要多少顆石頭才能滿，加進need陣列中。  
想要盡可能裝滿更多袋子，所以優先把need排序，優先從需求最小的塞石頭。  
在剩餘石頭足夠的情況下，不斷往空袋子塞石頭，每塞一個便多一個full。最後回傳full值就是答案。

```python
class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        full=0
        need=[]
        for c,r in zip(capacity,rocks):
            if c==r:
                full+=1
            else:
                need.append(c-r)
                
        need.sort(reverse=1)
        while need and additionalRocks>=need[-1]:
            full+=1
            additionalRocks-=need.pop()
            
        return full
```
