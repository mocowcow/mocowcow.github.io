---
layout      : single
title       : LeetCode 3169. Count Days Without Meetings
tags        : LeetCode Medium Array Sorting
---
周賽 400。

## 題目

輸入正整數 days，代表你從第 1 天到第 days 天都要工作。  
另外輸入二維整數陣列 meetings，其中 meetings[i] = [start_i, end_i]，代表第 i 次開會的起始日期 (包含首尾)。  

求有多少工作日是**不用開會**的。  

注意：會議期間可能重疊。

## 解法

將 meeting 排序之後，可以知道哪場會議先開始。  
但多場會議可能在同天開始、不同天結束。為確保知道最晚的結束日期，需要再以結束日期遞減排序。  

維護空閒的起始日期 curr，並遍歷排序好的 meetings。  
從 curr 到開始日 s 的前一天是空閒的，將空閒日數加入答案。  
而直到結束日 e 的都沒空，以結束日的下一天 e + 1 更新下次的空閒日起始。  

別忘記所有會議結束後，一直到第 days 天都是空閒的！  

時間複雜度 O(N log N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x:(x[0], -x[1]))
        ans = 0
        curr = 1
        for s, e in meetings:
            # [curr, s - 1] is free
            ans += max(0, s - 1 - curr + 1)
            # [s, e] is not free
            curr = max(curr, e + 1)
            
        # no more meetings
        # [curr, days] is free
        ans += max(0, days - curr + 1)
        
        return ans
```

會議日期可能重疊，不如先找出哪幾天有開會。  
問題轉換成**區間合併**。  

合併完之後，從 days 扣掉有會議的天數即可。  

時間複雜度 O(N log N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        
        a = []
        for s, e in meetings:
            if a and a[-1][1] >= s:
                a[-1][1] = max(a[-1][1], e)
            else:
                a.append([s, e])
               
        ans = days
        for s, e in a:
            ans -= e - s + 1
            
        return ans
```
