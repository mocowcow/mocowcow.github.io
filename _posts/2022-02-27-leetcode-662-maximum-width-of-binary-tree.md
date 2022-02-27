---
layout      : single
title       : LeetCode 662. Maximum Width of Binary Tree
tags 		: LeetCode Medium BinaryTree DFS BFS
---
每日題。周賽最後一題卡好久，花70分鐘還寫不出來，差點沒吐血。

# 題目
輸入節點root表示一顆二元樹的根節點，求這棵樹的最大寬度。  
寬度的定義是同一深度的節點，最右邊和最左邊的節點的距離，中間若有空節點也要列入計算。

# 解法
其實我覺得題目描述有點怪怪的。
像是例題root = [1,3,2,5,3,null,9]：  
> 第一層 [1]  寬度1  
> 第二層 [3,2]  寬度2  
> 第三層 [5,3,null,9]  寬度4  

若第三層改為[5,3,9]的話則寬度變成3，與其說兩端之間的距離，不如說是最左到最右這範圍可以塞下幾顆節點？  

使用DFS先把所有節點依層數分類，並以編號表示節點位置，根為1，左節點為父節點編號\*2，右邊為父節點編號\*2+1，以此類推。preorder traversal可以保證每一層中一定是左方節點先出現。  
之後對每一層算寬度，最後一個節點編號-第一個節點編號+1就是當層寬度。回傳最大的寬度就是答案。
例題root = [1,3,2,5,3,null,9] 經過編號後：  
> [1] 第一層寬度(1-1)+1 = 1  
> [2,3] 第二層寬度(3-2)+1 = 2  
> [4,5,7] 第三層寬度(7-4)+1 = 4  
> (第三層6號位是空節點，不影響計算)   

```python
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        lvl = defaultdict(list)

        def dfs(node, idx, d):
            if not node:
                return
            lvl[d].append(idx)
            dfs(node.left, idx*2, d+1)
            dfs(node.right, idx*2+1, d+1)

        dfs(root, 1, 0)

        return max(d[-1]-d[0] for d in lvl.values())+1

```
