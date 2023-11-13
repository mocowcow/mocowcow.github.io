---
layout      : single
title       : LeetCode 2933. High-Access Employees
tags        : LeetCode Medium Array String HashTable Sorting Simulation
---
周賽371。題目很長的綜合練習題，python寫起來還算普通，其他語言可能有點麻煩。  

## 題目

輸入長度n的二維字串陣列access_times。其中access_times[i][0]代表員工名字，而access_times[i][1]代表該員工的訪問時間點。  
所有存取紀錄都是在同一天內。  

存取時間以**四個數字**的字串組成，為**24小時制**。例如："0800"或"2250"。  

如果某個員工在**一小時**的時間段內存取**三次或以上**，則稱為**高存取**。  
若兩次存取正好差了一小時，則**不**視作同一個時間段。例如："0815"和"0915"**不**屬同一時間段。  

跨日的訪問也不算在同一個時間段。例如："0005"和"2350"**不**屬同一時間段。  

求**高存取**員工的名單，並以任意順序回傳。  

## 解法

題目還算有良心，說了一小時的時間段，是**閉區間**，頭尾差必須小於60分鐘。  
而且還不用考慮跨日。  

以字串判斷時間很麻煩，先統一轉成**分鐘**，比較方便判斷。例如"0815"轉成60\*8+15 = 495。  
然後依照員工別分類其存取時間。  

遍歷每個員工，先將存取時間排序，檢查有沒有哪個時間段包含至少三次存取，有就加入答案。  
枚舉存取時間i，可以透過二分、滑動窗口等方式找到間。  
但我們只需要知道有沒有三次，而不在乎時間段內的總次數，直接判斷i+2和i的差小於60或否即可。  

```python
def f(s):
    h=int(s[:2])
    m=int(s[2:])
    return h*60+m
    
def high(v):
    v.sort()
    N=len(v)
    for i in range(N-2):
        if v[i+2]-v[i]<60:
            return True
    return False

class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        d=defaultdict(list)
        for name,time in access_times:
            d[name].append(f(time))
            
        ans=[]
        for k,v in d.items():
            if high(v):
                ans.append(k)
                
        return ans
```
