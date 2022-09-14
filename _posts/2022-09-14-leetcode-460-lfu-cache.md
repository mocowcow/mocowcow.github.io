--- 
layout      : single
title       : LeetCode 460. LFU Cache
tags        : LeetCode Hard LinkedList Design HashTable
---
[LRU]({% post_url 2022-09-14-leetcode-146-lru-cache %})的好兄弟，打鐵陣熱一起做掉，但是花了好多時間才整理成好看的樣子。  
中文叫做**最少使用**快取，這次真的是把使用次數最少的踢掉，有多個次數相同就踢最久沒用過那個(也就是LRU)。  

# 題目
設計Least Frequently Used (LFU) cache。  

實作LFUCache類別：  
- LFUCache(int capacity)：初始化快取容量為capacity  
- int get(int key)：如果key存在則回傳key的值，否則回傳-1  
- void put(int key, int value)：如果key存在，則以value更新值，否則將key加入快取中。若容量超過限制，則應先刪除使用次數最少的key，才加入新的key。若平局則刪除**最久未使用**者  

你必須為每一個快取的key值維護一個**使用計數器**，而計數最小者即為**最少使用**的key。  
一個新的key加入快取時，他的計數器初始為1。之後每次執行put或是get都會使計數增加1。  

函數get和put的時間複雜度必須是O(1)。  

# 解法
與其說是LRU的好兄弟，不如說是他的爸爸。  
LFU使用一個hash map來維護數個不同使用頻率的doubly linked list(跟LRU差不多)，每當key被呼叫，就把它搬進下一個頻率的list中。  
另外還需要一個變數mn_freq來記錄所有key中的最低使用頻率是多少，這樣要刪除的時候才知道去哪邊找。  

先說說doubly linked list需要什麼功能：  
- add(Node node)：將node加入到list的頂端  
- remove(Node node)：將node從list中刪除  

然後實作LRU的函數：  
- get(int key)：如果key存在，則將節點**移到下一個頻率**的list頂端，並回傳其值；否則回傳-1  
- put(int key, int value)：如果key存在，則將節點**移到下一個頻率**，並更新其值；否則先檢查容量是否已滿，並以mn_freq找到最久未使用的key刪除。之後加入全新的key，頻率為1，故mn_freq也會變回1  

有沒有發現**移到下一個頻率**這個動作很冗長？給他一個專門的函數：  
- freq_up(Node node)：把該節點的頻率遞增1，然後移到正確的list頂端。記得要檢查刪完後mn_freq對應的list是否為空，而將mn_freq調整成正確的值  

有個比較特別的點，就是題目的**快取容量會設成0**，所以在put的時候如果cap為0，別做任何動作。  

```python
class Node:
    __slots=['key','val','next','prev','freq']
    def __init__(self,key=None,val=None,freq=0):
        self.key=key
        self.val=val
        self.freq=freq
        self.next=self.prev=None
        

class LinkedList:

    def __init__(self):
        self.dummy_head=Node()
        self.dummy_tail=Node()
        self.dummy_head.next=self.dummy_tail
        self.dummy_tail.prev=self.dummy_head
        self.size=0
    
    def remove(self, node):
        a=node.prev
        b=node.next
        a.next=b
        b.prev=a
        self.size-=1
    
    def add(self, node):
        a=self.dummy_head
        b=a.next
        a.next=node
        node.prev=a
        b.prev=node
        node.next=b
        self.size+=1
        
class LFUCache:

    def __init__(self, capacity: int):
        self.mp={}
        self.cap=capacity
        self.mn_freq=0
        self.d=defaultdict(LinkedList)

    def get(self, key: int) -> int:
        if key in self.mp:
            node=self.mp[key]
            self.freq_up(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.cap==0:
            return
        if key in self.mp:
            node=self.mp[key]
            self.freq_up(node)
            node.val=value
        else:
            if len(self.mp)==self.cap:
                self.remove_least_freq()
            node=Node(key,value,1)
            self.d[1].add(node)
            self.mp[key]=node
            self.mn_freq=1

    def freq_up(self,node):
        self.d[node.freq].remove(node)
        node.freq+=1
        self.d[node.freq].add(node)
        if self.d[self.mn_freq].size==0:
            self.mn_freq+=1
            
    def remove_least_freq(self):
        rmv=self.d[self.mn_freq].dummy_tail.prev
        self.d[self.mn_freq].remove(rmv)
        del self.mp[rmv.key]
```
