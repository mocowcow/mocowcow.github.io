--- 
layout      : single
title       : LeetCode 2410. Maximum Matching of Players With Trainers
tags        : LeetCode Medium Array Sorting Greedy
---
雙周賽87。腦子卡住誤會題意，想著要二分搜就吃一個WA。  

# 題目
輸入整數陣列player，其中player[i]代表第i個選手的能力。還有另外一個整數陣列trainers，其中trainers[j]代表第j個教練的能力。  
每個選手只能和能力不小於自己的教練搭配，且每個選手和教練最多只能選一人搭配。  

求最多能成功搭配幾組。  

# 解法
題目只問有幾組可以配對，而不管順序，那就先排序再說。  
假設有個選手，能力1，而教練有兩個，能力分別為3和10。對於該選手來說兩個教練都可以搭配，但是10等的教練能夠培訓更強的選手，因此我們應該盡可能優先配對低分的教練。  

那麼將排序好的選手、教練分別裝入佇列中，依序來做配對，直到人數不足為止。如果某教練分數低於目前最低分的選手，則教練不合格，請下一位入場；否則配對數+1，教練帶著選手離開。  

```python
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        ans=0
        p=deque(players)
        t=deque(trainers)
        
        while p and t:
            if t[0]<p[0]:
                t.popleft()
            else:
                ans+=1
                t.popleft()
                p.popleft()
            
        return ans
```
