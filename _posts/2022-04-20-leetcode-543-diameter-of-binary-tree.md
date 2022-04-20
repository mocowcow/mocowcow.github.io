---
layout      : single
title       : LeetCode 543. Diameter of Binary Tree
tags 		: LeetCode Easy BinaryTree DFS
---
和[2246. Longest Path With Different Adjacent Characters]({% post_url 2022-04-20-leetcode-2246-longest-path-with-different-adjacent-characters %})差不多的道理，只是這題只有兩個子節點。

# 題目
輸入一棵二元樹，求此樹的直徑。  
二元樹的直徑是樹中任意兩個節點之間最長路徑的長度，且此路徑可能不會通過根。兩個節點之間的長度為他們之間的**邊**數。

# 解法
直徑長度=邊數量=路徑節點數量-1。  
先求出最長直徑最多有幾個節點ans，再把ans-1就是答案。  

dfs(i)函數求的是以節點i出發，可以構成的最大路徑長度。  
試著以i為中心點，從左子樹通過i後前往右子樹，檢查是否能更新直徑。最後選擇左右子路徑中較大者，加上節點i組成新的子路徑。

```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans=0
        
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            l=dfs(node.left)
            r=dfs(node.right)
            ans=max(ans,l+r+1) # left+node=right
            return max(l,r)+1
        
        dfs(root)
        
        return ans-1
```

