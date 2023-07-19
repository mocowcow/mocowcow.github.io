--- 
layout      : single
title       : LeetCode 435. Non-overlapping Intervals
tags        : LeetCode Medium Array Greedy Sorting
---
每日題。正難則反的好例子。  

# 題目
輸入一個區間陣列intervals，其中intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]。  
求最少要刪除幾個區間，才能使所有區間**不重疊**。  

# 解法
乍看很難知道刪除哪個區間是最佳解。  
將問題轉換成：選擇最少的X個索引，使所有區間至少與一個索引交集，原區間數量N扣掉X就是要被刪除的個數。  

將區間以右端點排序，依序遍歷，能保證右方區間的右邊界一定大於等於當前區間。  
因此只要檢查當前區間[s,e]的左端點是否小於前一個區間的右端點last，若是則代表兩者可以共享索引last；否則需要選擇一個新的索引，越靠右則之後能被使用到的機率越大，故選擇索引作為新的last。  

瓶頸在於排序，時間複雜度O(N log N)。  
空間複雜度O(1)。  

```python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        N=len(intervals)
        intervals.sort(key=itemgetter(1))
        
        cnt=0
        last=-inf
        for s,e in intervals:
            if s>=last:
                cnt+=1
                last=e
                
        return N-cnt1
```

也可以依照左端點排序。  
右方區間的左端點一定大於等於左方區間。如果當前區間[s,e]想要和左方區間共用一個索引last，則e必須小於等於last；否則需要選擇一個新的索引，更新last為e。  

```python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        N=len(intervals)
        intervals.sort(key=itemgetter(0))
        
        cnt=0
        last=-inf
        for s,e in intervals:
            if e>last:
                cnt+=1
                last=e
                
        return N-cnt
```

當然也可以不轉換問題，就按照原本的題意來做。  

同樣以右端點排序，如果當前區間[s,e]要和左方的區間重疊，那必定是s要小於先前的右端點last，需要刪除，所以不更新右端點last；否則以e更新last。  

瓶頸在於排序，時間複雜度O(N log N)。  
空間複雜度O(1)。  

```python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        N=len(intervals)
        intervals.sort(key=itemgetter(1))
        
        cnt=0
        last=-inf
        for s,e in intervals: # assured e>=last
            if s<last: # overlapped, remove
                cnt+=1
            else: # keep and update right bound
                last=e
                
        return cnt
```