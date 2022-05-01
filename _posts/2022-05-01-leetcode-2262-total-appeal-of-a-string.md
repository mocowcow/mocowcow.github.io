--- 
layout      : single
title       : LeetCode 2262. Total Appeal of A String
tags        : LeetCode Hard String DP
---
周賽291。苦思久等的DP終於來了，結果想不出轉移方程式，又是三題幫。  
看到測資10^5還是不信邪的用bitmask做O(N^2)，只通過62/76測資。

# 題目
輸入字串s，求s所有子字串的**總吸引力**。  
**吸引力**指的是一個字串中出現幾種**不同**的字元。  
例：  
> 'abbca' 不同字元='abc' 吸引力3  

# 解法
想半天終於搞懂了。  
定義dp(i)為：以索引i結尾的子字串總吸引力。  
dp(0)為base case，以索引0為結尾的子字串永遠只有一個，且總吸引力也固定是1。  

先考慮沒有字元重複出現的情況，如：  
> s = 'abc'  
> i=0, 子字串a  
> i=1, 子字串ab, b  
> i=2, 子字串abc, bc, c  
> 總吸引力為1+2+1+3+2+1=10

每當考慮索引i，會對i-1結尾的子字串全部加上s[i]，還有只有s[i]的子字串，共有i+1個字串以索引i結尾。  
可以得到結論：若s[i]的字元沒有出現過，dp[i]=dp[i-1]+1+**i**。  

那如果s[i]已經出現過怎麼辦？考慮以下情況：  
> s = 'abcb'  
> i=0, 子字串a  
> i=1, 子字串ab, b  
> i=2, 子字串abc, bc ,c  
> i=3, 子字串abcb, bcb, bc, b
> 總吸引力為1+2+1+3+2+1+3+2+2+1=18

到s[3]=b的時候，可以看出來，除了保底的[b]以外，只有從c變成cb多得到1點吸引力。  
因為b的上次出現位置在j=1，所以在j之前的所有子字串都已經拿過b的吸引力了，只有j+1開始後到i的新子字串可以獲得b的吸引力。  
從j+1開始到i，總共是i-(j+1)+1等於i-j個子字串。但是我們先前有計算保底的子字串s[i]，所以要再扣掉1，變成(i-j-1)。  
所以若s[i]已經在j出現過，dp[i]=dp[i-1]+1+**(i-j-1)**。

照著以上的思路寫成程式碼。原字串s的**所有子字串吸引力總和**就是dp陣列的加總。

```python
class Solution:
    def appealSum(self, s: str) -> int:
        N=len(s)
        dp=[0]*N # 以i結尾的子字串數量
        dp[0]=1
        last={}
        last[s[0]]=0
        for i in range(1,N):
            dp[i]=dp[i-1]+1 #保底一個長度1子字串
            if s[i] not in last: # 左方有i個子字串全部多1
                dp[i]+=i
            else: # 有i-j-1個子字串全部多1
                j=last[s[i]] # 上次出現位置j
                dp[i]+=i-j-1 
            last[s[i]]=i
            
        return sum(dp)
```

因為dp(i)只會取用到dp(i-1)的狀態，所以可以把空間壓縮到O(1)。順便把算式簡化。  

```python
class Solution:
    def appealSum(self, s: str) -> int:
        ans=0
        dp=0
        last={}
        for i,c in enumerate(s):
            if c in last:
                dp=dp+i-last[c]
            else:
                dp=dp+1+i
            last[c]=i
            ans+=dp
            
        return ans
```            
