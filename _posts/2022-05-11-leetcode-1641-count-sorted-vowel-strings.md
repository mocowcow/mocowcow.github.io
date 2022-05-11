--- 
layout      : single
title       : LeetCode 1641. Count Sorted Vowel Strings
tags        : LeetCode DP
---
每日題。竟然沒有繼續出回溯系列題，今天突然變成DPDP的一天。

# 題目
輸入整數n，求只由母音(a,e,i,o,u)所組成，且按字典順序排序的字串數量。  
字串s若按字典順序排序，須滿足：對所有的i，s[i]的字典順序必須小於等於s[i+1]。  

# 解法
簡單來說就是a後面可接aeiou，e後面可接eiou，i後面可接iou，o後面可接ou，最後u只能接u。  

將aeiou分別對應到01234。  
定義dp(i,j)：長度為i，且由第j個母音結尾的數量。  
轉移方程式：dp(i,j)=sum(dp(i-1,k) FOR ALL j<=k<5)  
base cases：當長度為1時，以各種母音開頭的字串都只有1個，故初始化為1。

```python
class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp=[[0]*5 for _ in range(n)]
        dp[0][0]=dp[0][1]=dp[0][2]=dp[0][3]=dp[0][4]=1
        for i in range(1,n):
            for j in range(5):
                for k in range(j,5):
                    dp[i][j]+=dp[i-1][k]
        
        return sum(dp[-1])
```

因為只會用到前一次的狀態，所以可以將空間壓縮到O(1)。  
又因為以u開頭的字串一直都只能有1種，乾脆省略不計，每次加上1代替就好。

```python
class Solution:
    def countVowelStrings(self, n: int) -> int:
        a=e=i=o=1
        for _ in range(1,n):
            a, e, i, o = a+e+i+o+1, e+i+o+1, i+o+1, o+1
            
        return a+e+i+o+1
``` 