---
layout      : single
title       : LeetCode 230. Kth Smallest Element in a BST
tags 		: LeetCode Medium BinarySearchTree DFS
---
這幾天每日題好像都是二元樹。

## 題目
輸入一棵二元搜尋樹root，找到裡面第k小的節點值。

## 解法
二元搜尋樹的特性是：左方子樹的所有節點一定小於當前節點，而右方子樹所有節點一定大於當前節點。  
最簡單暴力的就是中敘dfs遍歷整棵樹，把節點通通撈出來，再回傳第k-1位置的節點。  

```python
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes=[]
        
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            nodes.append(node.val)
            dfs(node.right)
            
        dfs(root)
            
        return nodes[k-1]
```

看到有種O(H+k)的解法，H為樹的高度。  
二元搜尋樹最小的節點一定在左方，因為很重要所以再說一次。  
從root開始，一直不斷往左下方，並把沿途的節點塞入stack中，直到節點為空為止。  
取出stack最頂層的節點，若滿足第k個節點則回傳；否則繼續找接下來的節點，有右子樹的話優先把右子樹壓入stack。

```python
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        st=[]
        curr=root
        while 1:
            #go leftmost node
            while curr:
                st.append(curr)
                curr=curr.left
            curr=st.pop()
            k-=1
            if k==0:
                return curr.val
            curr=curr.right
```