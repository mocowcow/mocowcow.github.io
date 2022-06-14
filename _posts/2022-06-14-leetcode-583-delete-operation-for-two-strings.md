--- 
layout      : single
title       : LeetCode 583. Delete Operation for Two Strings
tags        : LeetCode Medium String DP
---
每日題。其實就是[1143. longest common subsequence]({% post_url 2022-02-08-leetcode-1143-longest-common-subsequence %})的變種。

# 題目
輸入兩個字串word1和word2，計算使word1和word2成為相同字串所需的最小動作次數。  
在一次動作中，可以刪除任一字串中的某一個字元。  

# 解法
透過最少的刪除次數使兩字串相同，換句話說，會剩下最長的共通子序列。  
那麼逆向計算，先找到共通子序列的長度x，假設兩個word的長度分別為M和N，word1需要刪除M-x次，而word2需要刪除N-x次。  

使用二維dp來找到最長共通子序列長度。  
定義dp[i][j]：以word1[i]和word2[j]結尾時的最長共通子序列長度。  
轉移方程式：  
- 若word1[i]等於word2[j] 則 dp[i][j]=dp[i-1][j-1]+1  
- 否則dp[i][j]=min(dp[i][j-1],dp[i-1][j])  

base cases：因為字串的第一個字元前方沒有狀態可以參考，所以i或j小於1時應回傳0。  
-1不為合法索引，所以將陣列長度加1、索引位移1，來處理base cases，因此dp陣列裡面的i,j索引都要加上1。  

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M,N=len(word1),len(word2)
        dp=[[0]*(N+1) for _ in range(M+1)]
        
        for i in range(M):
            for j in range(N):
                if word1[i]==word2[j]:
                    dp[i+1][j+1]=dp[i][j]+1
                else:
                    dp[i+1][j+1]=max(dp[i+1][j],dp[i][j+1])
                
        return M+N-dp[-1][-1]*2
```
