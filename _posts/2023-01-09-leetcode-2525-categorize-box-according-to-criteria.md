--- 
layout      : single
title       : LeetCode 2525. Categorize Box According to Criteria
tags        : LeetCode Easy Array
---
雙周賽95。又是超多名詞的臭長題。Bulky和Heavy的差別我還真分不太清楚。  

# 題目
輸入四個整數length, width, height和mass，分別代表箱子的尺寸和質量，回傳箱子所屬**類型**的字串。  

- 若箱子任一邊長至少10^4，或是其容量至少10^9，則稱為"Bulky"  
- 若箱子質量至少100，則稱為"Heavy"  
- 若箱子是"Bulky"也是"Heavy"，其類別為"Both"  
- 若箱子不是"Bulky"也不是"Heavy"，其類別為"Neither"  
- 若箱子是"Bulky"但不是"Heavy"，其類別為"Bulky"  
- 若箱子不是"Bulky"但是"Heavy"，其類別為"Heavy"  

# 解法
先分別判斷是否為Bulky或Heavy，在依照四種情況分類決定類別。  

時間複雜度O(1)。空間複雜度O(1)。  

```python
class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        bk=False
        hv=False
        
        if max(length,width,height)>=10**4:
            bk=True
            
        if length*width*height>=10**9:
            bk=True
            
        if mass>=100:
            hv=True
            
        if bk and hv:
            return "Both"
        
        if not bk and not hv:
            return "Neither"
        
        if bk:
            return "Bulky"
        
        return "Heavy"
```

或是先對四種情況建表，以bk, hv兩變數分別代表Bulky和Heavy，若符合則設為1，最後用變數去查表。  

時間複雜度O(1)。空間複雜度O(1)。  

```python
class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        bk=0
        hv=0
        
        if max(length,width,height)>=10**4:
            bk=1
            
        if length*width*height>=10**9:
            bk=1
            
        if mass>=100:
            hv=1
            
        category=[
            ["Neither","Heavy"],
            ["Bulky","Both"]
        ]
        
        return category[bk][hv]
```