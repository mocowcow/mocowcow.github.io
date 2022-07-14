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

上述方法是切割子陣列，每次切割區要O(N)，如果N測資太大的話效率不佳，可以改成以雙指針表示子陣列範圍。  
而且每個元素也只會出現一次，可以把索引值先裝進雜湊表，每次取值只要O(1)。  

```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        N=len(preorder)
        d={n:i for i,n in enumerate(inorder)}
        
        def f(l1,r1,l2,r2):
            if l1>r1 or l2>r2:
                return None
            val=preorder[l1]
            node=TreeNode(val)
            idx=d[val]
            leftcnt=idx-l2
            node.left=f(l1+1,l1+leftcnt,l2,idx-1)
            node.right=f(l1+leftcnt+1,r1,idx+1,r2)
            return node
            
        return f(0,N-1,0,N-1)
```