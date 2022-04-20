---
layout      : single
title       : LeetCode 2246. Longest Path With Different Adjacent Characters
tags 		: LeetCode Hard Tree Graph DFS DP
---  
周賽289。被Q3卡死，根本沒時間看Q4，結果這題還不算太難。  

# 題目
有一棵樹(無環無向圖)共有n個節點從0編號到n-1，根節點為0。  
陣列parent代表各節點的父節點，如parent[1]表示節點1的父節點，而0是根節點，所以parent[0]永遠為-1。  
字串s代表各節點的值，如s[0]代表節點0的值。  

求**沒有任何相鄰節點擁有相同值**所組成最長路徑長度。

# 解法
一個有效路徑必須只能是一條直線，不能有任何分岔。  
假設根節點0擁有三個子節點[1,2,3]，且s='abcd'，你只能從[1,2,3]中選擇一個點，通過0再前往另一個點，最長路徑是3。  

參考了[大老的解法](https://leetcode-cn.com/problems/longest-path-with-different-adjacent-characters/solution/by-endlesscheng-92fw/)，稍微修改成自己比較能接受的版本。從根節點0開始top down，原來這種方法叫做樹狀DP。  

個人將題目理解為：對每一個節點i，找兩個子節點from和to，從某個地方經過from抵達i，再經過to後跑到某處去，路上所能經過最多的節點是幾個。當然from和to也可以不存在。

定義dp(i)為：以i為出發點，通過子節點j可構成路徑中的最長長度。過程中，順便以節點i為中心，找出所有子節點中所能形成的最長路徑，並和兩個**最長且不同值子節點**from和to更新答案。
轉移方程式：dp(i)=1+max(dp(j) FOR ALL j屬於i的子節點)。  
當某個節點沒有子節點時為base case，會直接回傳1。  

```python
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        ans=1
        child=defaultdict(list)
        for i in range(1,len(parent)):
            child[parent[i]].append(i) 
        
        @lru_cache(None)
        def dp(i):
            nonlocal ans
            fromPath=0 # 當前最長合法子路徑
            for j in child[i]:
                toPath=dp(j) # 子節點j產生的合法子路徑to
                if s[i]!=s[j]:
                    ans=max(ans,fromPath+toPath+1) # 用from和to串起來，看能不能刷新ans
                    fromPath=max(fromPath,toPath) # 更新當前最長子路徑
            return fromPath+1
        
        dp(0)
        
        return ans
```

寫完才覺得上面邊計算、邊更新最長子路徑有點難懂，稍微修改一下，不過速度確實慢了些。  

```python
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        ans=1
        child=defaultdict(list)
        for i in range(1,len(parent)):
            child[parent[i]].append(i) 
        
        @lru_cache(None)
        def dp(i):
            nonlocal ans
            subs=[]
            for j in child[i]:
                sub=dp(j)
                if s[i]!=s[j]:
                    subs.append(sub)
            longest2=nlargest(2,subs)
            ans=max(ans,sum(longest2)+1)
            if longest2: # concat longest subpath
                return longest2[0]+1 
            else: # base case
                return 1
            
        dp(0)
        
        return ans
```
