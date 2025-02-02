---
layout      : single
title       : LeetCode 3440. Reschedule Meetings for Maximum Free Time II
tags        : LeetCode Medium Greedy SortedList
---
biweekly contest 149。

## 題目

<https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/description/>

## 解法

和 Q2 稍微有點不同。差別在於：  

- 只能移動 1 次  
- 移動之後，相對順序**可以改變**  

---

相對順序可改變，意味著會議可以整個搬走，搬到不相鄰的區間去。例如：  
> 101010  
> 把最中間的 1 搬到最右邊去  
> 變成 100011  
> 最大連續 = 3  

如果沒有足夠大的區間能搬到呢？  
那就是靠到左右邊，把會議左右兩邊的區間合併：  
> 101101  
> 中間的 11 沒地方可以完全移走  
> 只能靠左變成 111001  
> 或是 100111  
> 最大連續 = 2  

---

綜上，枚舉每個會議，看有沒有地方能放：  

- 有，新區間大小 = 左右區間 + 會議大小  
- 沒有，新空閒時間 = 左右區間  

為了知道有哪些地方能放，需要維護所有區間。  
枚舉時，還需暫時排除當前會議左右兩邊的區間，然後查詢最大值。  
需支持插入、刪除、查詢最大值，因此選用 sortedlist。  

先初始化所有區間。  
枚舉會議 x，先把左右兩邊的區間 gap1, gap2 刪除，再查詢最大值是否大於等於 x 的大小。  
更新答案後記得把 gap1, gap2 放回。  

時間複雜度 O(N log N)。  
空間複雜度 O(N)。  

```python
from sortedcontainers import SortedList as SL


class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        # convert to N+1 free time gaps
        a = []
        pre = 0
        for s, e in zip(startTime, endTime):
            a.append(s - pre)
            pre = e
        a.append(eventTime - pre) # last gap

        # maintain gaps can be use
        sl = SL(a)

        # enum job to move
        ans = 0
        for i, (s, e) in enumerate(zip(startTime, endTime)):
            sz = e - s
            gap1, gap2 = a[i], a[i+1]

            # remove gaps cannot be use
            sl.remove(gap1)
            sl.remove(gap2)

            # update answer
            if sl[-1] >= sz: # job can move to somewhere
                ans = max(ans, gap1 + gap2 + sz)
            else:
                ans = max(ans, gap1 + gap2)

            # put back
            sl.add(gap1)
            sl.add(gap2)

        return ans
```
