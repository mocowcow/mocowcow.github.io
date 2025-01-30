---
layout      : single
title       : LeetCode 3433. Count Mentions Per User
tags        : LeetCode Medium Sorting Heap
---
weekly contest-434。  
這題有點噁心，前 50 名甚至有 34 個中招。  

反正就是一堆細節 + 轉型 + 字串處理。  
要是改成設計題也不至於這麼噁心。  

## 題目

<https://leetcode.com/problems/maximum-frequency-after-subarray-operation/>

## 解法

簡而言之：系統有**提及**事件 (就是 @ 某人)。  
有三個用法：  

- @all 所有人  
- @online 所有在線的人  
- @someone 指定某些人，可重複，在線或否無所謂  

然後還有**下線**事件，讓某人在 t 下線，然後會在 t+60 秒自動**上線**。  

**沒有其他的上限方式**，且保證下線事件發生時，人一定在線。  
目前還算有良心。  

---

沒良心的是，範例給的事件時間是有序的，但題目可**沒保證有序**。  
建議一率當他沒排序過，自己排。  

然後同一個時間點 t 可能有好幾個事件。  
這時又有題目細節，**在線狀態改變優先**於提及。  
若同時時間內有 @ 和 OFFLINE，則會先讓人下線，然後才開始 @。  

然後 t 是字串，所以比較 t 之前要轉回整數。  

---

所以 events 排序規則是：  

- 先以 t 遞增  
- 若 t 相同，則 OFFLINE 優先  

可用自訂排序：  

```python
def cmp(a, b):
    t1 = int(a[1])
    t2 = int(b[1])
    if t1 != t2:
        return t1-t2
    if a[0] == "OFFLINE":
        return -1
    return 1
    
events.sort(key=cmp_to_key(cmp))
```

lambda 比較難寫：  
第二對鍵值要找到 OFFLINE 讓他變成負數；其餘保持 0。  

```python
events.sort(key=lambda x:(int(x[1]), -(x[0]=="OFFLINE")))
```

---

排完 events 之後就可以依序處理事件了。  
先處理上線、再處理下線、最後才是 @。  

拿一個集合維護在線的人，然後弄一個 min heap 以 (online_time, id) 的結構維護上線事件。  
n 很小，直接暴力給每個人 @ 計數即可。  

時間複雜度很彆扭，反正大概是 O(sort + nQ)，其中 Q = len(events)。  
空間複雜度 O(n)。  

```python
class Solution:
    def countMentions(self, n: int, events: List[List[str]]) -> List[int]:
        events.sort(key=lambda x: (int(x[1]), -(x[0] == "OFFLINE")))

        ans = [0] * n
        online = set(range(n))
        h = []  # [time, id]

        for msg, curr_time, s in events:
            curr_time = int(curr_time)
            # online first
            while h and h[0][0] <= curr_time:
                t = heappop(h)
                online.add(t[1])

            # OFFLINE
            if msg == "OFFLINE":
                id = int(s)
                online.remove(id)
                heappush(h, [curr_time+60, id])
                continue

            # MESSAGE
            if s == "ALL":
                for i in range(n):
                    ans[i] += 1
                continue

            if s == "HERE":
                for i in online:
                    ans[i] += 1
                continue

            for x in s.split():
                id = int(x[2:])
                ans[id] += 1

        return ans
```

看完[大神的做法](https://leetcode.cn/problems/count-mentions-per-user/solutions/3057699/an-zhao-shi-jian-chuo-fen-zu-mo-ni-by-en-w77b/)，真的是學習了。  

其實具體有誰在線根本不重要。  
只要知道每個人**上線的時間點**。  

```python

class Solution:
    def countMentions(self, n: int, events: List[List[str]]) -> List[int]:
        events.sort(key=lambda x: (int(x[1]), -(x[0] == "OFFLINE")))

        ans = [0] * n
        online = [0] * n

        for msg, curr_time, s in events:
            curr_time = int(curr_time)

            # OFFLINE
            if msg == "OFFLINE":
                id = int(s)
                online[id] = curr_time+60
                continue

            # MESSAGE
            if s == "ALL":
                for i in range(n):
                    ans[i] += 1
                continue

            if s == "HERE":
                for i in range(n):
                    if online[i] <= curr_time:
                        ans[i] += 1
                continue

            for x in s.split():
                id = int(x[2:])
                ans[id] += 1

        return ans
```
