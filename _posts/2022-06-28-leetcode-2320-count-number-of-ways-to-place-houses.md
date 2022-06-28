--- 
layout      : single
title       : LeetCode 2320. Count Number of Ways to Place Houses
tags        : LeetCode Medium DP
---
周賽299。這題稍微卡了一下，可能是題目描述不太精準。後來發現很少人用我的解法，至少個人認為我的方法比較直觀。  

# 題目
有一條街道，街道兩側各有n塊地，共n*2塊。  
每塊地都可以放一棟房屋，但是同側不可以有房屋彼此相鄰。求有多少放置房屋的方式。  
答案可能很大，模10^9+7後回傳。  

# 解法
把道路上下方的地塊當作同一組，每組共有四種房屋擺法：  
- 不放房屋  
- 上面放  
- 下面放  
- 上下都放  

而其先決條件分別為：  
- 永遠合法  
- 前一組的上方為空  
- 前一組的下方為空  
- 前一組的上下皆為空  

dp[i][j]表示第i組以第j種擺法結尾的方式有幾種，最初那組沒有擺放限制，四種擺法都是1。  
又因為只會參考到前一個區域的狀態，所以可以將空間壓縮到一維。  

```python
class Solution:
    def countHousePlacements(self, n: int) -> int:
        MOD=10**9+7
        dp=[1]*4
        
        for _ in range(n-1):
            t=[0]*4
            t[0]=sum(dp)
            t[1]=dp[0]+dp[2]
            t[2]=dp[0]+dp[1]
            t[3]=dp[0]
            dp=t

        return sum(dp)%MOD
```

有人指出：上下兩排的地塊之間是獨立的，可以拆開成兩個相同的子問題，只要計算出單排的房屋擺法，相乘即可得到答案。  

dp[i]表示第i塊地結尾的排法有幾種。  
每塊地只有放和不放兩種選擇，若要放，前塊地不可放；不放，則無所謂。  
dp[i]的結尾方式有dp[i+1]+dp[i-2]種，而dp[0]沒有地，只有空序列一種排法；dp[1]沒有限制，放或不放都可以。  

求出dp[n]之後，平方後回傳。  

```python
class Solution:
    def countHousePlacements(self, n: int) -> int:
        MOD=10**9+7
        dp={0:1,1:2}
        for i in range(2,n+1):
            dp[i]=(dp[i-1]+dp[i-2])%MOD
            
        return (dp[n]*dp[n])%MOD
```