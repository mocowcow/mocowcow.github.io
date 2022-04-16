---
layout      : single
title       : LeetCode 1507. Reformat Date
tags 		: LeetCode Easy Easy String 
---
意外看到某位大神的[周賽講解影片](https://www.youtube.com/watch?v=aAiSmtf6Xl0)，想說自己來做做看。要是我碰到這題八成會被氣死。

# 題目
輸入以下格式的日期字串：
- 日期格式 {"1st", "2nd", "3rd", "4th", ..., "30th", "31st"}.
- 月份格式 {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}.
- 年份介於 [1900, 2100]之間.

將其轉換成YYYY-MM-DD的格式輸出。

# 解法
第一步驟當然是以空白符號切割成三段。  
年分y一定是四個字，不用特別處理。月份m就從題目提供的對照表查詢。日期要砍掉後面兩個贅字。  
麻煩的是補日、月長度不足2的話還要補0，太久沒有搞字串格式化，還特別去查查怎麼寫，要不然真的要加一堆if來判斷。  
複習字串格式化真算是有所收穫。

```python
class Solution:
    def reformatDate(self, date: str) -> str:
        d,m,y=date.split()
        M=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]        
        m=M.index(m)+1
        d=int(d[:-2])
        
        return '%s-%02d-%02d' % (y,m,d)
```

