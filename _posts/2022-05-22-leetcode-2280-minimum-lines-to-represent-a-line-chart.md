--- 
layout      : single
title       : LeetCode 2280. Minimum Lines to Represent a Line Chart
tags        : LeetCode Medium Array Sorting Math
---
周賽294。花了5解決前面兩題，結果在這題卡了70分鐘才過，隱藏測資過於噁心。

# 題目
輸入二維整數陣列stockPrices，其中stockPrices[i] = [day, price]，表示第day[i]天的股票價格為price[i]。  
以基於x,y兩軸的折線圖表示股價波動，求至少需要幾條直線。

# 解法
應該很多人都可以想到兩點間的斜率公式：(y2-y1)/(x2-x1)。  
假設有三個點A,B,C，計算兩點之間的斜率，如果(A,B)與(B,C)斜率相等，代表可以共用同一條線。  

理論上都對，但是跑出一個不公開的測資，說答案錯了，但是又不想讓你知道錯在哪。  
魔鬼出在細節裡，浮點數在一定的精度下會出現誤差，如果拿兩個float很可能會出錯。  

結果我手動調精度調半天也抓不到正確值，最後是用了內建的Decimal函數庫才通過。

```python
from decimal import Decimal

class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        p=sorted(stockPrices)
        N=len(p)
        ans=0
        prev=None

        def slope(x1,y1,x2,y2):
            return (Decimal(y1)-Decimal(y2))/(Decimal(x1)-Decimal(x2))
        
        for i in range(1,N):
            x1,y1=p[i-1]
            x2,y2=p[i]
            sl=slope(x1,y1,x2,y2)
            if prev is None or Decimal.compare(sl,prev)!=0:
                ans+=1
                prev=sl

        return ans
```

看了討論區，原來許多人都漏掉了這麼重要的部分，看到有人總結的重點：  
1. 浮點數不要除法，先移項變成乘法  
2. 或是轉成分數，用gcd約分  

一開始先過濾掉edge cases，只有一個點時，不會有線；兩個點時，肯定一條線。  
再來將兩個斜率的等式分母化簡掉，變成純粹的乘法，判斷不共用一條線時，line計數+1。
> (y1-y2)/(x1-x2) != (y2-y3)/(x2-x3)  
> 兩邊同乘(x1-x2)和(x2-x3)  
> (y1-y2)\*(x2-x3) != (y2-y3)\*(x1-x2)  

```python
class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        N=len(stockPrices)
        if N<=2:
            return N-1
        
        line=1
        p=sorted(stockPrices)
        for i in range(1,N-1):
            x1,y1=p[i-1]
            x2,y2=p[i]
            x3,y3=p[i+1]
            if (y1-y2)*(x2-x3)!=(y2-y3)*(x1-x2):
                line+=1

        return line
```
