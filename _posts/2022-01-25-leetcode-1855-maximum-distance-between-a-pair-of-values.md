---
layout      : single
title       : LeetCode 1855. Maximum Distance Between a Pair of Values
tags 		: LeetCode Medium BinarySearch
---
# 題目
輸入遞減整數陣列nums1、nums2，長度分別為M、N。  
求i和j的最大差值。(i,j)必須滿足以下條件：  
1. 0 <= i < M
2. 0 <= j < N
3. i <= j
4. nums1[i] <= nums2[j]  
   
# 解法
一看到有序就該想到二分搜。因為j必須大於等於i，那每次搜尋的範圍就是(i~M-1)。  
對(M,N)取最小值，可以省略掉多餘計算。

```python
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        M = len(nums1)
        N = len(nums2)
        ans = 0
        for i in range(min(M, N)):
            left = i
            right = N-1
            while left < right:
                mid = (left+right+1)//2
                if nums2[mid] >= nums1[i]:
                    left = mid
                else:
                    right = mid-1
            ans = max(ans, left-i)

        return ans
```
