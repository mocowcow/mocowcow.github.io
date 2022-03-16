---
layout      : single
title       : LeetCode 1367. Linked List in Binary Tree
tags 		: LeetCode Medium LinkedList BinaryTree DFS 
---
學習計畫中的一題。以前也吃了4次WA才過，但一次可以練習到tree+list+recursion，算是優質營養大補包。

# 題目
輸入一linked list的首節點head以及一樹的根節點root，求此linked list能否完整的在樹中任一地方出現。  
> Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]  

![示意圖](https://assets.leetcode.com/uploads/2020/02/12/sample_1_1720.png)

# 解法
首先過濾edge cases：傳入空head一定是true，空root一定是false。  
寫一個findList函數，用來遞迴比對list node以及tree node。  

但是因為list不一定是從root開始就出現，也有可能是在左右子樹中才開始，所以只要以下其一為真就可以：  
1. 從root開始找到整個head  
2. 在root左子樹有找到head  
3. 在root右子樹有找到head  

最後是findList(listNode,treeNode)的細節，list為空代表整個都找到了，回傳true；或是list不為空但tree為空，沒法再找了，回傳false。兩節點值不同，比對失敗也是false。遞迴在左右子樹中找list的下個節點即可。  

```python
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not head:
            return True
        if not root:
            return False
        
        def findList(listNode, tree):
            # entire list found
            if not listNode:
                return True
            # end of tree
            if not treeNode:
                return False
            if treeNode.val!=listNode.val:
                return False
            # find next node
            return findList(listNode.next,treeNode.left) or findList(listNode.next,treeNode.right)
        
        
        return findList(head,root) or self.isSubPath(head,root.left) or self.isSubPath(head,root.right)
```

