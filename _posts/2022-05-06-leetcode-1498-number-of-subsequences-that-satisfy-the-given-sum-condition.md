--- 
layout      : single
title       : LeetCode 1498. Number of Subsequences That Satisfy the Given Sum Condition
tags        : LeetCode Medium Array TwoPointers Sorting BinarySearch
---
好像是二分搜學習計畫的，~~超級不適合二分搜~~。

# 題目
輸入陣列nums和整數target。求有多少子序列符合以下規則：  
- 不為空序列  
- 序列中最大值+最小值總和小於target  

答案可能很大，需要模10^9+7後回傳。

# 解法
題目要求的是子序列，而且不用管子序列本身長什麼樣子，只求合法的數量，那把nums排序也不影響答案。  
排序後就變成簡單的雙指針問題，左指針是最小元素，右指針是最大元素，若兩者相加超過target，則將右指針收縮；否則以此範圍計算答案，從l到r，共有r-l+1個元素，而我們要計算以l為開頭的子序列數量，右方有r-l個元素可以選擇拿或不拿，所以共有2^(r-l)個子序列。

這題還有另一個難點在2^x的計算，剛好python內建的pow函數就有快速冪功能，其他語言則要自己刻快速冪，同時套用模運算，否則一定會TLE。

瓶頸為排序，時間複雜度O(N log N)。  
空間複雜度O(1)。  

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

2023-05-06更新。  

每日題竟然放這麼難，而我這次最先想到二分搜。  
當初怎麼想到雙指針的，真神奇。  

排序後，窮舉nums[i]作為子序列中最小的數，這時合法的最大值應為target-nums[i]。  
用二分搜找到最後一個小於等於最大值的索引j。因為nums[i]為最小值，所以j必須要大於等於i才合法。  
i\~j之間共有cnt個數，nums[i]必選，剩下cnt-1的數可選可不選，答案增加2^(cnt-1)種。  

瓶頸為排序，時間複雜度O(N log N)。  
空間複雜度O(1)。  

```python
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD=10**9+7
        nums.sort()
        ans=0
        
        for i,x in enumerate(nums):
            if x>target:
                break
            j=bisect_right(nums,target-x)-1
            if j>=i:
                cnt=j-i+1
                ans=(ans+pow(2,cnt-1,MOD))%MOD
                
        return ans
```