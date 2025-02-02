---
layout      : single
title       : LeetCode 3439. Reschedule Meetings for Maximum Free Time I
tags        : LeetCode Medium SlidingWindow
---
biweekly contest 149。

## 題目

<https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/description/>

## 解法

注意：本題移動會議後，**相對順序**須保持不變。  

以 0 表示空閒，1 表示會議：  
> 010  

只要把會議移到移到其中一邊的最遠處，就能讓空閒時間合併：  
> 變成 001  
> 或是 100  

---

如果移動更多次呢？  
> 0101010, k = 2  
> 變成 1100010
> 或是 0100011  
> 或是 0111000  
> ...

觀察得出，可以合併 k+1 個相鄰的空閒區間。  

---

問題轉換成：  
> 在 N+1 個元素，找出大小為 k+1 的**最大子陣列和**。  

用滑動窗口解決即可。  

時間複雜度 O(N)。  
空間複雜度 O(N)，可做到 O(1)。  

```python
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        # convert to N+1 free time gaps
        a = []
        pre = 0
        for s, e in zip(startTime, endTime):
            a.append(s - pre)
            pre = e
        a.append(eventTime - pre) # last gap

        # maximum subarray
        ans = 0
        sz = k + 1
        sm = 0
        left = 0
        for right, x in enumerate(a):
            sm += x
            if right - left + 1 == sz:
                ans = max(ans, sm)
                sm -= a[left]
                left += 1

        return ans
```
