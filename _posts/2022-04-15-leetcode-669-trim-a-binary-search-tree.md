---
layout      : single
title       : LeetCode 669. Trim a Binary Search Tree
tags 		: LeetCode Medium BinaryTree DFS
---
每日題。看到官方解答跟我寫的幾乎一樣，然後底下有老哥留言：  
> Exactly what I did. So proud of myself :)  

我也替他感到驕傲！

# 題目
輸入一顆二元搜尋樹，以及整數low, high。把不在[low, high]範圍內的節點刪掉，並回傳修剪過後的二元搜尋樹。  
修剪時必須保持各節點的相對位置，且只有一種正確答案。根節點可能會根據界限不同而改變。

# 解法
二元搜尋樹的特性，左子樹節點一定小於父節點，右子樹節點一定大於父節點。  
所以能夠確定：  
- 若當前節點小於low，那麼他的左子樹一定也都小於low，所以只要遞迴處理右子樹  
- 若當前節點大於high，那麼他的右子樹一定也都大於high，所以只要遞迴處理左子樹  
- 否則保留當前節點，但是遞迴處理左右子樹後回傳  

```python
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val<low:
            return self.trimBST(root.right,low,high)
        if root.val>high:
            return self.trimBST(root.left,low,high)
        root.left=self.trimBST(root.left,low,high)
        root.right=self.trimBST(root.right,low,high)
        return root
```

