--- 
layout      : single
title       : LeetCode 2673. Make Costs of Paths Equal in a Binary Tree
tags        : LeetCode Medium Array Tree BinaryTree DFS Greedy
---
周賽344。老實說我覺得這輸入有點整人，說節點從1開始算，但是對應的值卻是0開始算，兩者統一不是更好。  

# 題目
輸入整數n，代表一顆有n個節點的prefect binary tree，節點編號分別為1\~n。  
根節點編號為1，對於每個節點i，左子節點的編號為2\*1，右子節點編號為i\*2+1。  

每個節點都有一個成本，由整數長度n的陣列cost表示。其中cost[i]代表節點編號i+1的成本。  
你可以將**任意**節點的成本增加1**任意**次。  

求使得從根節點到所有**葉節點**的路徑成本相同，**最少**需要增加成本幾次。  

# 解法
一開始想錯方向，以為把每層的節點都改到跟最大的一樣就行，但碰到以下例子就會發現完全不對：  
![示意圖](/assets/img/2673-1.jpg)  
每條路徑都是[1,3,2]或[1,2,3]，根本不用改就相同。  

後來想想，正確應是使每條路徑等於**成本最大的路徑**。  
如果我們從上往下找，並不知道子節點會出現什麼值，更不用說判斷成本相不相同。所以先dfs遍歷一次，找出最大的路徑。  
![示意圖](/assets/img/2673-2.jpg)  
如圖，最大的路徑應為13，必須將其他路徑修改數次，使之變成13。  
但如果兩條路徑擁有共通的父節點，那麼在父節點上修改，只需要**一半的修改次數**。  
![示意圖](/assets/img/2673-3.jpg)  
因此維護陣列inc，透過後序dfs求出各節點所需的修改次數inc[i]。  
若當前節點i為葉節點，則修改次數inc[i]為mx-sm；否則為左右節點提出的共通值mn，並將左右扣掉mn。  

最後回傳inc的加總就是答案。  
順帶一提，根節點inc[1]永遠會是0。若不為0的狀況下，代表左右節點有共通的提取值，代表有冗於的修改次數，必定不是最佳答案。  

時間複雜度O(n)。  
空間複雜度O(n)。  

```python
class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        cost=[0]+cost
        inc=[0]*(n+1)
        mx=0
        
        def dfs(i,sm):
            nonlocal mx
            l=i*2
            r=i*2+1
            sm+=cost[i]
            if l<=n:
                dfs(l,sm)
                dfs(r,sm)
            else: # leaf
                mx=max(mx,sm)
                
        dfs(1,0)
        
        def dfs2(i,sm):
            l=i*2
            r=i*2+1
            sm+=cost[i]
            if l<=n:
                dfs2(l,sm)
                dfs2(r,sm)
                mn=min(inc[l],inc[r])
                inc[i]=mn
                inc[l]-=mn
                inc[r]-=mn
            else: # leaf
                inc[i]=mx-sm
        
        dfs2(1,0)
        
        return sum(inc)
```
