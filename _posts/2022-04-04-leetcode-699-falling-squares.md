---
layout      : single
title       : LeetCode 699. Falling Squares
tags 		: LeetCode Hard Array SegmentTree
---
普通線段樹一樣沒辦法過的超大測資，動態開點順利解決。  
後來看提示才知道出題者想考的是座標壓縮+普通的線段樹。沒錯，動態開點就是這麼任性。

# 題目
在一個2D平面上，有N個方塊要落下來。  
輸入二維陣列positions，其中positions[i]代表(方塊i的左邊界, 方塊i的邊長)。  
每個方塊會疊在落下範圍內的最高點上，回傳陣列ans，ans[i]表示第i個方塊落下後，目前的最高高度。


# 解法
用range maximum query線段樹，初始化範圍(0,10^8)，並維護變數mx紀錄最高高度。  
遍歷positions，每次查詢方塊落下範圍的最大值oldHeight，得到newHeight為oldHeight+邊長，將落下範圍最大值更新為newHeight。並以newHeight更新mx，最後將mx加入答案中。

```python
class Node:
    def __init__(self, L, R, mx):
        self.L = L
        self.R = R
        self.mx = mx
        self.left = self.right = None


class SegmentTree:
    def __init__(self, L, R):
        self.root = Node(L, R, 0)

    def query(self, i, j):
        return self._q(self.root, i, j)

    def _q(self, node, i, j):
        if i > node.R or j < node.L:  # out of range
            return 0
        if i <= node.L and j >= node.R:  # fully covered
            return node.mx
        if not node.left:
            return node.mx
        return max(self._q(node.right, i, j), self._q(node.left, i, j))

    def update(self, i, j, val):
        self._u(self.root, i, j, val)

    def _u(self, node, i, j, val):
        if i > node.R or j < node.L:  # out of range
            return
        if i <= node.L and j >= node.R:  # fully covered
            node.mx = val
            node.left = node.right = None
            return
        M = (node.L+node.R)//2
        if not node.left:
            node.left = Node(node.L, M, node.mx)
            node.right = Node(M+1, node.R, node.mx)
        if M >= i:
            self._u(node.left, i, j, val)
        if M < j:
            self._u(node.right, i, j, val)
        node.mx = max(node.left.mx, node.right.mx)


class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        st = SegmentTree(0, 10**8+5)
        ans = []
        mx = 0
        for left, side in positions:
            oldHeight = st.query(left, left+side-1)
            newHeight = oldHeight+side
            st.update(left, left+side-1, newHeight)
            mx = max(mx, newHeight)
            ans.append(mx)

        return ans
```

2022-6-2更新。  
這幾天一直複習線段樹，又回來練這題，結果發現這題用座標壓縮執行時間更快，也更好寫ㄋ。  

```python
class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        co=set()
        for l,size in positions:
            co.add(l)
            co.add(l+size-1)
        
        co=sorted(co)
        ans=[]
        height=[0]*len(co)
        mx=0
        for l,size in positions:
            start=bisect_left(co,l)
            end=bisect_right(co,l+size-1)
            curr=0
            for i in range(start,end):
                curr=max(curr,height[i])
            new_height=curr+size
            for i in range(start,end):
                height[i]=new_height
            mx=max(mx,new_height)
            ans.append(mx)
                
        return ans
```