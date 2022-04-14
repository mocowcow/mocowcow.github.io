---
layout      : single
title       : LeetCode 222. Count Complete Tree Nodes
tags 		: LeetCode Medium BinaryTree DFS 
---
某人的面試題，今天想到做來玩玩。

# 題目
輸入一棵complete(完整)二元樹，計算出節點數量。  
complete binary tree指的是除最後一層以外，各層的節點都是滿的，且最後一層的節點都靠左方。  
設計一個時間複雜度小於O(N)的演算法。

# 解法
題目要求小於O(N)，基本上就是不要普通的遍歷了，不過還是姑且做一次。

```python
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1+self.countNodes(root.left)+self.countNodes(root.right)
```

比較多人使用的方法是：  
從root開始，找最左方和最右方的子節點，如果層數相同代表這棵樹是perfect(完美)的，可以直接以公式算出節點數為(2^層數)-1。  
否則分別遞迴處理左右子樹。  

```python
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # get left height
        lh=rh=0
        l=root
        while l:
            lh+=1
            l=l.left
            
        # get right height
        r=root
        while r:
            rh+=1
            r=r.right
            
        # check if perfect
        if lh==rh:
            return (2**lh)-1
        else:
            return 1+self.countNodes(root.left)+self.countNodes(root.right)
```

還有一種比較神奇但是可讀性差的寫法：  
一樣找最左最右子節點，但是判斷條件改成右節點不為空。因為complete tree保證節點一定先出現在左方，可以確定若有右方能走，則左方一定能走。  
如果此樹為prefect，則左右都會停在空節點上；否則左節點不為空，需要遞迴求解。  

```python
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        l=root.left
        r=root.right
        depth=1
        while r:
            depth+=1
            l=l.left
            r=r.right
            
        # check if perfect
        if l==r: # both are null 
            return (2**depth)-1
        else:
            return 1+self.countNodes(root.left)+self.countNodes(root.right)
```