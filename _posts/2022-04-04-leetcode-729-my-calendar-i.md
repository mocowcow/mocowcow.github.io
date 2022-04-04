---
layout      : single
title       : LeetCode 729. My Calendar I
tags 		: LeetCode Medium Design SegmentTree BinarySearchTree SortedList BinarySearch
---
用牛刀殺雞，最後還變成電宰場了。  
從最初的的暴力法不斷進化，到sorted list(有序串列?)，又到二分搜尋樹，最後是動態開點線段樹。

# 題目
你在設計一個行事曆系統，每次可以新增一段期間的行程，且所有行程不可以有所重疊。每趟行程[start,end)為左閉右開，代表start~end-1的連續範圍。  

實作類別MyCalendar：  
1. 無參數建構子  
2. boolean book(int start, int end)，檢查[start,end)是否不存在任何行程，若是則將此行程預定，否則不動作。

# 解法
測資說最大只會有1000筆行程，暴力法O(N^2)其實還不錯。  
陣列book保存所有已訂的行程，每次加入時遍歷book確保沒有重疊，之後再加入新的行程即可。  

```python
class MyCalendar:

    def __init__(self):
        self.book = []

    def book(self, start: int, end: int) -> bool:
        for itv in self.book:
            if start >= itv[1] or end <= itv[0]:
                continue
            else:
                return False
        self.book.append((start, end))
        return True
```

前幾天學的sorted list，用來排不重複區間正合適。  
初始化的時候先用最大最小值padding，這樣就不用處理索引位置為0或是N-1時的特例。  
以start值去找第一個大於等於值的索引i，如果calendar[i-1]的結束時間大於start，則代表前一個行程末端會和當前重複，所以不合法。又或是calendar[i]的起始時間小於end，代表當前行程的尾端會和下一個行程重複到，所以也不合法。

```python
from sortedcontainers import SortedList

class MyCalendar:

    def __init__(self):
        self.calendar=SortedList([(-math.inf,-math.inf),(math.inf,math.inf)])

    def book(self, start: int, end: int) -> bool:
        i=self.calendar.bisect_left((start,end))
        if self.calendar[i-1][1]>start or end>self.calendar[i][0]:
            return False
        self.calendar.add((start,end))
        return True
```

官方解答看到二分搜尋樹，就試著做了一次。  
初始化root為樹節點為(-1,-1)，任何一個不在合法範圍內的值其實也都可以。  
每次book時直接對樹插入新節點，看是否成功。  

每次插入節點時從root開始，分成三種情況：  
1. 新節點的end大於等於當前節點start，往右子樹插入  
2. 新節點的start小於等於當前節點end，往左子樹插入  
3. 不滿足以上兩點，則代表有重疊，回傳false  

```python
class Node:
    
    def __init__(self,start,end):
        self.start=start
        self.end=end
        self.left=self.right=None

    def insert(self,node):
        if node.start>=self.end:
            if not self.right:
                self.right=node
                return True
            return self.right.insert(node)
        elif node.end<=self.start:
            if not self.left:
                self.left=node
                return True
            return self.left.insert(node)
        return False
    
class MyCalendar:

    def __init__(self):
        self.root=Node(-1,-1)

    def book(self, start: int, end: int) -> bool:
        return self.root.insert(Node(start,end))
```

最後是非常重型的線段樹，因為行程最大到10^9，普通的陣列線段樹記憶體一定爆炸，我特地去學了動態開點，搞了五天才把BUG全部修完。  
簡單說就是每次要book時先查詢該範圍，確認全部都沒被訂過才把範圍改為已排程。  

每個樹節點儲存左邊界L、右邊界R、該區段的預訂狀態book、左右子區段節點。  
線段樹初始化時設立根節點範圍為(0,10^9)。  
每次查詢區段(i,j)時：  
- 和當前節點位置沒有交集，回傳false  
- 節點完全被(i,j)覆蓋，回傳當前的預訂狀態book  
- 如果沒有子節點，代表子節點所有值和當前節點相同，直接回傳當前book  
- 剩下就是只有左半或右半重疊，將兩個子查詢合併再回傳  

每次更新區段(i,j)時：  
- 和當前節點位置沒有交集，不動作  
- 節點完全被(i,j)覆蓋，直接將當前book改為true  
- 分別更新左右子節點，將當前book設為子節點合併的結果  

```python
class Node:
    def __init__(self, L, R, book):
        self.L = L
        self.R = R
        self.book = book
        self.left = self.right = None


class SegmentTree:
    def __init__(self, L, R):
        self.root = Node(L, R, False)

    def query(self, i, j):
        return self._q(self.root, i, j)

    def _q(self, node, i, j):
        if i > node.R or j < node.L:  # out of range
            return False
        if i <= node.L and j >= node.R:  # fully covered
            return node.book
        if not node.left:
            return node.book
        return self._q(node.right, i, j) or self._q(node.left, i, j)

    def update(self, i, j):
        self._u(self.root, i, j)

    def _u(self, node, i, j):
        if i > node.R or j < node.L:  # out of range
            return
        if i <= node.L and j >= node.R:  # fully covered
            node.book = True
            node.left = node.right = None
            return
        M = (node.L+node.R)//2
        if not node.left:
            node.left = Node(node.L, M, node.book)
            node.right = Node(M+1, node.R, node.book)
        if M >= i:
            self._u(node.left, i, j)
        if M < j:
            self._u(node.right, i, j)
        node.book = node.left.book or node.right.book

class MyCalendar:

    def __init__(self):
        self.st=SegmentTree(0,10**9+5)

    def book(self, start: int, end: int) -> bool:
        if self.st.query(start,end-1):
            return False
        self.st.update(start,end-1)
        return True
```