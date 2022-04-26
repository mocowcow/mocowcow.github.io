---
layout      : single
title       : LeetCode 940. Distinct Subsequences II
tags 		: LeetCode Hard String DP
---
相似題[1987. Number of Unique Good Subsequences]({% post_url 2022-04-26-leetcode-1987-number-of-unique-good-subsequences %})。這題寫起來真的就是秒殺，看來我跟他電波比較合。

# 題目
輸入字串s，求s的**非空**子序列有幾種。答案可能很大，要模10^9+7後回傳。

# 解法
s中會出現26個小寫英文字母，太多了所以乾脆用dict來存比較方便。  
定義dp[c]表示以字元c結尾的子序列數量。  
每次讀入一個字元c，可以產生(原有子序列總量)的新子序列，還有一個長度為1的子序列[c]。以其他非c結尾的數量不變。  

時間O(N)、空間O(1)，難得第一次就可以直接寫出最佳解答。

```python
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD=10**9+7
        dp=defaultdict(int)
        for c in s:
            dp[c]=(sum(dp.values())+1)%MOD
            
        return sum(dp.values())%MOD
```

改回空間O(N)的寫法，比較容易理解轉移狀態。  
dp[i][j]代表讀入s[i]後，以第j個英文字母結尾的子序列數量。  
轉移方程式：dp[i][j]=sum(dp[i-1])+1 若j==s[i] 否則 dp[i][j]=dp[i-1][j]  

```python
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        N=len(s)
        MOD=10**9+7
        dp=[[0]*26 for _ in range(N)]
        dp[0][ord(s[0])-97]=1
        for i in range(1,N):
            c=ord(s[i])-97
            for j in range(26):
                if j==c:
                    dp[i][j]=(sum(dp[i-1])+1)%MOD
                else:
                    dp[i][j]=dp[i-1][j]
        
        return sum(dp[-1])%MOD
```
