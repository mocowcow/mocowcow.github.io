---
layout      : single
title       : LeetCode 732. My Calendar III
tags 		: LeetCode Hard Design SegmentTree
---
行事曆系列第三題，線段樹打天下，我永遠喜歡線段樹。

# 題目
你在設計一個行事曆系統，每次可以新增一段期間的行程。每趟行程[start,end)為左閉右開，代表start~end-1的連續範圍。  

實作類別MyCalendar：  
1. 無參數建構子  
2. boolean book(int start, int end)，在[start,end)增加一個行程，並回傳整個行事曆中的最大行程重疊數。

# 解法
這次的需求要用到範圍加法、範圍最大值，將先前的線段樹稍微修改一下。  
因為永遠都是求整棵樹的最大值，所以就把query函數砍掉，每次直接回傳root的最大值即可。  

範圍加法時，對每一個節點都加的話太過沒有效率，因此使用lazy propagation，代表整個範圍的異動值，只有下方節點有需要單獨操作時，才會將lazy值往下推。  
加法時：  
- 若節點和行程範圍無交集，直接跳出  
- 若節點完全被行程所涵蓋，則將lazy值+1  
- 否則將lazy值下放至子節點，正確進行完加法後更新當前節點最大值

```python
class Node:
    def __init__(self, L, R, mx):
        self.L = L
        self.R = R
        self.mx = mx
        self.lazy = 0
        self.left = self.right = None


class SegmentTree:
    def __init__(self, L, R):
        self.root = Node(L, R, 0)

    def update(self, i, j, inc):
        self._u(self.root, i, j, inc)
        return self.root.mx+self.root.lazy

    def _u(self, node, i, j, inc):
        if i > node.R or j < node.L:  # out of range
            return
        if i <= node.L and j >= node.R:  # fully covered
            node.lazy += inc
            return
        M = (node.L+node.R)//2
        if not node.left:
            node.left = Node(node.L, M, node.mx)
            node.right = Node(M+1, node.R, node.mx)
        if node.lazy:
            node.mx += node.lazy
            node.left.lazy += node.lazy
            node.right.lazy += node.lazy
            node.lazy = 0
        if M >= i:
            self._u(node.left, i, j, inc)
        if M < j:
            self._u(node.right, i, j, inc)
        node.mx = max(node.left.mx+node.left.lazy, node.right.mx+node.right.lazy)


class MyCalendarThree:

    def __init__(self):
        self.st = SegmentTree(0, 10**9+5)

    def book(self, start: int, end: int) -> int:
        return self.st.update(start, end-1, 1)
```

官方建議解答是這樣，試想一個線性時間，對每個行程的開始時間標記+1，結束時標記-1，這樣就可以得到最大的併行數量。  

```python
class MyCalendarThree:

    def __init__(self):
        self.event=defaultdict(int)

    def book(self, start: int, end: int) -> int:
        self.event[start]+=1 # event start
        self.event[end]-=1 # event end

        overlap=0
        k=0
        for time in sorted(self.event.keys()):
            overlap+=self.event[time]
            k=max(k,overlap)
        
        return k
```