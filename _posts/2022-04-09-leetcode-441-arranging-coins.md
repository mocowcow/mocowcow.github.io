---
layout      : single
title       : LeetCode 441. Arranging Coins
tags 		: LeetCode Easy Greedy BinarySearch 
---
最近幾天在玩二分搜學習計畫，才想著這題應該會出現，今天果然碰上了。  
這題按爛的人還不少，不知道是不是把問題想得太複雜，明明暴力法也可以過。

# 題目
你有n個硬幣要來拿疊樓梯，第i階樓梯需要疊i個硬幣，求可以疊幾層**完整**的樓梯。

# 解法
先來個暴力貪心法。  
變數coin表示下一次蓋樓梯要花多少個硬幣，初始為1，遞增1。若剩下的硬幣還能蓋就繼續蓋。

```python
class Solution:
    def arrangeCoins(self, n: int) -> int:
        ans=0
        coin=1
        while n>=coin:
            n-=coin
            ans+=1
            coin+=1
            
        return ans
```

再來是這次的重點，二分搜。  
奇怪了我已經明明用過a*(a+1)/2這個鬼公式，怎麼前幾次周賽就沒想到，真是見鬼。  
下界為1，因為最少也有一個，一定可以一層。上界為n，這樣保證大於樓層數。  
用公式mid*(mid+1)/2算出mid層樓梯共需要多少硬幣，若超過n則更新上界為mid-1，否則更新下界為mid。

```python
class Solution:
    def arrangeCoins(self, n: int) -> int:
        lo=1
        hi=n
        while lo<hi:
            mid=(lo+hi+1)//2
            if mid*(mid+1)//2 >n:
                hi=mid-1
            else:
                lo=mid
                
        return lo
```

剩下還有神奇數學一行公式解，就不管它了。