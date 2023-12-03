---
layout      : single
title       : LeetCode 2952. Minimum Number of Coins to be Added
tags        : LeetCode Medium Array Math Greedy
---
周賽374。老實說我看這次贊助商是JQ就覺得不妙，畢竟上次周賽360給他贊助也搞得很難。  
確實是挺難的。  

## 題目

輸入整數陣列coins，代表可用硬幣的面額。還有一個整數target。  

若你能透過某些硬幣來湊到總額為x，則稱x為**可得的**。  

求**最少**要加入幾枚**面額不限**的硬幣，才能使得[1, target]區間中所有數字都是**可得的**。  

## 解法

要湊到x，最理想的狀況就是剛好有面額為x的硬幣；否則只能靠若干個小於x的硬幣湊出來。
先將coins排序。  

目前**最大可得**數記為limit。  
假設當前能湊出[1, limit]的所有數，這時候又多出一個等於limit的硬幣會怎樣？  
是不是[1, limit]中所有組合都可以再加上limit，得到[limit+1, limit+limit]，那最大可得就變limit+limit了。  
同理，只要硬幣面額小於limit都能**無縫擴展**limit上限。  

那如果當前要湊x湊不出，又沒有硬幣剛好是x，只能自己加。  
可以加任意面額的硬幣，要選哪個最好？  
如果選1，只能讓limit變limit+1；選x，可以讓limit變limit+x。很明顯要選x。  

每次自己增加硬幣會讓x變成兩倍，最多增加log target次。  
時間複雜度O( (N log N) + (log target) )。  
空間複雜度O(N)，如果不用deque可以O(1)。  

```python
class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        q=deque(sorted(coins))
        ans=0
        x=1
        limit=0
        
        while x<=target:
            while q and q[0]<=x:
                limit+=q.popleft()
            if limit<x:
                ans+=1
                limit+=x
            else:
                x=limit+1
                
        return ans
```
