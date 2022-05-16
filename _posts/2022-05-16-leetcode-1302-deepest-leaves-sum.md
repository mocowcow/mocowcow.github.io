--- 
layout      : single
title       : LeetCode 1302. Deepest Leaves Sum
tags        : LeetCode Medium BinaryTree DFS
---
昨天的每日題，周賽完太累來不及寫題解，今天才補上。

# 題目
輸入二元樹的根，返回最深葉節點值總和。

# 解法
最直覺的方法就是dfs直接計算每層的總和，回傳最深那層的總和值就好。

```python
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        val=defaultdict(int)
        
        def dfs(node,d):
            if not node:
                return 
            val[d]+=node.val
            dfs(node.left,d+1)
            dfs(node.right,d+1)
        
        dfs(root,0)
        
        return val[max(val.keys())]
```

上面的方法多了好幾次運算，也浪費空間，試著只維護最底層的節點總和。  
dfs時，只有沒有子節點的情況下，才試著計算總和：若當前層數d超過最深層數deep，則更新deep；若剛好是最深層，則加入當前節點值；否則不動作。

```python
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        deep=0
        ans=0
        
        def dfs(node,d):
            nonlocal ans,deep
            if not node:
                return 
            if node.left==node.right==None:
                if d>deep:
                    deep=d
                    ans=node.val
                elif d==deep:
                    ans+=node.val
            else:
                dfs(node.left,d+1)
                dfs(node.right,d+1)
            
        dfs(root,0)
        
        return ans
```
