--- 
layout      : single
title       : LeetCode 2336. Smallest Number in Infinite Set
tags        : LeetCode Medium Design HashTable
---
周賽301。個人覺得這題比Q1還簡單，可能因為測資不夠大。

# 題目
你有一個包含所有正整數的無限集合[1,2,3,4,5..]。  

設計類別SmallestInfiniteSet：
- SmallestInfiniteSet()：無參數建構子
- int popSmallest()：刪除並回傳集合中的最小值  
- void addBack(int num)：若num不在集合中，則將其加回集合  

# 解法
既然都說是無限集合，當然別想把所有數字都存起來，只能從1開始循序向後取用。  
而且還要符合加回功能，如果num已經出現過，則加到back中。  
每次取出數字，優先取出back中最小值；若back為空才使用新的數字。  

因為最多只會有1000次動作，就算遍歷back找最小值，複雜度O(N^2)也沒關係。  
如果測資大一點，可能要考慮將集合換成sorted list。

```python
class SmallestInfiniteSet:

    def __init__(self):
        self.back=set()
        self.n=0

    def popSmallest(self) -> int:
        if self.back:
            mn=min(self.back)
            self.back.remove(mn)
            return mn
        self.n+=1
        return self.n

    def addBack(self, num: int) -> None:
        if num<=self.n and num not in self.back:
            self.back.add(num)
```

使用現成的有序集合也可以。  
直接將1000個數字加到集合中，有序集合會以遞增排序，所以第一個元素永遠會是最小值。  

```python
from sortedcontainers import SortedSet

class SmallestInfiniteSet:

    def __init__(self):
        self.s=SortedSet(range(1,1005))

    def popSmallest(self) -> int:
        return self.s.pop(0)

    def addBack(self, num: int) -> None:
        self.s.add(num)
```
