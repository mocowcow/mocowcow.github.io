--- 
layout      : single
title       : LeetCode 790. Domino and Tromino Tiling
tags        : LeetCode Medium DP
---
推理型DP，第一次碰到的時候是每日題，那時我直接印出所有測資找出公式解，但沒有實際理解怎麼推導的。今天特地來補課，發現還真有點難度。

# 題目
你有兩個形狀的磁磚：多米諾和托米諾。你可以旋轉這些形狀。  
輸入整數n，代表2*n的地面，求有幾種將地面鋪滿的方法。

# 解法
有排列方法，一看就知道是dp，但不知道怎麼轉移。  
先定義dp(i)：鋪滿2*i地面的方法。  
base cases：i=0，沒有地面要鋪，一種方法；i=1，只有直著擺一種方法；i=2，兩根直或橫的，兩種方法。  
i=3開始就不太一樣了，這時候可以加入托米諾型磁磚。兩個托米諾可以排成2\*3的形狀，且有兩種擺法。所以dp(3)擺法共有：  
- dp(2)加上一根直的  
- dp(1)加上兩根橫的(兩根直的已經包含在dp(2)裡面)  
- dp(0)加上新出現的圖型：兩個托米諾，且有兩種擺法  
  
得到dp(3)=dp(2)+dp(1)+dp(0)*2。  
再來推算看dp(4)如何：  
- dp(3)加上一根直的  
- dp(2)加上兩根橫的  
- dp(1)加上兩個托米諾，且有兩種擺法  
- dp(0)加上新出現的圖形：兩個托米諾+一個多米諾，且有兩種擺法  

得到轉移方程式：dp(i)=dp(i-1)+dp(i-2)+(dp(i-3)+dp(i-4)..+dp(0))\*2  

```python
class Solution:
    def numTilings(self, n: int) -> int:
        MOD=10**9+7
        dp=[0]*1001
        dp[0]=1
        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
            for j in range(i-3+1):
                dp[i]+=dp[j]*2
            dp[i]%=MOD
                     
        return dp[n]
```

上面的時間複雜度O(N^2)，剛好測資n<=1000，還不會超時，如果再大一些就需要繼續優化轉移方程式。  
dp(i)=dp(i-1)+dp(i-2)+(dp(i-3)+dp(i-4)..+dp(0))\*2，又dp(i-1)=dp(i-2)+dp(i-3)+(dp(i-4)+dp(i-5)..+dp(0))\*2，最後簡化成dp(i)=dp(i-1)+dp(i-3)*2。  
不太懂怎麼推的，最終版本如下。

```python
class Solution:
    def numTilings(self, n: int) -> int:
        MOD=10**9+7
        dp=[0]*1001
        dp[1]=1
        dp[2]=2
        dp[3]=5
        
        for i in range(4,n+1):
            dp[i]=(dp[i-1]*2+dp[i-3])%MOD
                     
        return dp[n]
```