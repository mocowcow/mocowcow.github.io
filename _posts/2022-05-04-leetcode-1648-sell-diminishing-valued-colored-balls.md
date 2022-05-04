--- 
layout      : single
title       : LeetCode 1648. Sell Diminishing-Valued Colored Balls
tags        : LeetCode Medium Array Math BinarySearch Greedy
---
二分搜學習計畫。最後這幾天的題目幾乎是hard的難度，而且這題的圖例竟然是GIF，好用心。  

# 題目
你有好幾種顏色的球，有個顧客想要買orders顆球，顏色隨便。  
這顧客很奇怪，如果黃球剩6顆，他會出6塊買一顆黃球。之後剩下5顆，他只願意出5塊買下一顆黃球(球的價格隨數量遞減)。  
輸入陣列inventory，inventory[i]=x代表第i種顏色的球有x顆，可以依照任意順序賣球，求賣了orders顆的最大收入為多少。答案可能很大，要模10^9+7後回傳。  

# 解法
一開始看到這描述，還以為是要用heap，看到orders最大10^9驚覺不對，一顆一顆拿絕對會TLE。  
看看這種超大數字有沒有什麼可以拿來二分搜的？想半小時才想到：搜球的最低出售價要多少，才能湊滿orders顆。  

寫一個函數countBalls(val)，遍歷每種球，只要價格不小於val，就一直賣出，計算總共可以賣出多少顆。  
題目有說每種球最少1顆，代表最低價格也是1，下界定為1，而上界就是inventory中最大的值。以mid去計算可以湊到多少球，如果不足orders顆，則代表需要將最低價格下調，更新上界為mid-1；否則代表存貨足夠了，將下界更新為mid。考慮lo=1, hi=2的狀況，若取左中位數mid=1，若更新下界會出現死循環，故改用右中位數。  

二分搜停止後，lo會是最低出售價格，所有價格超過lo的球都應該要被賣掉。  
假設lo=3，某球數有7，需要賣出3+4+5+6+7，這時候梯形公式可以在常數時間內計算出總金額。  
最後再遍歷一次inventory，同時計算賣出的總利潤sell及總球數cnt。  
但是cnt有可能超過orders，多的球=cnt-orders，sell扣除掉lo*多出的球就是正確答案。  

當時想說，多賣的時候，要先從便宜的球開始退錢。不過仔細想想，要退錢只會退到每顆lo元的球，因為如果能退完所有lo元球的話，二分搜的時候lo就不會降到現在這個數值了。

```python
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        MOD=10**9+7
        
        def countBalls(val): # 達到val都賣
            cnt=0
            for x in inventory:
                if x>=val:
                    cnt+=x-val+1
            return cnt
        
        lo=1
        hi=max(inventory)
        while lo<hi:
            mid=(lo+hi+1)//2
            if countBalls(mid)<orders: #找第一個能湊滿orders的價格
                hi=mid-1
            else:
                lo=mid
                
        sell=0
        cnt=0
        for x in inventory:
            if x>=lo:
                sell+=(x+lo)*(x-lo+1)//2
                cnt+=x-lo+1
                
        return (sell-(cnt-orders)*lo)%MOD
        
        
```
