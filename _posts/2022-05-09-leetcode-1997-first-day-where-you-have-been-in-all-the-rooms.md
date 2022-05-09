--- 
layout      : single
title       : LeetCode 1997. First Day Where You Have Been in All the Rooms
tags        : LeetCode Medium Array DP
---
去年某次周賽沒寫出來的Q3。當時連這是DP都不知道，有夠誇張的題目，難度直逼Q4。

# 題目
你要訪問N個房間，分別從編號0\~N-1。從第0天開始，你每天都會訪問一個房間。  

第0天你一定是訪問0號房。輸入長度為N的陣列nextVisit，你訪問房間次序遵循以下規則：  
- 某天你訪問了i號房  
- 如果你訪問i號房的次數是奇數(包含這次)，明天你必須訪問第nextVisit[i]號房，nextVisit[i]不會超過i  
- 如果你訪問i號房的次數是偶數(包含這次)，明天你必須訪問第(i+1) mod N號房  

求在哪一天可以訪問完所有的房間，答案保證存在，且可能很大，必須模10^9+7後再回傳。

# 解法
那時候我好像沒有沒有搞清楚題意，加上題目講什麼(i+1)%N，還以為會亂序訪問，根本被騙。  

nextVisit[i]一定只會出現小於等於i的房間號，所以第一次能到達i+1的路線，**一定只有i一個**，那麼首次訪問i號房，至少要訪問前一號房**兩次**。  
但有個問題：第一次抵達i號房是從0號房出發，但是第二次抵達是從nextVisit[i]號房出發，有可能少用幾天。這樣遞迴關係就很清楚了。  
定義dp(i)為訪問到第i號房的所需天數。  
轉移方程式：dp(i)=(dp(i-1)+1)*2-dp(nextVisit[i-1])
base case：i=0為起點，第一天就在這裡。  

```python
class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        MOD=10**9+7
        N=len(nextVisit)
        dp=[0]*N
        for i in range(1,N):
            dp[i]=((dp[i-1]+1)*2-dp[nextVisit[i-1]])%MOD
        
        return dp[-1]
```
