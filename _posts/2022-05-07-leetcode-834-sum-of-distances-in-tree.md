--- 
layout      : single
title       : LeetCode 834. Sum of Distances in Tree
tags        : LeetCode Hard Tree Graph DP DFS 
---
[2246. longest path with different adjacent characters]({% post_url 2022-04-20-leetcode-2246-longest-path-with-different-adjacent-characters %})相似題，樹狀DP，但這題難上不少。

# 題目
輸入整數n和長度為n的二維陣列edges，代表一顆以0為根節點，共有n個節點的樹，以及每個節點的邊。  
回傳長度為n的陣列answers，answer[i]代表節點i到其他節點的距離總和。

# 解法
參考了[grandyang](https://www.cnblogs.com/grandyang/p/11520804.html)的文章才理解，我自己大概是想不通其中關係。  
![例圖](https://assets.leetcode.com/uploads/2021/07/23/lc-sumdist1.jpg)  
通過觀察發現，節點0的距離總和=所有子樹的(距離總和+節點數)。  
用圖片來舉例，節點0到節點[2,3,4,5]，至少需要從節點0前往節點2**重複4次**，再加上節點2前往其他子節點的總距離，以此遞迴關係可以從節點0往下dfs算出前往各節點的總距離。  

但是這樣只有節點0的答案是正確的：節點1沒有算到前往2子樹的總距離、節點2也沒算到0子樹的總距離，除了0以外的節點都少算一些，必須再dfs一次求得正確的答案。  
拿節點0的總距離8和節點2的總距離x來比較，會增加**節點2前往節點0重複2次**，並減少**節點0前往節點2重複4次**，x=8+2-4=6，得到節點2的正確答案。再以此正確答案繼續對子節點修正。  

```python
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        cnt=[1]*n # 子節點數量
        dis=[0]*n
        g=defaultdict(list)
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        
        
        def dfs(curr,prev):
            for adj in g[curr]:
                if adj!=prev:
                    dfs(adj,curr)
                    cnt[curr]+=cnt[adj]
                    dis[curr]+=dis[adj]+cnt[adj]
        
        def dfs2(curr,prev):
            for adj in g[curr]:
                if adj!=prev:
                    # n-cnt[adj]個節點 距離全部+1
                    # cnt[adj]個節點 距離全部-1
                    dis[adj]=dis[curr]+(n-cnt[adj])-cnt[adj]
                    dfs2(adj,curr)
        
        dfs(0,None)
        dfs2(0,None)
        
        return dis
```
