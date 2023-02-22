--- 
layout      : single
title       : LeetCode 2573. Find the String with LCP
tags        : LeetCode Hard String Array Matrix DP
---
周賽333。剩十分鐘，看到lcp就絕望了。還以為又是什麼z-function之類的怪東西，其實思路想明白就很簡單。  

# 題目
對於長度為n，只由小寫字母組成的字串word，定義定義一個n\*n的矩陣lcp，滿足：  
- lcp[i][j]等於子字串word[i,..,n-1]和word[j,..,n-1]的**最長公共前綴**長度

輸入n\*n的矩陣lcp，求符合此矩陣，且**字典順序最小**的字串word。若不存在，則回傳空字串。  

# 解法
如果lcp[i][j]不為0，則代表i和j是相同的字元；否則一定為0，因為這是共通前綴。  
而題目要求字典順序最小的字串，所以要從0開始往後填，優先選用順序較小的字元，也就是從a開始。  

從遍歷所有索引i，若s[i]尚未填入字元，則找到所有與i相同字元的索引j(也就是lcp大於0)，全部填入相同字元。如果s中超過26種不同的字元，則無法滿足題目要求，直接回傳空字串。  

這時我們已經按照lcp的要求構造出一個長度為N的字串s。接著透過dp來求出s的lcp，檢查是否和題目的lcp相同：完全相同則回傳s，否則回傳空字串。  

定義dp[i][j]為：s[:i]和s[:j]的lcp長度。  
轉移方程式：若s[i]等於s[j]，則dp[i][j]=1+dp[i+1][j+1]；否則為0。  
base cases：i或j等於N時，超出邊界，lcp當然為0。  

建構s的部分為O(26\*N)，驗證lcp為O(N^2)，整體時間複雜度O(N^2)。空間複雜度O(N^2)。  

```python
class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        N=len(lcp)
        s=[""]*N
        c=0
        for i in range(N):
            if s[i]!="":continue
            if c==26:return ""
            for j in range(i,N):
                if lcp[i][j]!=0:
                    s[j]=chr(c+97)
            c+=1
        
        dp=[[0]*(N+1) for _ in range(N+1)]
        for i in reversed(range(N)):
            for j in reversed(range(N)):
                if s[i]==s[j]:
                    dp[i][j]=dp[i+1][j+1]+1
                else:
                    dp[i][j]=0
                if dp[i][j]!=lcp[i][j]:
                    return ""
        
        return "".join(s)
```
