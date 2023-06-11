--- 
layout      : single
title       : LeetCode 2733. Neither Minimum nor Maximum
tags        : LeetCode Easy Array Sorting Simulation
---
周賽349。送分題。  

# 題目
輸入整數陣列nums，由不重複的正整數組成。  
找出任意一個**既非最小值也非最大值**的數字。若不存在則回傳-1。  

# 解法
照題意模擬。  

時間複雜度O(N)。  
空間複雜度O(1)。  

```python
class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        mn=min(nums)
        mx=max(nums)
        for x in nums:
            if x!=mn and x!=mx:
                return x
            
        return -1
```

如果要充分利用題目的**不重複**性值，可以保證至少要長度3以上才有答案。  
先檢查長度，如果足夠的話排序後回傳非首尾的任一數字。  

時間複雜度O(N log N)。  
空間複雜度O(1)。  

```python
class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return -1
        nums.sort()
        return nums[1]
```