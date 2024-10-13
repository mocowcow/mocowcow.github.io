---
layout      : single
title       : LeetCode 3319. K-th Largest Perfect Subtree Size in Binary Tree
tags        : LeetCode Medium Tree DFS Sorting
---
weekly contest 419。  

## 題目

輸入二元樹的根節點以及整數 k。  

求第 k 大的**完美二元子樹**的大小，若不存在則回傳 -1。  

完美二元樹指的是所有葉節點高度都相同，且父節點都有兩個子節點。  

## 解法

若某樹是完美的，其左右左右子樹必定也是完美的，而且節點數相同。
具有相同子問題，可以用遞迴解決。  

若其中一個子樹不完美，則之後就不可能完美。  
除了要記錄節點數之外，還需要一個參數表示**是否完美**。  
此處使用節點數 -1 代表不完美，反正只要不完美，有幾個節點就不重要了。  

時間複雜度 O(N log N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        a = []

        def dfs(o):
            if not o:
                return 0
            left = dfs(o.left)
            right = dfs(o.right)
            if left >= 0 and left == right:
                sz = left + right + 1
                a.append(sz)
                return sz
            return -1

        dfs(root)
        if len(a) >= k:
            a.sort()
            return a[-k]

        return -1
```
