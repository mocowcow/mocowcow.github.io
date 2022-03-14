---
layout      : single
title       : LeetCode 5. Longest Palindromic Substring
tags 		: LeetCode Medium DP TwoPointers
---
經典的DP題，沒事就多複習幾次。而且解法多元，甚至有O(N)解法，十分有趣。

# 題目
字串s，求s裡可以找到最長的回文子字串。  
任一種答案即可，s = "babad"，可以為"bab"或是"aba"。

# 解法
一般來說應該比較容易想到DP解法。  
dp(l,r)表示子字串的起點為l，終點為r，若成立回文則為true，否則false。  
轉移方程式：dp(l,r) = s[l]等於s[r] 且 r-l為1或dp(l+1,r-1)為true。  
base cases：l和r相同時，只有單一字元，肯定回文。或是l和r相鄰且相同，無法再縮，也是回文(已經併入轉移方程)。  
計算dp時順便更新長度以及起始座標，最後以起始座標+長度取得子字串回傳。  
time-space O(N^2)，跑了5095ms。

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        N=len(s)
        dp=[[False]*N for _ in range(N)]
        size=1
        start=0

        #init size 1 substring
        for i in range(N):
            dp[i][i]=True
            
        for r in range(N):
            for l in range(r):
                if s[l]==s[r] and (r-l==1 or dp[l+1][r-1]):
                    dp[l][r]=True
                    if r-l+1>size:
                        size=r-l+1
                        start=l
                        
        return s[start:start+size]

```

再來是雙指標，這種方法比較像人類的查找方法。  
分別以字串中的每一個位置為中心點，試圖往左右擴展。  
比較特別的是回文中心部分有可能有多個字元，如"..a.."或"..aa.."甚至是"..aaaaaaa.."，所以在確認中心點後，若右方字元與中心相同，可以持續向右擴展，保證整個中心部位被納入。  
再來是同時擴展兩方，若l左邊以及r右邊還有字元且相同，同時移動一格。停止擴展後更新長度。  
time O(N^2) space O(1)，雖然時間複雜度相同，但是跑起來快很多，只要1065ms。  

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        N=len(s)
        start=0
        size=1

        for center in range(N):
            l=r=center
            #expand center part
            while r+1<N and s[r]==s[r+1]:
                r+=1
            #expand two sides
            while l>0 and r+1<N and s[l-1]==s[r+1]:
                l-=1
                r+=1
            #update longest size
            if r-l+1>size:
                size=r-l+1
                start=l
                
        return s[start:start+size]
```
