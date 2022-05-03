--- 
layout      : single
title       : LeetCode 1146. Snapshot Array
tags        : LeetCode Medium Array HashTable BinarySearch Design
---
二分搜學習計畫。有點像是陣列的更新紀錄，又或是整個陣列的差分陣列。

# 題目
設計一個資料結構，可以查詢在特定時間點的陣列數值。  
實作以下類別：  
- 建構子，初始化陣列長度為length  
- void set(index, val)，將index處元素設為val  
- int snap()，對陣列儲存當前狀態的快照，並回傳快照編號(編號是snap()呼叫次數-1)  
- int get(index, snap_id)，選擇編號第snap_id張快照，並回傳當時index的值  

# 解法
陣列長度N最大50000，最多會呼叫50000次。如果想要保存整個陣列*snap次，最多需要50000^2的空間，一定MLE。  
結果我一開始選擇掃描整個陣列是否修改過，變成50000^2次運算，拿個一個TLE。正確解法應該是在set呼叫時紀錄修改索引。  

對每個索引位置i建立差分陣列log，以(id,val)的方式表示在第id次快照時數值發生變化，需初始化為[(-1,0)]，防止某個索引全程沒有被修改而出現查詢錯誤。  
另外還需要整數id紀錄快照編號，雜湊表modified紀錄修改過的索引位置及數值。  

每次呼叫set時，在modified中記錄索引位置及值。  
snap時，將所有修改過的索引位置及新值加入對應的log中，最後清空modified。  
最重點的get，以二分搜在log[index]中，找到第一個大於snap_id的位置，將其-1，得到最後一個小於等於snap_id的位置i，log[index][i]則為當時的數值。

```python
class SnapshotArray:

    def __init__(self, length: int):
        self.log=[[(-1,0)] for _ in range(length)]
        self.id=-1
        self.modified={}

    def set(self, index: int, val: int) -> None:
        self.modified[index]=val

    def snap(self) -> int:
        self.id+=1
        for i in self.modified:        
            self.log[i].append((self.id,self.modified[i]))
        self.modified.clear()
        return self.id

    def get(self, index: int, snap_id: int) -> int:
        i=bisect_right(self.log[index],(snap_id,math.inf))-1
        return self.log[index][i][1]

```
