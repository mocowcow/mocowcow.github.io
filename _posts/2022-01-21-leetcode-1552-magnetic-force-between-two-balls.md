---
layout      : single
title       : LeetCode 1552. Magnetic Force Between Two Balls
tags 		: LeetCode Medium BinarySearch Greedy
---
講一大堆什麼星球、磁力，有夠複雜的題目，差點沒被嚇哭，乾脆用自己的方式簡化。邊界處理錯誤造成死結，又吃了個TLE。

# 題目
有m顆球，可放入指定位置position中，每個位置只能放一顆，要將任意兩顆兩鄰球的**最小間隔**最大化。

# 解法
最小間隔最大化的意思，其實就是盡可能平均分配間隔距離。  
下界=1，上界=最後位-初位，做二分搜，如果能放得完m顆球，更新下界；否則更新上界。  
為什麼會是(low+high+1)/2？在這題的情況下，中間值必須向上取整，否則在某些時候會出錯。
例如：low=4、high=5時，mid=下向取整=4，若可放下4球，更新low為mid，跟沒改一樣，造成TLE。

```python
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        N = len(position)
        position.sort()
        low = 1
        high = position[-1]-position[0]

        def canPut(force):
            ball = 1
            last = position[0]
            for i in range(1, N):
                if position[i]-last >= force:
                    ball += 1
                    last = position[i]
            return ball >= m

        while low < high:
            mid = (low+high+1)//2
            if canPut(mid):
                low = mid
            else:
                high = mid-1

        return low
```
