--- 
layout      : single
title       : LeetCode 2641. Cousins in Binary Tree II
tags        : LeetCode Medium BinaryTree DFS HashTable
---
雙周賽102。

# 題目
輸入二元樹的根節點root，將樹中所有節點的值替換成所有**堂兄弟節點值的總和**。  

若某兩個節點的深度相同，但父節點不同，則稱為**堂兄弟**。  

回傳修改過後的root。  

# 解法
如果說同深度不同父叫做**堂兄弟**，那麼同深度且同父是不是**親兄弟**？  
那麼深度中所有節點，扣掉親兄弟，在扣掉自己，剩下就全是堂兄弟了。  

先一次dfs，依照深度計算各層節點值總和，順便以各**節點的父親**將節點分組。  
再來第二次dfs，將節點值更新為**深度節點值總和**扣掉**父節點的所有兒子(包含自己和親兄弟)**。  

時間複雜度O(N)。空間複雜度O(N)。  

```python
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        depth_sum=Counter()
        same_father=Counter()
        
        def dfs(o,fa,d):
            if not o:
                return
            depth_sum[d]+=o.val
            same_father[fa]+=o.val
            dfs(o.left,o,d+1)
            dfs(o.right,o,d+1)
            
        dfs(root,None,0)
        
        def dfs2(o,fa,d):
            if not o:
                return
            o.val=depth_sum[d]-same_father[fa]
            dfs2(o.left,o,d+1)
            dfs2(o.right,o,d+1)
            
        dfs2(root,None,0)
        
        return root
```
