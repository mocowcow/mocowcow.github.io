---
layout      : single
title       : LeetCode 3028. Ant on the Boundary
tags        : LeetCode Easy Array Simulation
---
周賽383。

## 題目

有隻螞蟻站在邊界上，他有時候走左，有時候走右。  

輸入非零整數陣列 nums，依序代表螞蟻的移動順序。每次移動規則如下：  

- 若 nums[i] < 0，則向走左 -nums[i] 步  
- 若 nums[i] > 0，則向走左 nums[i] 步  

求螞蟻會**回到邊界**幾次。  

注意：  

- 邊界兩方無限寬廣  
- 只有在螞蟻**移動結束**才進行判定。也就是說，如果移動中有經過邊界，但沒有停留，則不計入  

## 解法

說邊界好像有點怪怪的，乾脆叫**起點**。  

反正就是照著移動，移動完停在起點的話答案就加 1。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        ans = 0
        curr = 0
        for x in nums:
            curr += x
            if curr == 0:
                ans += 1
                
        return ans
```
