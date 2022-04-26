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

雙指針解法，比上面的簡潔好理解，但是不知道為啥慢了一些，反正我個人更喜歡下面的解法。  
一樣先把難度和利潤打包好，拿去排序。我們不在乎工人的指派順序，所以也拿去排序。  
維護變數i，紀錄下一個要比較的工作索引，變數best紀錄可獲得最大利潤。  
遍歷所有工人，如果此工人能力可以承擔工作i，則以工作i的利潤去更新best，直到工作全部處理完或是工人能力不足為止。這時候的best就是此工人能賺到的最大利潤，將best加入答案。

```python
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        N=len(difficulty)
        jobs=sorted(zip(difficulty,profit),key=itemgetter(0))
        i=best=ans=0
        for w in sorted(worker):
            while i<N and jobs[i][0]<=w:
                best=max(best,jobs[i][1])
                i+=1
            ans+=best

        return ans
```