--- 
layout      : single
title       : LeetCode 1340. Jump Game V
tags        : LeetCode Hard Array DP
---
隨便抽的，剛好抽到我最愛的DP題型，希望周賽也能碰到這種。

# 題目
輸入整數陣列arr和整數d。在每次移動，你可以從索引i跳到：
- i+x，符合i+x < arr.length 且 0 < x <= d  
- i-x，符合i-x >= 0 且 0 < x <= d  

而且i和j之間的所有索引k，arr[k]也必須小於arr[i]，使得arr[i]>arr[k]>=arr[j]。
你可以選擇任意索引作為起點，求最多可以抵達幾個索引位置。

# 解法
簡單來講就是從i可以往左或往右跳1\~d格，而且中間的所有高度必須小於arr[i]。  
定義dp(i)：從i出發，最多可以抵達的位置數量。  
轉移方程式：dp(i)=max(dp(j) for ALL abs(j-i)<=d 且 arr[j]<=arr[k]<arr[i] for ALL k between(i,j))  
base case：沒有其他位置可跳，只計算當前位置，回傳1。  

最後從每個位置中出發的最佳結果中，選擇最大者就是答案。  

```python
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        N=len(arr)
        
        @cache
        def dp(i):
            best=0
            # go left
            for j in range(i-1,i-d-1,-1):
                if j<0 or not arr[i]>arr[j]:
                    break
                best=max(best,dp(j))         
            # go right
            for j in range(i+1,i+d+1):
                if j>=N or not arr[i]>arr[j]:
                    break
                best=max(best,dp(j))       
            return best+1
        
        return max(dp(i) for i in range(N))
```
