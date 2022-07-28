--- 
layout      : single
title       : LeetCode 437. Path Sum III
tags        : LeetCode Medium DFS PrefixSum BinaryTree HashTable
---
每日題。滿好玩的一題，至少有三種解法，但我沒想到最佳解。  

# 題目
輸入二元樹的根節點root和整數targetSum，求有多少路徑其節點值總和等於targetSum。  
路徑不需要從根節點或葉節點開始或結束，但只能從父節點往子節點移動。  

# 解法
測資範圍不大，最多只有1000個節點，那麼O(N^2)解法一定可行。  

撰寫dfs函數，從root往下遞迴，列舉每個節點node為起點，分別計算產生多少路徑總和為targetSum。  
若碰到空節點，沒有合法路徑，回傳空list；否則先求出左右子節點所有的路徑，並分別對總和加上當前的節點值，還有一個只包含當前節的新路徑。  
這時以node為起點的路徑已經全部列舉完，計算裡面有多少總和targetSum，更新至答案中。  

```python
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans=0
        
        def dfs(node):
            nonlocal ans
            if not node:
                return []
            path=[0]+dfs(node.left)+dfs(node.right)
            path=[x+node.val for x in path]
            ans+=path.count(targetSum)
            return path
            
        dfs(root)
        
        return ans
```

可能有很多條路徑會得到同樣的路徑總和，將list改為雜湊表理論上可以節省一些時間，但是整體複雜度還是O(N^2)。  
結果執行時間不如預期，反而比上面的方法還慢，

    
```python
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans=0
        
        def dfs(node):
            nonlocal ans
            d=defaultdict(int)
            if not node:
                return d
            l=dfs(node.left)
            r=dfs(node.right)
            d[node.val]+=1
            for k,v in l.items():
                d[k+node.val]+=v
            for k,v in r.items():
                d[k+node.val]+=v
            ans+=d[targetSum]
            return d
            
        dfs(root)
        
        return ans
```

最佳解其實只需要O(N)，有點類似[1074. number of submatrices that sum to target]({% post_url 2022-07-18-leetcode-1074-number-of-submatrices-that-sum-to-target %})的概念。  

和原本O(N^2)的解法不太一樣，現在改成列舉從root出發、以所有節點node結尾的所有路徑，而路徑總和為pathSum。這有點像是在樹上做前綴和，以當前路徑扣掉先前出現過的路徑，產生符合目標的子路徑。  

假設有三個節點連成一直線，其值分別為[2,3,4]，targetSum=4：  
> curr=2, pathSum=2  
> curr=3, pathSum=5  
> curr=4, pathSum=9  
> [2,3,4]扣掉[2,3]這段，剩下[4]符合targetSum=4  

有幾個需要注意的點：  
- 就像普通的前綴和需要多儲存一格空陣列一樣，需要初始化長度為0的路徑和，這樣碰到路徑和等於targetSum才有辦法更新答案  
- 遞迴離開時要把路徑計樹回溯掉，否則會誤用先前計算過的結果  

PS
```python
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans=0
        d=defaultdict(int)
        d[0]=1 # empty path
        
        def dfs(node,pathSum):
            nonlocal ans
            if not node:
                return 
            pathSum+=node.val
            ans+=d[pathSum-targetSum]
            d[pathSum]+=1
            dfs(node.left,pathSum)
            dfs(node.right,pathSum)
            d[pathSum]-=1 # backtracking
            
        dfs(root,0)
        
        return ans
```
