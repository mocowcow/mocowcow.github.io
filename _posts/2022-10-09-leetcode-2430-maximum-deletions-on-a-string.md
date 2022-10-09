--- 
layout      : single
title       : LeetCode 2430. Maximum Deletions on a String
tags        : LeetCode Hard String DP
---
周賽313。還滿尷尬的題目，因為python的字串切片效率太快，導致有些人O(N^3)解法可以通過，這倒是我沒想到的。  

# 題目
輸入一個由小寫英文字母組成的字串s。  

每次操作中，你可以：  
- 刪除整個字串s，或是  
- 對於1 <= i <= s.length / 2 範圍內任何i，如果s的前i個字母和接著的i個字母相同，則可以刪除s的前i個字母

例如，如果s = "ababc"，那麼在一次操作中，可以刪除s的前兩個字母"ab"後得到"abc"，因為"ab"從前方連續出現兩次。  

求刪除s所需的**最大**操作次數。  

# 解法
題目要求越多刪除次數越好，所以要盡可能從前面多刪幾次，真的沒辦法才刪整個s。  
例題給的提示很明顯，根據不同的刪除方式，會產生不同的子字串，也有各自不同的刪除次數。處理這種子問題當然就是dp。  

定義dp(s)：字串s的最大刪除次數。  
轉移方程式：max(dp(s[size:]))+1，其中size為前綴的長度，且前綴s[:size]連續出現兩次。  
base case：字串s長度剩下1或是沒有可刪除的前綴，直接刪除整個s，回傳1。  

但是字串s長度為N，最差的狀況下會產生種N/2個子狀態，且每次產生子字串都要O(N)，整體時間複雜度高達O(N^3)，結果當然是TLE。  

```python
class Solution:
    def deleteString(self, s: str) -> int:
        
        @cache
        def dp(s):
            ans=0
            for i in range(len(s)//2):
                size=i+1
                if s[:size]==s[size:size*2]:
                    ans=max(ans,dp(s[size:]))
            return ans+1
        
        return dp(s)
```

我們需要把比對子字串的部分優化，找到O(1)的比對方法來降低成本。  
這時候要先預處理最長公共前綴(LCP)，定義lcp[i][j]為兩個子字串s[i:]和s[j:]所共用的最長前綴長度。只要lcp長度大於某前綴大小size，則可以確定該前綴重複出現兩次。  

時間複雜度降低到O(N^2)，空間複雜度O(N^2)。雖然官方後來新增一些測資，python變得連O(N^)都跑不過了，要有個公正的評判標準真難。  

```python
class Solution:
    def deleteString(self, s: str) -> int:
        if len(set(s))==1:
            return len(s)
        
        N=len(s)
        lcp=[[0]*(N+1) for _ in range(N+1)]
        
        for i in range(N-1,-1,-1):
            for j in range(N-1,-1,-1):
                if s[i]==s[j]:
                    lcp[i][j]=lcp[i+1][j+1]+1
                    
        dp=[0]*N
        for i in range(N-1,-1,-1):
            for size in range(1,(N-i)//2+1):
                if lcp[i][i+size]>=size:
                    dp[i]=max(dp[i],dp[i+size])
            dp[i]+=1
                
        return dp[0]
```