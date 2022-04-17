---
layout      : single
title       : LeetCode 2240. Number of Ways to Buy Pens and Pencils
tags 		: LeetCode Medium Math 
---
雙周賽76。差點用暴力法下去，好險及時回頭。

# 題目
你有total塊錢，鋼筆售價為cost1，鉛筆售價為cost2。  
不必把所有錢花完，求有幾種購買(或不買)鋼筆和鉛筆的組合。  

> total = 20, cost1 = 10, cost2 = 5  
> 買0支鋼筆 搭配0,1,2,3,4支鉛筆  
> 買1支鋼筆 搭配0,1,2支鉛筆  
> 買2支鋼筆 搭配0支鉛筆  
> 共9種組合

# 解法
先把total除cost1，得到最多可以買的鋼筆數量max1。  
代入迴圈，計算買i支鋼筆後剩下remain塊錢，最多可以買j支鉛筆。  
也可以選擇不買，所以i支鋼筆可以搭配0...j共j+1種選擇，答案加上j+1。

```python
class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ans=0
        max1=total//cost1
        for i in range(max1+1):
            remain=total-cost1*i
            j=remain//cost2
            ans+=j+1
            
        return ans
```

