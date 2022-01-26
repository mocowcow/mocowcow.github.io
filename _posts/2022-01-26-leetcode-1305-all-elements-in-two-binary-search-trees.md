---
layout      : single
title       : LeetCode 1305. All Elements in Two Binary Search Trees
tags 		: LeetCode Medium DFS BinaryTree Sorting 
---
看討論區才知道原來python內建使用timsort，長知識了。

# 題目
輸入兩個binary search tree，返回一個包含所有元素的整數陣列，並以遞增排序。

# 解法
分別對兩棵樹做中序DFS，合併即可。

```python
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def dfs(node, q):
            if not node:
                return
            dfs(node.left,q)
            q.append(node.val)
            dfs(node.right,q)

        q1 = deque()
        q2 = deque()
        dfs(root1, q1)
        dfs(root2, q2)
        ans = []
        while q1 and q2:
            if q1[0] < q2[0]:
                ans.append(q1.popleft())
            else:
                ans.append(q2.popleft())
        if q1:
            ans += q1
        elif q2:
            ans += q2

        return ans
```

另一個解法是把兩棵樹塞進陣列使用sort函數，強大的[timsort](https://zh.wikipedia.org/wiki/Timsort)會把複雜度壓到O(N)。

```python
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def dfs(node, a):
            if not node:
                return
            dfs(node.left,a)
            q.append(node.val)
            dfs(node.right,a)
        val = []
        dfs(root1,a)
        dfs(root2,a)
        return sorted(val)
```