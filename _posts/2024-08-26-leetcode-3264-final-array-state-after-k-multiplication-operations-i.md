---
layout      : single
title       : LeetCode 3264. Final Array State After K Multiplication Operations I
tags        : LeetCode Easy Simulation Heap
---
weekly contest 412。  

## 題目

輸入整數陣列 nums，還整數 k 和 multiplier。  

你需對 nums 執行 k 次操作。每次操作：  

- 找到 nums 中的最小值 x。若存在多個，則選最先出現者。  
- 將 x 替換成 x \* multiplier。  

執行完 k 次操作後，將 nums 回傳。  

## 解法

暴力模擬。  
先找最小值，在找第一個最小值並乘上 multiplier，重複 k 次即可。  

時間複雜度 O(Nk)。  
空間複雜度 O(1)。  

```python
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        N = len(nums)
        for _ in range(k):
            mn = min(nums)
            nums[nums.index(mn)] *= multiplier

        return nums
```

可以改用 min heap 維護最小值，不必每次都遍歷整個 nums。  
執行完操作後，再從 heap 中把值寫回 nums。  

時間複雜度 O(k log N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        h = []
        for i, x in enumerate(nums):
            heappush(h, [x, i])

        for _ in range(k):
            t = heappop(h)
            t[0] *= multiplier
            heappush(h, t)

        for x, i in h:
            nums[i] = x

        return nums
```
