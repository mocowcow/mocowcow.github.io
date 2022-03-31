---
layout      : single
title       : LeetCode 2188. Minimum Time to Finish the Race
tags 		: LeetCode Hard DP
---
周賽282。本來只花了13分鐘寫前面三題，剩下77分鐘都被這大哥吞了，看來我還是跟DP不夠熟。

# 題目
輸入二維整數陣列tires、整數changeTime和numLaps，time[i]=[fi,ri]，f為該輪胎跑一圈的初始耗時，r為成長倍率。  
實際耗時公式為：第i圈耗時=f*(r^(i-1))；但也可以選擇先更換任一種新胎，需花費changeTime，並恢復輪胎初始耗時。  
> tires = [[2,3],[3,4]], changeTime = 5, numLaps = 4  
> 用tires[0]出發跑2圈，換新，再用tires[0]跑兩圈  
> 第一圈2 + 第二圈6 + 換新5 + 第一圈2 + 第二圈6 = 21  

求跑完numLaps圈最快要幾秒。

# 解法
先說說原本的TLE解法好了。  
N個輪胎，定義dp(i,t,k)表示跑第i圈，現使用第t種輪胎，這輪胎跑完過k圈，每次可以選擇繼續跑或是換新胎。  
轉移方程式：dp(i,t,k)=min(t跑第k圈,換胎+tt胎跑第1圈+dp(i+1,tt,1) FOR ALL 0<=tt<N)。  
當i達到numLaps代表圈數已經夠了，為base cases，回傳0。
結果只通過8/54測資，好慘。

```python
class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        N = len(tires)

        @lru_cache(None)
        def dp(i, t, k):  # n-th lap, curr tire, k-times of run
            if i >= numLaps:
                return 0
            # keep
            best = tires[t][0]*(tires[t][1]**k)+dp(i+1, t, k+1)
            # change
            for tt in range(N):
                best = min(best, changeTime+(tires[tt][0])+dp(i+1, tt, 1))

            return best

        ans = math.inf
        for i in range(N):
            ans = min(ans, dp(0, i, 0))

        return ans

```

看了很多人的解法，幾乎都是先事先計算跑i圈的成本，之後再慢慢扣除圈數，這樣DP的狀態可以壓到一維去。  
維護一個雜湊表lap，lap[i]表示不換胎跑i圈的最短時間。只要在當前時間小於changeTime+第一圈時間f，不換胎繼續跑就是更好的選擇。算完之後確認lap裡面有多少元素，就知道不換胎一次最多可以跑多少圈，記為mostLap。  
dp(i)表示跑i圈的最短時間。  
轉移方程式為dp(i)=min(跑j圈+換胎+dp(i-j) FOR ALL 1<=j<=min(i,mostLap))。  
當i=0時為base case，代表圈跑夠了，不需要再換胎，回傳-changeTime。

```python
class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        lap = defaultdict(lambda: math.inf)
        # pretreat best time that do laps without change tire
        for f, r in tires:
            currTime = f
            sumTime = f
            i = 1
            while i <= numLaps and currTime < changeTime+f:
                lap[i] = min(lap[i], sumTime)
                i += 1
                currTime *= r
                sumTime += currTime

        mostLap = len(lap) # max laps without change tire

        @lru_cache(None)
        def dp(i):
            if i <= 0:
                return -changeTime
            best = math.inf
            for j in range(1, min(mostLap, i)+1):
                best = min(best, lap[j]+changeTime+dp(i-j))
            return best

        return dp(numLaps)

```
