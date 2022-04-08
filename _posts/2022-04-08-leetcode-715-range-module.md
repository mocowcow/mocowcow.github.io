---
layout      : single
title       : LeetCode 715. Range Module
tags 		: LeetCode Hard Design SegmentTree
---
又拿動態開點線段樹來刷題數了，merge邏輯稍微改改又是一題hard。

# 題目
Range Module可以用來追蹤某一個範圍的數字，每個範圍[left, right)左閉右開，代表left~right-1內的所有數字。

實作類別RangeModule：  
1. 無參數建構子  
2. void addRange(int left, int right)，將[start,end)範圍全部追蹤  
3. boolean queryRange(int left, int right)，查詢[start,end)範圍全部內是否全部為追蹤中  
4. void removeRange(int left, int right)，將[start,end)範圍全部取消追蹤  

# 解法
每次修改線段樹時，幾乎只要更改query函數超界時的預設值，還有兩節點合併的merge邏輯就可以。  
題目要求範圍內所有數字都要被追蹤，所以merge邏輯使用and。節點超出查詢範圍時，因為是做and運算，回傳True才不會汙染查詢結果。  

```python
class Node:
    def __init__(self, L, R, used):
        self.L = L
        self.R = R
        self.used = used
        self.left = self.right = None


class SegmentTree:
    def __init__(self, L, R):
        self.root = Node(L, R, False)

    def query(self, i, j):
        return self._q(self.root, i, j)

    def _q(self, node, i, j):
        if i > node.R or j < node.L:  # out of range
            return True
        if i <= node.L and j >= node.R:  # fully covered
            return node.used
        if not node.left:
            return node.used
        return self._q(node.right, i, j) and self._q(node.left, i, j)

    def update(self, i, j, used):
        self._u(self.root, i, j, used)

    def _u(self, node, i, j, used):
        if i > node.R or j < node.L:  # out of range
            return
        if i <= node.L and j >= node.R:  # fully covered
            node.used = used
            node.left = node.right = None
            return
        M = (node.L+node.R)//2
        if not node.left:
            node.left = Node(node.L, M, node.used)
            node.right = Node(M+1, node.R, node.used)
        if M >= i:
            self._u(node.left, i, j, used)
        if M < j:
            self._u(node.right, i, j, used)
        node.used = node.left.used and node.right.used


class RangeModule:

    def __init__(self):
        self.st=SegmentTree(0,10**9+5)

    def addRange(self, left: int, right: int) -> None:
        self.st.update(left,right-1,True)

    def queryRange(self, left: int, right: int) -> bool:
        return self.st.query(left,right-1)

    def removeRange(self, left: int, right: int) -> None:
        self.st.update(left,right-1,False)
```

