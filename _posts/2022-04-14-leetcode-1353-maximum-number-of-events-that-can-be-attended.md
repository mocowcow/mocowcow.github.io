---
layout      : single
title       : LeetCode 1353. Maximum Number of Events That Can Be Attended
tags 		: LeetCode Medium Array Greedy Heap HashTable
---
待辦清單挖出來的，可能是初學heap時碰到但解不出來才放著。個人體感是將近hard程度，不太好想。

# 題目
輸入events陣列代表各活動的起迄時間。在同一天你只能選擇一個活動參加，求最多可以參加到幾個活動。

# 解法
一開始只想著活動一開始就趕快參加，且優先選擇舉辦期間較短的，結果到33/44測資就爆炸。  
> [[1,2],[1,2],[3,3],[1,5],[1,5]]  
> 照我的邏輯排序會變成  
> [[1,2],[1,2],[1,5],[1,5],[3,3]]   
> 然後最後[3,3]沒參加到，就出錯  

參考[這篇](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/discuss/510262/Detailed-analysisLet-me-lead-you-to-the-solution-step-by-step)文章，正確的方式應該是**優先選擇即將結束的活動**。  

詳細步驟為：  
1. 記錄當天日期，如果有活動今天開幕，則將其加入候選清單中  
2. 將已經過期的活動移出清單
3. 若清單不為空，則挑選結束日期最近的那個參加  

```python
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        N = len(events)
        events.sort(key=itemgetter(0))
        firstDay = min(x[0] for x in events)
        lastDay = max(x[1] for x in events)
        idx = 0
        h = []
        ans = 0
        for today in range(firstDay, lastDay+1):
            # add events start today
            while idx < N and events[idx][0] == today:
                heappush(h, events[idx][1])
                idx += 1

            # pop finished events
            while h and h[0] < today:
                heappop(h)

            # attend a event which is about to end
            if h:
                ans += 1
                heappop(h)

        return ans
```

不排序活動，改成用雜湊表紀錄開幕日期。  

```python
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        eventStart=defaultdict(list)
        for a,b in events:
            eventStart[a].append(b)
            
        firstDay=math.inf
        lastDay=0
        for a,b in events:
            firstDay=min(firstDay,a)
            lastDay=max(lastDay,b)
            
        ans=0
        h=[]
        for today in range(firstDay,lastDay+1):
            # add events start today
            if today in eventStart:
                for x in eventStart[today]:
                    heappush(h,x)
                    
            # pop finished events
            while h and h[0] < today:
                heappop(h)
                
            # attend a event which is about to end
            if h:
                ans += 1
                heappop(h)
                
        return ans
```

