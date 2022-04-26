---
layout      : single
title       : LeetCode 826. Most Profit Assigning Work
tags 		: LeetCode Medium Array BinarySearch Sorting Greedy
---
二分搜學習計畫。這題也滿貼近現實生活應用的，雖然最佳解也不是二分搜，而是雙指針。

# 題目
輸入陣列difficulty和profit，代表工作i難度以及其利潤。陣列worker代表各工人的能力。  
每個工人只能選擇不超過自己能力的工作來做，求最大總利潤為多少。  

# 解法
看範例可以知道，難度高的工作利潤不一定會比較高，例：  
> difficulty = [85,47,57], profit = [24,66,99]  
> 難度85利潤24  
> 難度47利潤66  
> 難度57利潤99  

就算有個工人能力=100，他也應該選擇難度57的，才能賺最多錢。  

先將所有工作組合成(難度,利潤)，並以難度為key遞增排序。遍歷排序好的工作，並維護一個變數mx來記錄最大利潤，在雜湊表best中紀錄難度d最多可以賺p利潤。。  
遍歷worker，在排序過的難度diff中找到最後一個不大於工人能力的位置idx，而diff[idx]代表其能負荷的最高難度，再拿去best中找到其可以得到的最大利潤，加入答案中。

```python
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs=[(0,0)]
        for d,p in zip(difficulty,profit):
            jobs.append((d,p))
        jobs.sort(key=itemgetter(0,1))
        best=defaultdict(int)
        mx=0
        for d,p in jobs:
            mx=max(mx,p)
            best[d]=mx
        diff=sorted(best.keys())
            
        ans=0
        for w in worker:
            idx=bisect_right(diff,w)-1
            ans+=best[diff[idx]]
            
        return ans
```

