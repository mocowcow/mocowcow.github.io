---
layout      : single
title       : LeetCode 1508. Range Sum of Sorted Subarray Sums
tags 		: LeetCode Medium Array PrefixSum Sorting
---
題目很臭很長，排版還擠在一起。不確定是垃圾資訊太多，還是我沒有正確吸收到。

# 題目
輸入長度為n的正整數陣列nums。計算出nums生成的非空連續子陣列和，成為一個新的陣列。  
將新陣列遞增排序後，回傳其第left到第right個數總和。答案可能很大，必須模10^9+7後回傳。

# 解法
使用前綴和，先算出每個子陣列的總和陣列a，然後排序。  
把a在left到right內的的數邊加總邊MOD就是答案。  

如果不使用前綴和，複雜度會是O(N^3)，大概就會超時了。

```python
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD=10**9+7
        N=len(nums)
        a=[]
        
        for i in range(N):
            ps=0
            for j in range(i,N):
                ps+=nums[j]
                a.append(ps)
                
        a.sort()
        ans=0
        for i in range(left-1,right):
            ans=(ans+a[i])%MOD
            
        return ans
```

原來還有二分搜解法，看起來很麻煩，找個時間再來學習。