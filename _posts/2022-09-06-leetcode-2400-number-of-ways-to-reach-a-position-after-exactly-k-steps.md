--- 
layout      : single
title       : LeetCode 2400. Number of Ways to Reach a Position After Exactly k Steps
tags        : LeetCode Medium Array DP
---
周賽309。總算碰到和我腦波頻率相同的dp題，沒想到真正的大神竟然都是數學解，看來我還有得學。  

# 題目
輸入兩個正整數startPos和endPos。你從startPos出發，每步可以選擇往右或往左走。  
輸入正整數k，求從startPos出發走k步，到達endPos的方式有幾種。答案很大，需要模10^9+7後回傳。  

注意：如果移動順序不完全相同，則兩種方式視為不同的。位置座標也可以為**負數**。  

# 解法
求移動方式的計數、要對答案取餘數、測資範圍1000，這三點看下來很直覺是二維dp。  

定義dp(curr,step)：目前位置為curr，已經走了step步，到達endPos的方法有幾種。  
轉移方程式：只往左或是往右，dp(curr,step)=dp(curr-1,step+1)+dp(curr+1,step+1)  
base cases：當走完k步時，若剛好在endPos上則回傳1，代表有一種新的方式；否則無法抵達，回傳0。  

最後可以加上剪枝：當剩餘步數根本不可能從curr移動到endPos時，直接回傳0，不用浪費時間了。  
順帶一提，因為可以朝兩個方向走，若改成bottom up方式的話應該要開2000\*1000的矩陣，而不是1000\*1000。

```python
class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD=10**9+7
        
        @cache
        def dp(curr,step):
            if step==k:
                return curr==endPos
            if abs(curr-endPos)>k-step:
                return 0
            cnt=dp(curr-1,step+1)+dp(curr+1,step+1)
            return cnt%MOD
            
        return dp(startPos,0)
```
