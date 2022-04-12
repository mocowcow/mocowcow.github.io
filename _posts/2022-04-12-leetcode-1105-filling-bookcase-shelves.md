---
layout      : single
title       : LeetCode 1105. Filling Bookcase Shelves
tags 		: LeetCode Medium DP Array
---
好一陣子沒DP，找一題來玩玩。

# 題目
books陣列代表每本書的寬度及高度，而shelfWidth代表書櫃的寬度。你必須依照books的出現順序將所有書塞入書櫃。  
你可以選擇在任何時候加上一片隔板，建立新的平台在下方書籍的最高點上，繼續塞入剩下的書籍。求塞完所有書後，所堆積到的最小高度為多少。

# 解法
例題展示了有些時候塞滿每層並不是最佳解法，適時的換層也許會更好，那一定是DP了。  
定義dp(i)為塞完第i本書的最低高度。  
轉移方程式：dp(i)=min(這層n本書的最高高度+塞完第i-n本書的最低高度)，n取決於每本書的寬度總和不超過shelfWidth。  
i<0為base case，因為不存在第-1本書，所以回傳高度0。  
回傳dp[N-1]就是答案。

```python
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        
        @lru_cache(None)
        def dp(i):
            if i<0:
                return 0
            best=math.inf
            h=0
            j=i
            w=shelfWidth
            while j>=0 and w>=books[j][0]:
                w-=books[j][0]
                h=max(h,books[j][1])   
                j-=1
                best=min(best,h+dp(j))
            return best
        
        return dp(len(books)-1)
```

改成bottom up版本。  

```python
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        N=len(books)
        dp=[math.inf]*N
        
        for i in range(N):
            j=i
            w=h=0
            while j>=0 and w+books[j][0]<=shelfWidth:
                w+=books[j][0]
                h=max(h,books[j][1])
                prev=dp[j-1] if j>0 else 0
                dp[i]=min(dp[i],prev+h)
                j-=1
        
        return dp[-1]
```