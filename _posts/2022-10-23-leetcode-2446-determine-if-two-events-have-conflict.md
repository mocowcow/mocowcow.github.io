--- 
layout      : single
title       : LeetCode 2446. Determine if Two Events Have Conflict
tags        : LeetCode Easy Array String Sorting
---
周賽316。比賽時傻傻地的把字串轉成時間後才比較，其實直接用字串比較就好。  

# 題目
輸入兩個字串陣列event1和event2，分別代表同一天內發生的兩個事件，其中：  
- event1 = [startTime<sub>1</sub>, endTime<sub>1</sub>]  
- event2 = [startTime<sub>2</sub>, endTime<sub>2</sub>]  

事件時間是合法的24小時格式HH:MM。  
當兩個事件有交集時就會發生衝突。  
如果兩個事件之間有衝突，則回傳true；否則返回false。  

# 解法
先找到較早發生的事件放到t[0]，較晚的放到t[1]，只要t[0]的結束時間超過t[1]的就代表有交集。  

因為固定兩個元素，所以排序其實只需O(1)，時空間複雜度O(1)。  

```python
class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        t=[event1,event2]
        t.sort()
        
        return t[1][0]<=t[0][1]
```

提供大神的一行寫法。  

```python
class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        return min(event1,event2)[1]>=max(event1,event2)[0]
```