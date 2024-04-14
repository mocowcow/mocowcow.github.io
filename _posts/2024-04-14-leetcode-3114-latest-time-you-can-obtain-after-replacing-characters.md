---
layout      : single
title       : LeetCode 3114. Latest Time You Can Obtain After Replacing Characters
tags        : LeetCode Easy String
---
周賽 393。Q1 難度突然上升，平均每人錯兩次，個人覺得比 Q2 還難。  

## 題目

輸入字串 s 代表 12 小時制的時間，其中某些數字被 "?" 取代 (也可能沒有)。  

12 小時制以 "HH:MM" 表示，其中 HH 介於 [00, 11] 之間，而 MM 介於 [00, 59] 之間。  
最早的時間是 00:00，最晚的時間是 11:59。  

你必須將 s 中所有 "?" 替換成其他數字，得到一個**合法**且最晚的時間。  

回傳替換過後的字串。  

## 解法

時間分成小時 HH 和分鐘 MM 兩部分。  

其中 MM 比較單純，第一位一律換成 5；第二位的一律換成 9。  

但是 HH 的部分比較麻煩，兩個數字會互相影響，不能隨便填。  
第一位只有在第二位是 0,1,? 的情形才能填 1；否則只能填 0，不然會超過 12 小時限制。  
第二位只有在第一位是 0 的情形才能填 9；否則只能填1。  

時間複雜度 O(1)。  
空間複雜度 O(1)，答案空間不計入。  

```python
class Solution:
    def findLatestTime(self, s: str) -> str:
        a = list(s)
        # hour
        if a[0] == "?":
            if a[1] in "01?":
                a[0] = "1"
            else:
                a[0] = "0"
                
        if a[1] == "?":
            if a[0] == "0":
                a[1] = "9"
            else:
                a[1] = "1"
            
        # min
        if a[3] == "?":
            a[3] = "5"
            
        if a[4] == "?":
            a[4] = "9"
        
        return "".join(a)
```
