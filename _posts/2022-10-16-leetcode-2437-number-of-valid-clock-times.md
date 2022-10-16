--- 
layout      : single
title       : LeetCode 2437. Number of Valid Clock Times
tags        : LeetCode Easy String
---
雙周賽89。超級麻煩的題，很意外我沒有拿到WA就通過。  

# 題目
輸入長度5的字串time，以格式"hh:mm"表示時間。最早的可能時間為"00:00"，最晚的可能時間為"23:59"。  
在time中，由?符號表示數字未知，必須由0\~9的數字來替換。  

回傳整數ans，代表替換所有?符號後，能夠有幾種合法的時間格式。  

# 解法
一開始想說該不會要四個迴圈，分別替換四個位置的問號，再來檢查是否合法。這樣時間複雜度頂多O(10^4)，其實可行，但是24小時和60分鐘的格式檢查起來非常麻煩，直接放棄這個做法。  

後來才驚覺可以透過列舉所有以秒為單位的時間點，轉換為hh:mm格式後再來和規定的time格式做匹配，若可以由time生成，則答案+1。  

每次都固定窮舉1440個時間點，時空間複雜度O(1)。  

```python
class Solution:
    def countTime(self, time: str) -> int:
        a,b,_,c,d=list(time)
        ans=0

        for t in range(1440):
            h=t//60
            m=t%60
            
            h1=str(h//10)
            h2=str(h%10)
            m1=str(m//10)
            m2=str(m%10)
            
            if a!='?' and a!=h1:
                continue
            if b!='?' and b!=h2:
                continue
            if c!='?' and c!=m1:
                continue
            if d!='?' and d!=m2:
                continue
    
            ans+=1
        
        return ans
```
