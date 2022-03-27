---
layout      : single
title       : LeetCode 2218. Maximum Value of K Coins From Piles
tags 		: LeetCode Hard DP 
---
周賽286。今天終於四題全過，夠我開心一整天。

# 題目
二維陣列piles代表錢幣堆，piles[i]從左到右代表錢幣由頂端到尾端的順序。  
每堆錢幣一定要先拿頂端後，才能拿底下的。求拿k個錢幣最多可以獲得多少錢。

# 解法
k<=硬幣總數<=2000，size(piles)<=1000，一眼就知道DP。  
剛開始思考方向錯誤，又差點歪到要記錄哪堆拿過幾個錢幣，好險及時拉回來。  

定義dp(i,k)為到第i堆硬幣為止，總共拿了k個硬幣的最大值。答案就是回傳dp(N-1,k)。  
在第i堆的時候，可以決定拿0~min(k,piles[i]大小)個硬幣，剩下的次數k留給i左邊的其他堆。  
轉移方程式：dp(i,k)=max(sum(piles[i]前x項)+dp(i-1,k-x)) FOR ALL 0<=x<=size(piles[i])。  
edge cases：  
- i小於0，沒有這種錢堆了，回傳0  
- k等於0，沒辦法再拿了，回傳0  
- k<0，不允許多拿，回傳inf

雖然說轉移的時候有限制k的大小，理論上不會遇到k<0，以防萬一還是加了上去。  


```python
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        N=len(piles)
        
        @lru_cache(None)
        def dp(i,k): #to ith pile,take k coins
            if i<0: #no such pile
                return 0
            if k==0: #no take
                return 0
            if k<0: #take too much
                return math.inf
            acc=0
            best=dp(i-1,k) #no take in this pile
            #try take 1~j coins in this pile
            for j in range(len(piles[i])):
                if j+1>k:
                    break
                acc+=piles[i][j]
                best=max(best,acc+dp(i-1,k-j-1))
            return best        
        
        return dp(N-1,k)
```

