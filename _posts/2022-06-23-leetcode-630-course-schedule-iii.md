--- 
layout      : single
title       : LeetCode 630. Course Schedule III
tags        : LeetCode Medium Array Heap Greedy
---
每日題。有點像是[1353. maximum number of events that can be attended]({% post_url 2022-04-14-leetcode-1353-maximum-number-of-events-that-can-be-attended %})。  

# 題目
有n個不同的課程，編號從1到n。輸入陣列courses，其中courses[i] = [durationi, lastDayi]表示第i門課需要連續占用durationi天，且最慢必須在lasyDayi天完成。  

從第1天開始，每次只能修一門課，求最多總共可以修完幾門課。  

# 解法
每堂課都有設定最後期限，先不論耗時幾天，先選擇截止日期較接近的課程總是更佳選擇，故先將courses以截止日期遞增排序。  

維護變數today，代表當前的日期，以及最大堆積h，儲存已選的課程。  
遍歷排序好的courses，其耗時為cost，截止日期為last，而day加上cost就是最後一天上課日。  
如果最後一天上課日會超出截止日，則必須退掉一堂課。既然要退就退掉已選課程h中耗時最久者，可以替未來空出更多時間。  
最後回傳h大小就是已選修的課程數。

```python
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=itemgetter(1))
        h=[]
        today=0
        for cost,last in courses:
            today+=cost
            heappush(h,-cost)
            if today>last:
                drop=-heappop(h)
                today-=drop
                
        return len(h)
```
