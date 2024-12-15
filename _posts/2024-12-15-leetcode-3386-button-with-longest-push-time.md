---
layout      : single
title       : LeetCode 3386. Button with Longest Push Time
tags        : LeetCode Easy Simulation
---
weekly contest 428。  
從 Q1 的題目就很讓人迷惑，寫得不開心。  

## 題目

輸入二維整數陣列 events，代表一個小孩按下鍵盤的時間。  

每個 events[i] = [index <sub>i</sub>, time <sub>i</sub>] 代表在時間 time <sub>i</sub> 按下按鍵 index <sub>i</sub>。  

- events 按照 time 遞增排序。  
- 按下按鍵的耗時是兩次**連續**按下事件的**時間差**。  
    第一次按鍵的所需時間即為該時間戳。  

求**耗時最長**的按鍵編號。  
若有多個耗時相同，則回傳**編號最小**者。  

## 解法

這題意不太好懂，還看看測資怎麼搞才知道**連續**指的應該是**兩次相鄰事件**。  
有人以為是**同一顆按鍵**按下兩次間的時間差，那就錯了。  

順代一提，原文要求答案是：  
> **button** with the smallest index  

千萬不要誤以為是 events 的 index。  

---

每次按下，時間差為 times[i] - prev。  
第一次按的耗時為 events[0][1]，方便起見 prev 初始值為 0。  

其餘按照題意模擬即可。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        ans = -1
        mx = -inf
        prev = 0
        for idx, time in events:
            diff = time - prev
            if diff > mx:
                mx = diff
                ans = idx
            elif diff == mx and idx < ans:
                ans = idx
                
            prev = time

        return ans
```
