---
layout      : single
title       : LeetCode 3379. Transformed Array
tags        : LeetCode Easy Simulation
---
weekly contest 427。

## 題目

輸入整數陣列 nums，代表一個**循環**陣列。  
你必須建立一個相同大小的新陣列 result，並滿足以下條件。  

對於每個索引 i 執行以下操作：  

- 若 nums[i] > 0：從 i 向右走 nums[i] 步，並將抵達位置對應的值寫入 result[i]。  
- 若 nums[i] < 0：從 i 向左走 nums[i] 步，並將抵達位置對應的值寫入 result[i]。  
- 若 nums[i] == 0：將 nums[i] 寫入 result[i]。  

回傳新陣列 result。  

注意：nums 是循環的，如果從最後一個位置向右移動會回到陣列開頭；反之亦然。  

## 解法

沒什麼好說的，索引直接加上 nums[i] 後對 N 取餘數即可。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = [0] * N
        for i, x in enumerate(nums):
            t = (i+x) % N
            ans[i] = nums[t]

        return ans
```
