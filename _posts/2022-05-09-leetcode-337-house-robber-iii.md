--- 
layout      : single
title       : LeetCode 337. House Robber III
tags        : LeetCode Medium BinaryTree DP DFS
---
複習經典的樹狀DP。今天才知道house robber系列有個飽含詩意的中文名：**打家劫舍**。

# 題目
小偷又來行竊了，這次只有一個入口：root。  
除了root以外，每間屋子都只有一個**父房屋**。小偷逛了一圈，發現這些房子剛好形成一棵二元樹。和之前一樣，只要有兩間相鄰的房屋在同一天被竊，警報器就會響起。  
輸入二元樹的root，求小偷不被發現的情況下，能夠得到的最大金額。

# 解法
響起以前初見這題時苦惱好久，那時只知道偷和不偷，但想不出怎麼計算最大利潤。  

其實不用想太複雜，一樣也是選擇要不要偷當前房屋：  
1. 偷，左右子房屋不能偷，但是**子房屋的子房屋可以偷**  
2. 不偷，但是偷左右子房屋  

只是要考慮到子房屋為空的時候，根本沒有子子房屋，需要加上if來判斷。  
這種方法重複計算到同樣位置好幾次，需要對dfs做快取，否則會TLE。

```python
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        @lru_cache(None)
        def dfs(node):
            if not node:
                return 0
            notake=dfs(node.left)+dfs(node.right)
            take=node.val
            if node.left:
                take+=dfs(node.left.left)+dfs(node.left.right)
            if node.right:
                take+=dfs(node.right.left)+dfs(node.right.right)
            return max(take,notake)

        return dfs(root)
```

把dfs的回傳值修改，變成同時回傳**偷**和**不偷**的結果，複雜度降至O(N)。  
也因為回傳值變成兩個，所以對root呼叫dfs完之後要記得取最大值。

```python
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return [0,0] # take, no take
            l=dfs(node.left)
            r=dfs(node.right)
            notake=max(l)+max(r)
            take=node.val+l[1]+r[1] # cant take child if take this
            return [take,notake]

        return max(dfs(root))
```