---
layout      : single
title       : LeetCode 3010. Divide an Array Into Subarrays With Minimum Cost I
tags        : LeetCode Easy Array Sorting Heap
---
雙周賽122。

## 題目

輸入長度 n 的整數陣列 nums。  

一個陣列的**成本**等於他的**第一個元素**。例如 [1,2,3] 的成本是 1。  

你要將 nums 分割成三個的獨立子陣列。  
求這三個陣列的最小總成本。  

## 解法

第一個子陣列的開頭一定是 nums[0]，成本是固定的。  
我們只需要找到除了 nums[0] 以外的兩個最小元素當作子陣列開頭即可。  

除掉第一個元素之後排序，抓最前方兩個即可。  

時間複雜度 O(N log N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        a = sorted(nums[1:])
        return nums[0] + sum(a[:2])
```
