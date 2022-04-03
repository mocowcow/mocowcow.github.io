---
layout      : single
title       : LeetCode 2226. Maximum Candies Allocated to K Children
tags 		: LeetCode Medium Array BinarySearch
---
周賽287。一眼看出是二分搜，但誤會題意又噴一次WA，太苦了。

# 題目
你有好幾堆糖果堆，整數陣列candies代表每堆的糖果數量。你可以把糖果堆分成任意小堆，但是不可以把堆合併。  
現在有k個小孩，每人最多只能選擇其中一堆，且拿到相同的**糖果數量必須相同**，有些糖果不會被分出。求小孩最多能分到多少糖果。

# 解法
糖果不夠，每個人都別想吃，下界為0。又假設全部糖果剛好是k堆，每人拿一堆，上界設為sum(candies)/k。  
函數canDo(x)用來計算每份x顆糖的話，能分成幾分。若能讓k人都拿到就回傳true。  
開始二分搜，如果每人不能分到mid，則減少每份糖果數量，上界更新為mid-1；否則下界更新為mid。

```python
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:

        def canDo(x):
            ppl = 0
            for n in candies:
                ppl += n//x
            return ppl >= k

        lo = 0
        hi = sum(candies)//k

        while lo < hi:
            mid = (lo+hi+1)//2
            if not canDo(mid):
                hi = mid-1
            else:
                lo = mid

        return lo

```

