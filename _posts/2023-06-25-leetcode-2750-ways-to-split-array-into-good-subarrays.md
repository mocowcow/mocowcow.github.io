--- 
layout      : single
title       : LeetCode 2750. Ways to Split Array Into Good Subarrays
tags        : LeetCode Medium Array 
---
周賽351。不小心把%=寫成%，拿到免費的BUG。  

# 題目
輸入二進位陣列nums。  

如果一個子陣列只擁有一個1元素，則稱為**好的**。  

求把nums分割成任意個**好的**子陣列有幾種方案。答案很大，先模10^9+7後回傳。  

# 解法
本來想說要靠dp維護子陣列中有多少個1元素，再來決定是否分割，仔細看看發現只有兩個1中間可以切一刀。  

如果兩個1之間的距離就是可以切的位置數量，根據乘法原理全部相乘就是答案。  

注意：整個nums中沒有1，那就根本不能弄出**好的**子陣列，答案就是0。  

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        MOD=10**9+7
        
        if 1 not in nums:
            return 0
        
        ones=[i for i,x in enumerate(nums) if x==1]
        ans=1
        for a,b in pairwise(ones):
            ans*=(b-a)
            ans%=MOD
        
        return ans
```
