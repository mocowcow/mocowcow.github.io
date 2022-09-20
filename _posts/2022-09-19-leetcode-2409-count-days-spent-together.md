--- 
layout      : single
title       : LeetCode 2409. Count Days Spent Together
tags        : LeetCode Easy String
---
雙周賽87。夢回大學時期，那時要求算日期增減，還要考慮閏年，真是難搞的不行。  
那次真留下深刻印象，我寫了一大串的垃圾，改成查表很簡單就解決了。  

# 題目
Alice和Bob要去羅馬參加不同的商務會議。  
輸入4個字串arriveAlice, leaveAlice, arriveBob和leaveBob，分別代表Alice和每個都是一個長度5的字串，格式為"MM-DD"，對應到月份和日期。  
求Alie和Bob同時都在羅馬的日期有多少天。  

你可以假設兩個日期都在同一個年份內，而且不會有閏年。  
每月的天數分別為：[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]。  

# 解法
這題還算佛心，有保證兩個日期都在同一年內，我們只要轉換成兩個日期區間分別是當年的第幾天，問題就簡化成找區間交集。  
而且連每個月有幾天都給我們了，把它塞進陣列days，直接用索引值就可以拿到當月天數。  

轉換後得到Alice停留時間為[aa,al]，而Bob停留時間為[ba,bl]。  
區間的交集的左邊界s為兩者起始時間的較晚者，所以取max；而右邊界e為結束時間的較早者，所以取min。  
若s小於等於e則代表有交集，則回傳閉區間[s,e]的長度；無交集則回傳0。  

```python
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days=[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def f(s):
            M,D=map(int,s.split("-"))
            cnt=D
            for i in range(M-1):
                cnt+=days[i+1]
            return cnt
        
        aa=f(arriveAlice)
        al=f(leaveAlice)
        ba=f(arriveBob)
        bl=f(leaveBob)
        
        s=max(aa,ba)
        e=min(al,bl)
        
        if s<=e:
            return e-s+1
        else:
            return 0
```
