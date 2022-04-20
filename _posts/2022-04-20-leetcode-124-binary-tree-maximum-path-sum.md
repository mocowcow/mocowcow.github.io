---
layout      : single
title       : LeetCode 124. Binary Tree Maximum Path Sum
tags 		: LeetCode Hard BinaryTree DFS DP
---
打鐵趁熱，把以前寫過的樹狀DP也複習幾次。

# 題目
輸入一棵二元樹，求此樹的最大**非空**路徑和。  
二元樹的路徑是節點序列，其中每個相鄰節點都有一條連接的邊，一個節點最多只能在序列中出現一次，且此路徑不必通過根。  

# 解法
題目要求的非空路徑和，代表路徑序列最少得包含一個節點。  

定義dfs(i)：從i出發往下走，可以得到的最大**非空**路徑和。  
試著以i為中心組成更大的路徑和，但是因為以左右子節點構成的**非空**子路徑有可能為負值，需要手動選擇要不要接上這些子路徑，之後更新答案。  
而由i所組成的子路徑，是由節點i加上左右其中一條為正值的子路徑所組成。

```python
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans=root.val
        
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            l = max(0,dfs(node.left)) 
            r = max(0,dfs(node.right))
            ans=max(ans,l+r+node.val)
            return node.val+max(l,r)
        
        dfs(root)
        
        return ans
```

稍微修改一下dfs(i)的定義，變成從i出發往下走，可以得到的最大**可以為空**路徑和，就可以連i點都不要的意思。  
這樣求左右子路徑的時候就不會出現負值，所以由i為中心組成的路徑可以直接拿i點加上左右的dfs結果，最壞的情況也就是路徑和不變而已。  
回傳時多和0取最大值，避免出現負數的路徑和。

```python
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans=root.val
        
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            ans=max(ans,l+r+node.val)
            return max(0,node.val+max(l,r))
        
        dfs(root)
        
        return ans
```

