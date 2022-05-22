--- 
layout      : single
title       : LeetCode 647. Palindromic Substrings
tags        : LeetCode Medium String DP
---
每日題。很久以前只做過一次，但是解法卻記得很清楚，真不愧是經典題。

# 題目
輸入字串s，回傳其回文子字串的數量。  
都某字串向後讀與向前讀的結果相同時，就是回文。  
子字串是字串中連續的字元序列。  

# 解法
某個長度n的回文字串，將其左右各剔除一個字元，必定也是回文的。  
由此可得知遞迴關係，我們可以先從所有長度1的回文子字串，慢慢向兩方擴展。  

定義dp(i,j)表式起點為i，終點為j的子字串是否為回文。  
轉移方程式：dp(i,j) = s[i]等於s[j] 且 dp(i+1,j-1)為true。  
base case：當i等於j時，只有一個字元，必定是回文，故為true。  

窮舉每個i為中心點，試著向左右擴展，找到更長的回文子字串。  
但是回文的中心點有時候是偶數，例如'aa'和'aaaa'也都是回文，所以遍歷每個長度1的子字串時，可以先將j向右擴展。  
j停止擴展後，再判斷i左方與j右方的字元是否相同，若是則同時擴展一位。  
最後遍歷dp陣列，查看有多少true，即是回文子字串的數量。

```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        N=len(s)
        dp=[[False]*N for _ in range(N)]
        ans=0
        for i in range(N):
            dp[i][i]=True
            j=i
            while j+1<N and s[i]==s[j+1]:
                j+=1
                dp[i][j]=True
            while i>0 and j+1<N and s[i-1]==s[j+1]:
                i-=1
                j+=1
                dp[i][j]=True
                        
        for i in range(N):
            for j in range(N):
                if dp[i][j]:
                    ans+=1
                    
        return ans
```

但是題目根本沒有要問那些子字串回文，只求數量，那乾脆省略dp陣列，將空間簡化至O(1)。

```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        N=len(s)
        ans=0
        for i in range(N):
            ans+=1
            j=i
            while j+1<N and s[i]==s[j+1]:
                j+=1
                ans+=1
            while i>0 and j+1<N and s[i-1]==s[j+1]:
                i-=1
                j+=1
                ans+=1
                        
        return ans
```