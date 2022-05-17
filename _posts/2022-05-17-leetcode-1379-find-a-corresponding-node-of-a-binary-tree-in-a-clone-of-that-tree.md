--- 
layout      : single
title       : LeetCode 1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree
tags        : LeetCode Medium BinaryTree DFS
---
每日題。如果不管follow up，那真的是有點無意義的題目。但應該沒有到需要按爛的程度吧，竟然有1300個爛。

# 題目
輸入兩棵一模一樣的二元樹original和cloned，還有一個屬於original節點target。  
在不做任何修改的情況下，回傳在cloned中對應到target的節點。  
節點保證不會出現重複值。

Follow up:如果節點值會重複，你有辦法解決嗎?

# 解法
我看到follow up才發現：題目一開始強調值不會重複，該不會設想要大家用節點值去判斷？  
完全無視original樹，直接在cloned裡面找到跟target同值的節點回傳就好。

```python
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def dfs(node):
            if not node:
                return
            if node.val==target.val:
                return node
            return dfs(node.left) or dfs(node.right)
        
        return dfs(cloned)
```

剛好我一開始想到的解法就可以處理follow up中出現重複節點值的情形：以節點的記憶體比對。  
dfs函數改成同時遍歷兩棵樹，但是只以original樹中的節點和target做比對，如果找到就回傳cloned樹的當前節點；找不到則繼續往下dfs，題目保證總會找到的。

```python
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def dfs(n1,n2):
            if not n1:
                return 
            if n1==target:
                return n2
            return dfs(n1.left,n2.left) or dfs(n1.right,n2.right)
                
        return dfs(original,cloned)
```
