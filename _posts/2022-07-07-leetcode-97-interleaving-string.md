--- 
layout      : single
title       : LeetCode 97. Interleaving String
tags        : LeetCode Medium String DP
---
每日題。好久以前就看過這題，但是想不出bottom up解法，感覺很麻煩就沒碰。沒想到今天腦子不太對勁，用top down一次就過了。

# 題目
輸入字串s1、s2和s3， 判斷s3是否能由s1和s2**交織**而成。  
**交織**指的是將s1和s2拆成若干個子字串，且子字串保持著原本的相對順序，組成s3。  

![圖例](https://assets.leetcode.com/uploads/2020/09/02/interleave.jpg)

# 解法
這題目靠著文字還真不好描述，圖片一出來倒是很清楚想要做什麼。  
反正大概就是從s1和s2的最左邊開始，每次從其中一邊選擇字元，最後組成s3。  

因為s1和s2的每個字元都必須被使用到，所以這兩個字串的長度加起來必須等於s3，才有可能交織成功，否則直接回傳false。  
要滿足當前目標字元s3[k]，可以從s1[i]或是s2[j]之中選擇一個，並繼續求剩下的子字串是否能交織。  

定義dp(i,j,k)：以s1到第i個索引的子字串、s2到第j個索引的子字串，能否組成s3到第k個索引的子字串。  
轉移方程式：若s1[i]或s2[j]等於s3[k]，且剩餘的子字串依然能夠組成s3剩下長度k-1的子字串，則回傳true；否則回傳false。  
base case：當k小於0，代表s3已經全部滿足了，直接回傳true。  

答案為dp(s1的最後索引, s2的最後索引, s3的最後索引)。  

```python
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        M=len(s1)
        N=len(s2)
        O=len(s3)
        
        @cache
        def dp(i,j,k):
            if k<0:
                return True
            ans=False
            if i>=0 and s1[i]==s3[k] and dp(i-1,j,k-1):
                ans=True
            if j>=0 and s2[j]==s3[k] and dp(i,j-1,k-1):
                ans=True
            return ans
        
        if M+N!=O:
            return False
        return dp(M-1,N-1,O-1)
```
