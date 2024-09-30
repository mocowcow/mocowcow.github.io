---
layout      : single
title       : LeetCode 3300. Minimum Element After Replacement With Digit Sum
tags        : LeetCode Easy Simulation
---
biweekly contest 140。  

## 題目

輸入整數陣列 nums。  

你必須將 nums 中的每個元素替換成其數位的**總和**。  

求替換後，nums 中的最小元素。  

## 解法

依照題意模擬。  

時間複雜度 O(N log MX)，其中 MX = max(nums)。  
空間複雜度 O(1)。  

```python
class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = inf
        for x in nums:
            val = 0
            while x > 0:
                val += x % 10
                x //= 10
            ans = min(ans, val)

        return ans
```

python 快樂一行版。  

```python
class Solution:
    def minElement(self, nums: List[int]) -> int:
        return min(sum(map(int, str(x))) for x in nums)
```
