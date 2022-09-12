--- 
layout      : single
title       : LeetCode 2406. Divide Intervals Into Minimum Number of Groups
tags        : LeetCode Medium Array Heap SortedList Sorting BinarySearch Greedy
---
周賽310。聽說和253. Meeting Rooms II同一題，但是我沒買會員不能看。

# 題目
輸入二維整數陣列intervals，其中intervals[i] = [lefti, righti]，表示閉區間[lefti, righti]。  
你必須將區間劃分為一個或多個分組，使得每個區間正好屬於一個組，且同一組中每個區間沒有重疊。  
求最少需要幾個組。  

# 解法
若要使每一組盡可能塞多個區間，則應當從開始時間最早的區間開始塞進任意可用組別裡，所以先把intervals遞增排序。  
我們還需要維護所有組別的結束時間，借此找到合法的組別來插入下一個區間，故使用sorted list。  

遍歷排序好的區間(a,b)，在找到任意結束時間小於a的任意組別，將其結束時間更新為b；若找不到則自成一組，直接插入結束時間b。  
最後回傳groups大小就是答案。時間複雜度O(N log N)，空間複雜度O(N)。  

順帶一提，如果有兩個組別[1,3]和[1,4]，選擇哪個來插入新的區間[5,10]，答案會不會不同？  
其實不會，因為區間已經排序過，之後的區間左邊界一定不會小於5，所以放到哪邊都是一樣的。  

```python
from sortedcontainers import SortedList

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        groups=SortedList() # ending time
        
        for a,b in intervals:
            idx=groups.bisect_left(a)-1
            if idx<0: # not exist
                groups.add(b)
            else:
                groups.pop(idx)
                groups.add(b)
        
        return len(groups)
```

既然選擇哪個組別都沒差，那其實用heap取代sorted list更好，還不用二分搜。  

```python
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        groups=[]
        
        for a,b in intervals:
            if groups and groups[0]<a:
                heappop(groups)
            heappush(groups,b)
                
        return len(groups)
```

但我覺得最好的解法應該是將區間轉換成差分，但似乎不太直覺。  
可以把區間[a,b]想成從a開始多占用一個組，而b+1結束後釋放一個組出來。  
接著把差分排序，遍歷過程中以當前組數來更新答案。  
時間複雜度一樣O(N log N)，空間複雜度O(N)。  

```python
from sortedcontainers import SortedList
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        diff=[]
        for a,b in intervals:
            diff.append([a,1])
            diff.append([b+1,-1])
            
        ans=0
        group=0
        for _,d in sorted(diff):
            group+=d
            ans=max(ans,group)
            
        return ans
```
