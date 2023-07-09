--- 
layout      : single
title       : LeetCode 2771. Longest Non-decreasing Subarray From Two Arrays
tags        : LeetCode Medium Array DP
---
周賽353。一開始往貪心的方向去想，吃了一個WA。  

# 題目
輸入長度n的整數陣列nums1和nums2。  

定義長度同為n的整數陣列nums3，其中nums3[i]可以由nums1[i]或nums2[i]組成。  

你的目標是在nums3中，找到**最長的非遞減子陣列**。  

求nums3的**最長的非遞減子陣列**長度。  

# 解法
當在考慮nums3[i]要選誰時，前一個選的可能是nums1[i-1]或是nums2[i-1]，或是根本沒選。  
不同的選法會產生重疊子問題，故考慮dp。  

定義dp(i,prev)：前一個選的數字是prev，以nums3[i]開頭的**最長的非遞減子陣列**長度。  
轉移方程式：max(選nums1, 選nums2, 都不選)。若nums1>=prev則可考慮nums1，若nums2>=prev則可考慮nums2。  
base case：當i=N時，沒東西可選，回傳0。  

最長的子陣列有可能以任意一個索引為起點。起點的數字不受限制，故枚舉所有索引i，以dp(i,0)更新答案。  

對於每個索引i來說，prev只有三種可能：nums1[i-1]、nums2[i-1]或0。  
時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        N=len(nums1)
        
        @cache
        def dp(i,prev):
            if i==N:
                return 0
            res=0
            if nums1[i]>=prev:
                res=max(res,dp(i+1,nums1[i])+1)
            if nums2[i]>=prev:
                res=max(res,dp(i+1,nums2[i])+1)
            return res
        
        ans=0
        for i in range(N):
            ans=max(ans,dp(i,0))
            
        return ans
```
