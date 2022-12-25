--- 
layout      : single
title       : LeetCode 2511. Maximum Enemy Forts That Can Be Captured
tags        : LeetCode Easy Array String
---
雙周賽94。題目描述**超級爛**，對於空地一下使用"no fort"，一下使用"empty"，看半天才知道是同一件事情。  

# 題目
輸入長度n的整數陣列forts，代表堡壘的位置。forts[i]可以是-1, 0或是1：  
- -1代表空地  
- 0代表敵方堡壘  
- 1代表我方堡壘  

你決定將你的軍隊從位置i的我方堡壘移動到一個空地j：  
- 0 <= i,j <= n-1  
- 你的部隊**只能**越過**敵方堡壘**，也就是所有的位置k，其中forts[k]=0  

在移動部隊的過程中，所以經過的敵方堡壘都會**被佔領**。  
求可以佔領的敵方堡壘**最大數量**。如果無法移動部隊，或是沒有任何我方堡壘則回傳0。  

# 解法
簡單來說就是要從1出發，前往某一個-1，途中只能經過0，求最多可以連續幾個0。  

變數cap用來記錄移動途中所佔領的**敵方堡壘**數。因為要先抵達我方堡壘才開始計數，所以初始化為-inf。  
從左向右遍歷forts：  
- 若碰到空地-1則結算佔領數，更新答案，並重置cap為無限小  
- 若碰到敵方堡壘0則佔領數+1  
- 若碰到我方堡壘1則刷新佔領數，將cap設為0  

這樣只有涵蓋到1 -> -1的狀況，沒有處理到-1 <- 1，所以要再逆向計算一次。  

遍歷forts兩次，時間複雜度O(N)。空間複雜度O(1)。  

```python
class Solution:
    def captureForts(self, forts: List[int]) -> int:
        ans=0
        cap=-inf
        for n in forts:
            if n==-1:
                ans=max(ans,cap)
                cap=-inf
            elif n==0:
                cap+=1
            else:
                cap=0
        
        cap=-inf
        for n in reversed(forts):
            if n==-1:
                ans=max(ans,cap)
                cap=-inf
            elif n==0:
                cap+=1
            else:
                cap=0
                
        return ans
```

另一種解法，找到我方堡壘後向左右邊擴展。個人比較喜歡第一種解法就是。  

```python
class Solution:
    def captureForts(self, forts: List[int]) -> int:
        N=len(forts)
        ans=0
        
        for i,n in enumerate(forts):
            if n==1:
                # go right
                j=i+1
                while j<N and forts[j]==0:j+=1
                if j<N and forts[j]==-1:ans=max(ans,j-i-1)
                # go left
                j=i-1
                while j>=0 and forts[j]==0:j-=1
                if j>=0 and forts[j]==-1:ans=max(ans,i-j-1)
                    
        return ans
```
