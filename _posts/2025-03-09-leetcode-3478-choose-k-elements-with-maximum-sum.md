---
layout      : single
title       : LeetCode 3478. Choose K Elements With Maximum Sum
tags        : LeetCode Medium Sorting Heap
---
weekly contest 440。

## 題目

<https://leetcode.com/problems/choose-k-elements-with-maximum-sum/description/>

## 解法

以 nums1[i] 遞增的順序填答案，可以確保更小的 nums1[j] 都已經出現過。  
搭配 min heap 維護前 k 大的 nums2[j] 總和即可。  

時間複雜度 O(N log N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        N = len(nums1)
        a = sorted([x, i] for i, x in enumerate(nums1)) # sort by nums1[i]
        
        sm = 0
        h = []
        ans = [0] * N
        j = 0
        for i, (x, qi) in enumerate(a):
            # add nums1[j] <= nums[i]
            while j < i and a[j][0] < x:
                idx = a[j][1]
                val = nums2[idx]
                sm += val
                heappush(h, val)
                if len(h) > k:
                    sm -= heappop(h)
                j += 1

            ans[qi] = sm

        return ans
```
