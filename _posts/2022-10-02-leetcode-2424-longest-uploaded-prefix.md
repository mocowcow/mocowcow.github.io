--- 
layout      : single
title       : LeetCode 2424. Longest Uploaded Prefix
tags        : LeetCode Medium Design SortedList HashTable
---
雙周賽88。這題反而比Q1簡單多了，應該把兩題交換。  

# 題目
你會收到n個影像的的串流，每個影像由1\~n的不重複數字表示，要將這些影向上傳到伺服器。現在需要一個資料結構，在上傳過程中計算出**已上傳的最長影像前綴**。  

如果1到i(包含)範圍內的所有影像都已上傳，則認為i是影像的前綴。**最長上傳前綴**是滿足這個定義的所有i中的最大值。  

實作類別LUPrefix：  
- LUPrefix(int n)：初始化n個影像  
- void upload(int video)：將影像上傳到伺服器  
- int long() 回傳**已上傳的最長影像前綴**  

# 解法
與其說是前綴，不如說下載一半的影片從頭開始播放可以連續放多久，這樣應該更貼切。  

我們需要一個雜湊表s來記錄上傳過的影像，以及變數last紀錄當前前綴。  
而只有在上傳某段影像後，才有可能使前綴增加。所以在upload時先加入新的影像，檢查當前前綴的下一格影像是否也存在，若存在則不斷增加前綴。  

因為每個影像最多只會被加入一次，也只會被計入前綴一次，所以時間複雜度O(n)。空間複雜度也是O(n)。  

```python
class LUPrefix:

    def __init__(self, n: int):
        self.n=n
        self.last=0
        self.s=set()

    def upload(self, video: int) -> None:
        self.s.add(video)
        while self.last+1 in self.s:
            self.last+=1

    def longest(self) -> int:
        return self.last
```

看到第一名大神的寫法，效率比較差，但確實是可行。  
將1\~n+1的數都加入sorted list中，每次上傳則將影像從list移除，前綴則是list中最小元素減一。  

因為在sorted list中增刪為O(log n)，所以整體時間複雜度為O(n log n)，但空間複雜度還是O(n)。  

```python
from sortedcontainers import SortedList

class LUPrefix:

    def __init__(self, n: int):
        self.sl=SortedList()
        for i in range(1,n+2):
            self.sl.add(i)

    def upload(self, video: int) -> None:
        self.sl.remove(video)
                
    def longest(self) -> int:
        return self.sl[0]-1
```