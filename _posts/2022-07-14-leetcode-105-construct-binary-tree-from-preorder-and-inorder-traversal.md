--- 
layout      : single
title       : LeetCode 105. Construct Binary Tree from Preorder and Inorder Traversal
tags        : LeetCode Medium Array DevideAndConquer HashTable Tree BinaryTree
---
每日題。超級經典的遞迴題，當初我還手畫了幾次圖才理解這在幹什麼，滿佩服想出這種考題的人。  

# 題目
輸入兩個整數陣列preorder和inorder，其中preorder是二元樹的前序遍歷結果，inorder中序遍歷的結果，構造並返回二叉樹。

# 解法
preorder順序為[根節點, 左子樹, 右子樹]，只能知道每個節點作為子樹根節點的順序，但無法判斷無判斷出現位置。  
而inorder順序為[左子樹, 根節點, 右子樹]，只能看出個某根節點的左右子節點，但不知道誰是根。  

但是兩個一起看，先從preorder中找到根節點，拿到inorder中找到出現位置idx，左半邊為左子樹，右半邊則為右子樹。  

![示意圖](/assets/img/105-1.jpg)

不斷遞迴下去，直到陣列為空，回傳null。  

```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        val=preorder[0]
        idx=inorder.index(val)
        node=TreeNode(val)
        node.left=self.buildTree(preorder[1:idx+1],inorder[:idx])
        node.right=self.buildTree(preorder[idx+1:],inorder[idx+1:])
        
        return node
```
