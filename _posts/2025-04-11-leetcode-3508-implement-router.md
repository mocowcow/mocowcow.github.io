---
layout      : single
title       : LeetCode 3508. Implement Router
tags        : LeetCode Medium Simulation SortedList BinarySearch HashTable
---
weekly contest 444。

## 題目

<https://leetcode.com/problems/implement-router/description/>

## 解法

這個路由器遵循 FIFO (First In Frist Out)，所有封包依先來後到的順序處理。  
符合先進先出的資料結構便是佇列 queue。  
在添加封包時不允許重複，所以還需要一個 set 去重。  

---

比較麻煩的是 getCount(destination, startTime, endTime)。  
需要按 destination 分組，找出時間段 [startTime, endTime] 內的封包數。  

分組很簡單，就是拿 destination 雜湊到對應的組別。  
至於計數，可以在組內二分找**第一個大於等於** startTime 的位置 s，還有**第一個大於** endTime 的位置 e。  
答案個數即為 e - s。  

注意：deque 的底層類似 linked list，隨機存取是 O(N)，不適合二分。  
為了有效率的二分，此處應選用 sorted list。  

時間複雜度 O(Q log min(memoryLimit, Q))。  
空間複雜度 O(min(memoryLimit, Q))。  

```python
from sortedcontainers import SortedList as SL

class Router:

    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.q = deque()
        self.vis = set()
        self.group = defaultdict(SL)  # group by dest

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source,  destination, timestamp)
        if packet in self.vis:
            return False
        self.q.append(packet)
        self.vis.add(packet)
        self.group[destination].add(timestamp)
        if len(self.q) > self.limit:
            self.forwardPacket()
        return True

    def forwardPacket(self) -> List[int]:
        if not self.q:
            return []
        packet = self.q.popleft()
        self.vis.remove(packet)
        self.group[packet[1]].pop(0)
        return packet

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        g = self.group[destination]
        s = g.bisect_left(startTime)
        e = g.bisect_right(endTime)
        return e-s

```
