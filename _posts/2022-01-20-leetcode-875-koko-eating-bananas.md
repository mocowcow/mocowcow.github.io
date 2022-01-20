---
layout      : single
title       : LeetCode 875. Koko Eating Bananas
tags 		: LeetCode Medium BinarySearch
---
之前把吃香蕉的函數寫錯又一個TLE，太苦了。  
相似題[878. Nth Magical Number](https://leetcode.com/problems/nth-magical-number/)。

# 題目
有N堆香蕉，每堆數量不同，Koko想在h小時內把香蕉全部吃完，求最慢一小時需要吃k個香蕉。  
每小時只能待在同個位置吃，若不足k則全部吃完，不能跑去其他地方。

# 解法
先找出一堆最多有多少香蕉，定為上界(再高也沒辦法加快進度)，下界=1，做二分搜。

```python   
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        def time(speed):
            t = 0
            for p in piles:
                t += (p-1)//speed + 1
            return t

        while low < high:
            mid = (low+high)//2
            if time(mid) <= h:
                high = mid
            else:
                low = mid+1

        return low
```
