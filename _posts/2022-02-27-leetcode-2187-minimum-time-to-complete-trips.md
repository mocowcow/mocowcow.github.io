---
layout      : single
title       : LeetCode 2187. Minimum Time to Complete Trips
tags 		: LeetCode Medium BinarySearch 
---
周賽282。上界不小心算錯吃一次WA，以後還是多設一點算了，不要計較這麼多。

# 題目
輸入長度N的整數陣列time，time[i]代表代表第i台公車跑完一趟車程要多久，整數totalTrips代表總共需要跑幾趟。  
求最少需要幾分鐘，公車司機們可以總共跑完totalTrips趟車程。  
例：
> time = [1,2,3], totalTrips = 5, 最少需要3分鐘  
> time = 1, 只有一號車跑完1趟  
> time = 2, 一號車2趟+二號車1趟  
> time = 3, 一號車3趟+二號車1趟+三號車1趟 共5趟   

# 解法
測資大得要命的奇怪題目八成就是二分搜，我越來越堅信了。  
定義函數canTrip(x)表示能不能在x分鐘內跑完目標趟數，接下來做二分搜找最小時間。  
最少一定要跑1分鐘，下界1，最多可能要跑10^7趟，且單程每趟需要10^7分鐘，上界為10^14。如果canTrip(mid)成功跑完，則更新high=mid；否則low=mid+1，最後low就是答案。  
canTrip(x)函數很單純，對每個車程t以(時間x/車程t)可以得出第i台車跑完幾趟，全部加總就是總趟數，回傳總趟數是否滿足totalTrips即可。



```python
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:

        def canTrip(x):
            trip = 0
            for t in time:
                trip += x//t
            return trip >= totalTrips

        low = 1
        high = 10**14
        while low < high:
            mid = (low+high)//2
            if canTrip(mid):
                high = mid
            else:
                low = mid+1

        return low

```
