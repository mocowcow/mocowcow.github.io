--- 
layout      : single
title       : LeetCode 968. Binary Tree Cameras
tags        : LeetCode Hard Tree BinaryTree DFS Greedy
---
每日題。本以為是樹型DP，結果也可以不用DP。  

# 題目
輸入二元樹的root。我們要在節點上安裝監視器，節點上的每個監視器都可以監控其父節點、自身及其相鄰子節點。  
回傳監視整棵樹的所有節點**最少**需要幾台監視器。

# 解法
每個節點只有三種狀態：  
- 沒有被監視，標記為0  
- 父節點或左右子節點有監視器，標記為1  
- 本身裝了監視器，標記為2  

基於貪心思想，從最底層的節點開始往上設置監視器，能放在越高處越好。  
從root開始做後序dfs，而碰到空節點也視為狀態1，才不會影響判斷。  

對於每個節點node，若左節點或右節點沒有被監視到，代表node必須裝上監視器，所以答案+1並回傳狀態2。  
那如果左節點或右節點都被監視到了，而且其中至少一個有裝監視器，代表node也可以被覆蓋到，直接回傳狀態1。  
剩下情況只有左右節點都有被監視到，但是沒監視器，當前節點沒被監視到，回傳0，交給其父節點處理。  

最後要另外判斷root的狀態，若root狀態為0，則必須多裝一個監視器，才能覆蓋到root。  

```python
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        # 0 = uncovered
        # 1 = covered 
        # 2 = has camera
        ans=0
        
        def dfs(node):
            nonlocal ans
            if not node:
                return 1
            l=dfs(node.left)
            r=dfs(node.right)
            if l==0 or r==0:
                ans+=1
                return 2
            if l+r>=3:
                return 1
            return 0
        

        if dfs(root)==0:
            return ans+1
        
        return ans
```
