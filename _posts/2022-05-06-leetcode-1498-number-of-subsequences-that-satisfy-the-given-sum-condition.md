--- 
layout      : single
title       : LeetCode 1498. Number of Subsequences That Satisfy the Given Sum Condition
tags        : LeetCode Medium Array TwoPointers Sorting
---
好像是二分搜學習計畫的，一樣超級不適合二分搜。

# 題目
輸入陣列nums和整數target。求有多少子序列符合以下規則：  
- 不為空序列  
- 序列中最大值+最小值總和小於target  

答案可能很大，需要模10^9+7後回傳。

# 解法
題目要求的是子序列，而且不用管子序列本身長什麼樣子，只求合法的數量，那把nums排序也不影響答案。  
排序後就變成簡單的雙指針問題，左指針是最小元素，右指針是最大元素，若兩者相加超過target，則將右指針收縮；否則以此範圍計算答案，從l到r，共有r-l+1個元素，而我們要計算以l為開頭的子序列數量，右方有r-l個元素可以選擇拿或不拿，所以共有2^(r-l)個子序列。

這題還有另一個難點在2^x的計算，剛好python內建的pow函數就有快速冪功能，其他語言則要自己刻快速冪，同時套用模運算，否則一定會TLE。

```python
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD=10**9+7
        nums.sort()
        ans=0
        l=0
        r=len(nums)-1
        while l<=r:
            if nums[l]+nums[r]>target:
                r-=1
            else:
                ans+=pow(2,(r-l),MOD)
                l+=1
                
        return ans%MOD
```
