---
layout      : single
title       : LeetCode 3478. Choose K Elements With Maximum Sum
tags        : LeetCode Medium Sorting Heap TwoPointers
---
weekly contest 440。

## 題目

<https://leetcode.com/problems/choose-k-elements-with-maximum-sum/description/>

## 解法

以 nums1[i] 遞增的順序填答案，可以確保更小的 nums1[j] 都已經出現過。  
用雙指針維護準備加入的元素，搭配 min heap 維護前 k 大的 nums2[j] 總和即可。  

時間複雜度 O(N log N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        N = len(nums1)
        a = sorted([x, i, nums2[i]] for i, x in enumerate(nums1)) # sort by nums1[i]
        
        sm = 0
        h = []
        ans = [0] * N
        j = 0
        for i, (x, idx, _) in enumerate(a):
            # add nums1[j] <= nums[i]
            while j < i and a[j][0] < x:
                val = a[j][2]
                sm += val
                heappush(h, val)
                if len(h) > k:
                    sm -= heappop(h)
                j += 1

            # answer query
            ans[idx] = sm

        return ans
```

也可以用分組循環，批次處理具有相同值的 nums1[i]。  

```python
class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        N = len(nums1)
        a = sorted([x, i, nums2[i]] for i, x in enumerate(nums1)) # sort by nums1[i]
        
        sm = 0
        h = []
        ans = [0] * N
        i = 0
        while i < N:
            # index in a[i..j] are same nums[i]
            j = i
            while j+1 < N and a[j+1][0] == a[i][0]:
                j += 1

            # answer query
            for _, idx, val in a[i:j+1]:
                ans[idx] = sm

            # add nums2[j]
            for _, idx, val in a[i:j+1]:
                sm += val
                heappush(h, val)
                if len(h) > k:
                    sm -= heappop(h)
            
            i = j+1

        return ans
```
