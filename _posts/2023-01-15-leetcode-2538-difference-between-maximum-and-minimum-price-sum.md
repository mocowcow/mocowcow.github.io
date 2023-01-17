--- 
layout      : single
title       : LeetCode 2538. Difference Between Maximum and Minimum Price Sum
tags        : LeetCode Medium Array Graph Tree DFS DP sorting
---
周賽328。剩下7分鐘好不容易想通，但沒來得及把分類討論寫完。連續三次周賽沒過Q4，好慘。  

# 題目
有個無向圖，共有n個節點，編號分別為0\~n-1。輸入二維整數陣列edges，其中edges[i] = [a<sub>i</sub>, b<sub>i</sub>]，代表a<sub>i</sub>和b<sub>i</sub>之間有一條邊。  

每個節點都有一個對應的**價格**。輸入整數陣列price，其中price[i]代表第i個節點的價格。  

定義**總價格**為一條路徑上所有節點的價格總和。  

你可以選擇任意節點作為根節點root，使圖成為一棵樹。選擇root作為根的的**成本**是以root為起點的所有路徑中，**總價格**最大的一條路徑和最小的一條路徑的差值。  

求所有可能的根節點中，**最大成本**為多少。  

# 解法
我第一個想到的就是[124. binary tree maximum path sum]({% post_url 2022-04-20-leetcode-124-binary-tree-maximum-path-sum %})。  

查看測資，發現節點價格至少為1，不會出現負值，所以有子節點的話一定要選。  

定義dfs為以某節點為子樹時，包含葉節點的總價格，以及扣除葉節點的總價格。  
任選一節點i作為root開始dfs，對於每棵子樹找出要連接的子節點，有以下幾種情況：  
1. 沒有子節點，最大=最小，成本為0  
2. 只有一個子節點，可以選擇扣掉當前節點i，或是扣掉葉節點  
3. 含、不含葉節點的最大路徑都**來自同一棵子樹**。節點i可以搭配最大含葉節點+次大不含葉節點，或是次大含葉節點+最大不含葉節點  
4. 含、不含葉節點的最大路徑**來自不同子樹**，直接取兩者的最大路徑搭配節點i  

若N-1個節點全部連接在某個中心時，排序會是時間瓶頸，時間複雜度O(N log N)。空間複雜度O(N)。  

```python
class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        ans=0
        g=defaultdict(list)
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
            
        def dfs(i,fa): # return [max path sum include leaf, max path sum exclude leaf]
            nonlocal ans
            leaf=[] # include leaf
            noleaf=[] # exclude leaf
            p=price[i]
            
            for j in g[i]:
                if j==fa:continue
                t=dfs(j,i)
                leaf.append([t[0],j])
                noleaf.append([t[1],j])
                
            if len(leaf)==0:
                return [p,0]
            
            leaf.sort(reverse=True)
            noleaf.sort(reverse=True)
            
            if len(leaf)==1:
                ans=max(ans,
                        leaf[0][0],
                        noleaf[0][0]+p
                       )
            elif leaf[0][1]==noleaf[0][1]:
                ans=max(ans,
                        leaf[0][0]+noleaf[1][0]+p,
                        leaf[1][0]+noleaf[0][0]+p
                       )
            else:
                ans=max(ans,leaf[0][0]+noleaf[0][0]+p)
            
            return [leaf[0][0]+p,noleaf[0][0]+p]
        
        dfs(0,-1)
            
        return ans
```
