---
layout      : single
title       : LeetCode 3264. Final Array State After K Multiplication Operations I
tags        : LeetCode Easy Simulation
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

時間複雜度 O(NK)。  
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
