--- 
layout      : single
title       : LeetCode 2507. Smallest Value After Replacing With Sum of Prime Factors
tags        : LeetCode Medium Math Simulation
---
周賽324。這鬼東西挺麻煩，我還花一陣子回想怎麼質因數分解。  

# 題目
輸入正整數n。  

重複將n質因數分解，並將n替換為其**質因數之和**。  
注意：若n可以被某個質因數整除多次，則求和時也應計入多次。  

求n可以達到的最小值。  

# 解法
原本將質因數個數=1設為迴圈終止條件，結果被n=4騙一個TLE。  
正確的中止條件應該是**求和後新值等於原值**。  

從最小的質數div=2開始向上窮舉，若能整除n則將div加入總和，並將n除以div。重複直到div^2超過n時停止。  
為什麼div^2<=n一定成立？  
> 因為我們由小到大窮舉質數，若存在小於div的因數，早就被除掉了  
> 所以n若能被div整除，則最小的商一定是div  

試想n=3的情況，無法被2整除，但是2^2超過3，迴圈終止時一樣n=3。這時應該將剩餘的n加回總和中。  

時間複雜度真的不知道怎麼算，據大神的說法是O(sqrt(n))。因數是從2開始算起，每次加總的操作量不會超過O(log n)，而最差的情況下，n由2和一個超大的質數所組成，加總後n的值將近是減半，反正可以感覺出n減少的速度非常快。  
空間複雜度O(1)。

```python
class Solution:
    def smallestValue(self, n: int) -> int:
        
        def f(n):
            div=2
            sm=0
            while div*div<=n:
                if n%div==0:
                    sm+=div
                    n//=div
                else:
                    div+=1
            if n>1:sm+=n
            return sm
        
        while True:
            t=f(n)
            if t==n:break
            n=t
            
        return n
```
