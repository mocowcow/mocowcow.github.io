--- 
layout      : single
title       : LeetCode 2555. Maximize Win From Two Segments
tags        : LeetCode Medium Array SlidingWindow DP
---
雙周賽97。有想到滑動窗口，但用的是貪心而不是dp，卡死整場。連續兩次只解出兩題有夠難受。  

# 題目
在**X軸**上有一些**獎品**。輸入**非遞減排序**的整數陣列prizePositions，其中prizePositions[i]為第i個獎品的位置。同一個位置上有可能有超過數個獎品。另外還有整數k。  

你可以選擇兩個區間，且區間的長度必須為k。你可以獲得區間覆蓋位置中的所有獎品。兩個區間可以重疊。  

例如：  
> k = 2時，你可以選擇[1, 3]和[2, 4]兩個區間，並得到1\~3和2\~4範圍內的所有獎品。  

求**最多**可以獲得多少獎品。  

# 解法
初始化左端點為0，並窮舉所有索引right作為右端點，若pos[right]到pos[left]的長度超過k，則不斷縮減左端點。  
這時候以right為右端點時，最多可以獲得right-left+1個獎品。我們必須在left左方再找一個最大的區間。  

維護長度N的陣列dp，其中dp[i]代表到從0到i為止，可以得到的最大區間。  
在上述窮舉right時，順便更新dp陣列。這時在每個right時，可以得到的兩個區間最大和為right-left+1+dp[left-1]，以此更新答案。  

時間複雜度O(N)。空間複雜度O(N)。  

```python
class Solution:
    def maximizeWin(self, pos: List[int], k: int) -> int:
        N=len(pos)
        dp=[0]*N
        ans=0
        left=0
        
        for right in range(N):
            while pos[right]-pos[left]>k:
                left+=1
            prev=0 if left==0 else dp[left-1]
            dp[right]=max(dp[right-1],right-left+1)  
            ans=max(ans,right-left+1+prev)
                    
        return ans
```
