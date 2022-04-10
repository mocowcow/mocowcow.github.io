---
layout      : single
title       : LeetCode 2233. Maximum Product After K Increments
tags 		: LeetCode Medium Array Heap    
---
周賽288。早知道先做第三題了，耗時比前兩題都短。  

# 題目
輸入整數陣列nums和整數k。你可以對nums中任何一個數字+1，最多k次。  
求加完k次後，將nums中所有數相乘，可以得到的最大乘積為多少。答案可能很大，需要模10^9+7後再回傳。

# 解法
連乘想要把乘積最大化，就要從最小數字下手。  
把nums整個塞進heap裡面，然後進行k次增加，每次取出最小值+1後再塞回去。  
最後對修改過後的nums一邊連乘一邊mod，最後乘積就是答案。

```python
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        h=nums
        heapify(h)
        for _ in range(k):
            t=heappop(h)
            heappush(h,t+1)

        ans=1
        MOD=10**9+7
        for n in h:
            ans=(ans*n) % MOD
            
        return ans
```

