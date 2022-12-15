--- 
layout      : single
title       : LeetCode 2498. Frog Jump II
tags        : LeetCode Medium Array BinarySearch Greedy
---
雙周賽93。有點類似[741. cherry pickup]({% post_url 2022-01-22-leetcode-741-cherry-pickup %})，很奇妙的綜合思考題。  

# 題目
輸入**嚴格遞增**的整數陣列stones，代表各石頭在河中的位置。  

有隻青蛙最初在第一顆石頭上，想要跳到最後一顆石頭，然後返回到第一顆石頭。但是**同顆石頭最多只能跳上去一次**。  

**跳躍長度**定義為兩顆石頭位置的絕對差，若從stones[i]跳到stones[j]，則跳躍長度為abs(stones[i]-stones[j])。  

**路徑成本**指的是所有跳躍中的**最大長度**。  
求路徑成本的**最小值**。  

# 解法
先看到**最大值最小化**，又看到測資範圍10^9，八九不離十就是第二分搜。  
仔細想想，如果青蛙能夠以最大長度x成功來回，那麼他肯定也能夠以x+1, x+2..來回，答案符合二分性質。  

最差情況下，直接從第一顆跳到最後一顆，上界為第一顆與最後一顆石頭的距離。  
最好情況下只有兩個石頭，而石頭位置不會重疊，那麼就設為1，或是設成第一、二顆石頭的距離也可以。  
開始二分答案，如果以最大長度mid能夠成功，那麼上界更新為mid；否則下界更新為mid+1。  

說是來回，其實就像撿櫻桃一樣，看做是兩隻青蛙同時從第一顆石頭出發，不踩到同樣的石頭，抵達最後一顆石頭後的最大跳躍長度。  
那這兩隻青蛙要怎麼跳才能使距離最小？  
假設有四個點ABCD，而青蛙位於A和B：  
> 如果讓青蛙A跳到C，會使B青蛙下次跳躍長度增加abs(C-D)  
> 如果讓青蛙B跳到C，會使A青蛙下次跳躍長度增加abs(C-D)  

既然兩者會增加的距離一樣，那麼選擇跳躍長度較大的青蛙先跳，肯定為較佳策略。當然，略過某顆石頭不跳的話，兩者的長度都會增加，是最差的選擇。  

每次二分搜都需要遍歷所有石頭，為O(N)，其中M為stones長度。整體時間複雜度為O(N log max(stones))。不需要額外空間，空間複雜度為O(1)。  

```python
class Solution:
    def maxJump(self, stones: List[int]) -> int:
        N=len(stones)
        
        def f(step):
            i=j=0
            for n in stones:
                if i+step<n:return False
                i=j
                j=n
            return True
                
        hi=stones[-1]
        lo=1
        while lo<hi:
            mid=(lo+hi)//2
            if not f(mid):
                lo=mid+1
            else:
                hi=mid
                
        return lo
```

後來才發現根本不用二分，根據上方的結論，兩隻青蛙輪流跳一定是最佳解，那就直接跳，看最大一步跳多遠就是答案。  

第一隻青蛙肯定跳到第二顆石頭，而第二隻青蛙肯定跳到第三顆，接下來開始依序輪流跳到i+2。  
若石頭只有兩顆，那麼答案會是第一、二顆石頭的距離；否則每次跳躍距離為stones[i+2]-stones[i]。  

```python
class Solution:
    def maxJump(self, stones: List[int]) -> int:
        N=len(stones)
        ans=stones[1]-stones[0]
        
        for i in range(2,N):
            ans=max(ans,stones[i]-stones[i-2])
    
        return ans
```