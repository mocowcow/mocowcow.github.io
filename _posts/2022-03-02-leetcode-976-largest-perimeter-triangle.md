---
layout      : single
title       : LeetCode 976. Largest Perimeter Triangle
tags 		: LeetCode Easy Math Greedy Sorting
---
Study Plan - Programming Skills。

# 題目
輸入整數陣列nums，任選三個值做成三角形，求三角形最大周長。

# 解法
兩個短邊加起來一定要大於長邊才能構成三角形。  
把nums降冪排序，從頭開始找，如果長邊小於後兩個邊長和就回傳周長，否則拋棄長邊，並加入下一個邊長。最後都沒合法的三角形則回傳0。

```python
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=1)
        for i in range(len(nums)-2):
            if nums[i]<nums[i+1]+nums[i+2]:
                return nums[i]+nums[i+1]+nums[i+2]
            
        return 0
```
