---
layout      : single
title       : LeetCode 2136. Earliest Possible Day of Full Bloom
tags 		: LeetCode Hard Array Sorting Greedy
---
模擬周賽275。這個例題示意圖太過分了，怕人家太輕鬆看出規律，竟然刻意打亂順序誤導人。

# 題目
你有N個種子，輸入長度N的整數陣列plantTime及growTime，表示每個種子需花費多少天種植、多少天成長。  
每天只能對同一顆種子種植，且種子i要種滿plantTime[i]才會開始生長。開始生長後則不必管他，天數足夠隔天會就開花，開花之後不會凋謝。  
求最快第幾天可看到所有種子同時開花。

# 解法
因為種好之後就會自動開始生長，很直覺的知道要先種植生長期較久的種子。  
把種植和生長時間打包起來，以生長時間降冪排序。維護變數lastBloom代表開花日期，currDay表示當前日期。遍歷排序好的種子，若當日+種植+生長時間超過預期開花日期，則更新開花日期，最後將當天日期加上種植天數，繼續處理下一顆種子。  
老實說，我看到示意圖在那邊交叉栽種不同顆種子，還以為有什麼神奇操作，特地拿紙筆試算我的理論，算完確定一樣快才安心。

```python
class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        plant = list(zip(growTime, plantTime))
        plant.sort(key=lambda x: -x[0])

        lastBloom = currDay = 0
        for g, t in plant:
            lastBloom = max(lastBloom, currDay+t+g)
            currDay += t

        return lastBloom

```
