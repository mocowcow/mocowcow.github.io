--- 
layout      : single
title       : LeetCode 2671. Frequency Tracker
tags        : LeetCode Medium Array HashTable
---
周賽344。

# 題目
設計一個資料結構，可以紀錄各元素的出現次數，並查詢是否有任意元素的出現次數正好是某個值。  

實作類別FrequencyTracker：  
- 無參數建構子  
- void add(int number)：加入一個number  
- void deleteOne(int number)：刪除一個number。若不存在number則不做動作  
- bool hasFrequency(int frequency)：若有任何元素正好出現frequency則回傳true，否則回傳false  

# 解法
維護兩個雜湊表cnt和freq，cnt用來記**數字出現次數**，而freq用來記**正好出現x次的數字有幾種**。  

add(number)時，先看number本來出現x次，把freq[x]減1。然後把number計數加1，freq[x]也加1。  
deleteOne(number)時，若x=0則不動作；否則把freq[x]減1。然後把number計數減1，freq[x]也加1。  
hasFrequency(frequency)，直接查freq中查正好出現frequency次的數字是否至少1種。  

以上三種操作都是O(1)，最多N次，時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class FrequencyTracker:

    def __init__(self):
        self.cnt=Counter()
        self.freq=Counter()

    def add(self, number: int) -> None:
        self.freq[self.cnt[number]]-=1
        self.cnt[number]+=1
        self.freq[self.cnt[number]]+=1

    def deleteOne(self, number: int) -> None:
        if self.cnt[number]==0:
            return
        self.freq[self.cnt[number]]-=1
        self.cnt[number]-=1
        self.freq[self.cnt[number]]+=1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency]>0
```
