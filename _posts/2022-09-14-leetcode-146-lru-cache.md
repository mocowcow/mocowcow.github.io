--- 
layout      : single
title       : LeetCode 146. LRU Cache
tags        : LeetCode Medium LinkedList Design HashTable
---
面試常考題，終於找到時間來做個詳解。  
中文叫做**最近最不常使用**快取，但是**常使用**是指使用次數還是使用時間？要記住LRU重點是**上次的使用時間**，把最久沒用的踢出去。    
乾脆叫他**太久沒上會被踢**快取。  

# 題目
設計Least Recently Used (LRU) cache。  

實作LRUCache類別：  
- LRUCache(int capacity)：初始化快取容量為capacity  
- int get(int key)：如果key存在則回傳key的值，否則回傳-1  
- void put(int key, int value)：如果key存在，則以value更新值，否則將key加入快取中。若容量超過限制，則刪除最近最不常使用的key  

函數get和put的複雜度必須是O(1)。  

# 解法
LRU是使用doubly linked list搭配hash map來達成O(1)時間複雜度。  
hash map以key值紀錄對應的快取節點，每次存取O(1)。而linked list本身增刪動作也是O(1)。  
每次加入新節點時，只要將節點放到list頂端；而刪除節點時，也只是刪除list尾節點；至於更新現有節點值，可以分解成兩個步驟：刪除舊節點、加入新節點。  

在linked list實作的部分上，為了避免edge cases，在首尾分別加入dummy空節點，在刪除/插入時可以省略空節點判斷。  
除了題目要求的get和put，還需要額外寫兩個輔助函數add和remove：  
- add(Node node)：將node加入到list的頂端  
- remove(Node node)：將node從list中刪除  
- get(int key)：如果key存在，則將原有的節點刪除後重新加入到頂端，並回傳其值；否則回傳-1  
- set(int key, int value)：如果key存在，則先刪除舊節點。以key, value建立新節點，加入至list頂端。若超出容量限制則刪除list末端節點，並**清除對應的key值**  

![示意圖](/assets/img/146-1.jpg)

```python
class Node:
    __slots=['key','val','next','prev']
    def __init__(self,key=None,val=None):
        self.key=key
        self.val=val
        self.next=self.prev=None

class LRUCache:

    def __init__(self, capacity: int):
        self.dummy_head=Node()
        self.dummy_tail=Node()
        self.dummy_head.next=self.dummy_tail
        self.dummy_tail.prev=self.dummy_head
        self.mp={}
        self.cap=capacity

    def get(self, key: int) -> int:
        if key in self.mp:
            node=self.mp[key]
            self.remove(node)
            self.add(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            node=self.mp[key]
            self.remove(node)
        node=Node(key,value)
        self.mp[key]=node
        self.add(node)
        if len(self.mp)>self.cap:
            rmv=self.dummy_tail.prev
            self.remove(rmv)
            del self.mp[rmv.key]
    
    def remove(self, node):
        a=node.prev
        b=node.next
        a.next=b
        b.prev=a
    
    def add(self, node):
        a=self.dummy_head
        b=a.next
        a.next=node
        node.prev=a
        b.prev=node
        node.next=b
```
