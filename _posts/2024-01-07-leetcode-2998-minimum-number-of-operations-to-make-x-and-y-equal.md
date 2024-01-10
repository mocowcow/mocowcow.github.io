---
layout      : single
title       : LeetCode 2998. Minimum Number of Operations to Make X and Y Equal
tags        : LeetCode Medium Array Graph BFS
---
雙周賽121。真的被這題搞死了，腦筋完全轉不過來，一直以為有奇怪的數學解。  
結果直接噴到5000名去。  

## 題目

輸入兩個整數x和y。  

每次操作，你可以執行以下其中一種：  

- 若x是11的倍數，則可以將x除11  
- 若x是5的倍數，則可以將x除5  
- 將x加1  
- 將x減1  

求**最少**需要幾次操作，才可以使x和y相等。  

## 解法

四種操作中有三種都是讓x變小，只有一種可以讓x變大。  
如果初始x<y，只有直接把x往上加1加到y一種答案。  

乍看之下x的可變範圍非常大，但是注意到x和y介於[1, 10^4]之間，也就是說兩者的差最多10^4。  
在x=10^4，y=1的極端狀況下，如果從x分別往正負數找、慢慢加減1的話，最多也就找到[x-10^4, x+10^4]。  

那除法怎麼辦？當x是倍數的時候可以除5或11，這時候x會快速的變小，之後經過幾次增減後，變回倍數又可以繼續除。  
但是當x變成**負數**之後，除法反而會將x**變大**。  
又因為x的初始值是正整數，要變成負數只能往下減。因此負數x做除法後會直接成已經碰過的數。  
又又或者說y不為負數，所以當x為負時沒必要繼續往下找了，可以將x的查找下界視作1。

總結起來，從x出發嘗試所有走法，只走沒走過的數，我們最多只會遍歷大約2\*10^4個數。  

時間複雜度O(x)。  
空間複雜度O(x)。  

```python
class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        if x<y:
            return y-x
        
        vis=set()
        q=deque()
        q.append(x)
        
        step=0
        while q:
            for _ in range(len(q)):
                x=q.popleft()

                if x in vis:
                    continue
                vis.add(x)    

                if x==y:
                    return step

                q.append(x+1)
                q.append(x-1)
                for t in [5,11]:
                    if x%t==0:
                        q.append(x//t)
            step+=1
```
