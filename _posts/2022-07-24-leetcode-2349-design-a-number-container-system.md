--- 
layout      : single
title       : LeetCode 2349. Design a Number Container System
tags        : LeetCode Medium Array HashTable SortedList
---
雙周賽83。有點尷尬的題目，看到10^9當然要想到二分搜，雖然沒有自己實作，但容器裡面確實是有用到。  

# 題目
設計數字容器系統：  
- 在某索引插入或替換一個數字  
- 回傳某數字的最小索引  

實作類別NumberContainers：  
- NumberContainers()：無參數建構子  
- void change(int index, int number)：將index對應的值設為number。若原本已經有值，則將其替換  
- int find(int number) 求值為number的最小索引。若無則回傳-1  

# 解法
根據題意，我們需要追蹤兩件事：  
1. 每個索引對應的值  
2. 每個值對應的索引  

第一項只需要簡單的雜湊表紀錄即可。至於第二項，因為需要找到最小的索引，必須使用有序的資料結構，使索引遞增排序，故選擇sorted list。  

每次find找到number對應的list，若為空則回傳-1，否則回傳第一個索引。  
每次change先檢查index是否已經被占用，若有則先清除舊的索引。將index對應的值設為number，再將index放入number對應的ist中。  

change清除舊索引、插入新索引複雜度都為O(log N)，整體O(N log N)。  
find直接取用第一個索引，複雜度O(1)。
雖然number和index可達10^9，但總共只會呼叫API最多10^5次，就算change全部集中在同一個值，最多也只會是10^5代入O(N log N)，算是可以接受的範圍。  

```python
from sortedcontainers import SortedList

class NumberContainers:

    def __init__(self):
        self.vals=defaultdict(SortedList)        
        self.mp=defaultdict(int)

    def change(self, index: int, number: int) -> None:
        if index in self.mp:
            oldv=self.mp[index]
            self.vals[oldv].remove(index)
        self.mp[index]=number
        self.vals[number].add(index)

    def find(self, number: int) -> int:
        if not self.vals[number]:
            return -1
        return self.vals[number][0]
```
