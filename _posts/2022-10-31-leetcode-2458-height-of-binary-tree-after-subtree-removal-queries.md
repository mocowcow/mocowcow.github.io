--- 
layout      : single
title       : LeetCode 2458. Height of Binary Tree After Subtree Removal Queries
tags        : LeetCode Hard Array BinaryTree HashTable SortedList DFS
---
周賽317。比賽中沒想出怎麼做，後來看了大神O(N)也不懂，暫時只能做出次佳解。  

# 題目
輸入有n個節點的二元樹的根root，各節點編號為分別為1~\n。還有一個大小為m的陣列queries。  
你必須在樹上執行m次**獨立的查詢**，在第i次查詢中執行以下操作：  
- 從樹中刪除以值為queries[i]的節點為根的子樹。保證query[i]不會等於root的值。  

回傳一個大小為m的陣列answer，其中answer[i]是執行第i次查詢後樹的高度。  

注意：
- 每次查詢是獨立的，因此在每次查詢後，樹會返回初始狀態  
- 樹的高度定義為**根節點至葉節點**的**最長路徑中的邊數**  

# 解法
baker大神的[圖解](https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/discuss/2757990/Python-3-Explanation-with-pictures-DFS)強的不行，光看圖就知道做法，連程式碼都不必看。  

簡而言之就是：要刪掉的節點q位於第lvl層，查看同一層除了q之外的節點最多可以往下走幾次(也就是邊數)。  
而位於第lvl層，也就是從root向下走lvl次的意思，所以刪除後的root的高度就是lvl+以同層節點為子樹的最大高度；若該層只有一顆節點，則刪除後無法抵達此層，所以高度變成lvl-1。  

講起來很簡單，做起來還真有點麻煩。  
我們需要三個雜湊表來記錄：  
- 各節點位於第幾層  
- 以各節點為根的子樹**最大高度**  
- 各層子樹的**最大高度**  

先以dfs求出上述各值，每次查詢時求出刪除節點q的層數，刪除相應子樹高度後將root高度加入答案後，再把剛才刪掉的加回去。  

總共M次查詢，每次查詢需要刪除又加回高度，為O(log N)。雖然不可能N個節點都擠在同一層，不過時間複雜度還是表示為O(M log N)。每個節點都要紀錄子樹高度和層數，空間複雜度O(N)。  

```python
from sortedcontainers import SortedList

class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        node_lvl=defaultdict(int)
        node_height=defaultdict(int)
        lvl_heights=defaultdict(SortedList)
        
        def dfs(node,lvl):
            if not node:
                return 0
            node_lvl[node.val]=lvl
            height=max(dfs(node.left,lvl+1),dfs(node.right,lvl+1))
            lvl_heights[lvl].add(height)
            node_height[node.val]=height
            return height+1
        
        dfs(root,0)
        
        ans=[]
        for q in queries:
            lvl=node_lvl[q]
            if len(lvl_heights[lvl])==1:
                ans.append(lvl-1)
            else:
                height=node_height[q]
                lvl_heights[lvl].remove(height)
                ans.append(lvl_heights[lvl][-1]+lvl)
                lvl_heights[lvl].add(height)
            
        return ans
```

後來總算搞懂[兩次dfs預處理](https://leetcode.cn/problems/height-of-binary-tree-after-subtree-removal-queries/solution/liang-bian-dfspythonjavacgo-by-endlessch-vvs4/)的的寫法。  

只看文字和程式碼搞得很抽象，完全不知道在幹什麼，怎麼可能用O(1)時間來查詢？自己畫了圖才恍然大悟。  
第一次dfs和之前一樣，計算以各節點為子樹的最大高度。第二次dfs，用來計算刪除當前node後，剩餘的最大高度，其參數有d和thoer，d指的是層數，也就是從root到達此節點的邊數；重點在於這個other。  
假設你在節點node，不包含node的最大高度為other，當繼續dfs處理node子節點的時候，當然不會使other減少。假設要刪除的是左節點，那麽右子樹有可能比other更大，兩者取max；同理，刪除右節點，左子樹可能更高，以other和左子樹高度取max。  

兩次dfs為O(N)，查詢為O(M)，時間複雜度O(N+M)。空間複雜度O(N)。  

```python
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        heights=defaultdict(int)
        rest=defaultdict(int)
        
        def dfs1(node):
            if not node:
                return 0
            heights[node]=1+max(dfs1(node.left),dfs1(node.right))
            return heights[node]
        
        dfs1(root)
        
        def dfs2(node,d,other):
            if not node:
                return 
            rest[node.val]=other
            dfs2(node.left,d+1,max(other,d+heights[node.right]))
            dfs2(node.right,d+1,max(other,d+heights[node.left]))
        
        dfs2(root,0,0)
        
        return [rest[q] for q in queries]
```