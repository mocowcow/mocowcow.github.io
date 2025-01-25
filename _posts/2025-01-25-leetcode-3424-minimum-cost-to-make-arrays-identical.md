---
layout      : single
title       : LeetCode 3424. Minimum Cost to Make Arrays Identical
tags        : LeetCode Medium Greedy Sorting
---
biweekly contest 148。

## 題目

<https://leetcode.com/problems/minimum-cost-to-make-arrays-identical/>

## 解法

如果不分割，答案就是所有 abs(arr[i] - brr[i]) 之和。  

若分割，則分割成大小 1 的子陣列最划算，相當於**所有元素可任意重排**。  
既然能重排，arr 中的元素都可以選擇要對應到 brr 的哪個元素了。  
最小的 arr[i] 與最小的 brr[i] 配，次小的與次小的配，以此類推。  

時間複雜度 O(N log N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        # no sort
        ans = 0
        for a, b in zip(arr, brr):
            ans += abs(a-b)

        # sort
        arr.sort()
        brr.sort()
        cost = k
        for a, b in zip(arr, brr):
            cost += abs(a-b)

        return min(ans, cost)
```
