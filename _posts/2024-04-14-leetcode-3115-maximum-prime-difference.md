---
layout      : single
title       : LeetCode 3115. Maximum Prime Difference
tags        : LeetCode Medium Array Math Greedy
---
周賽 393。

## 題目

輸入整數陣列 nums。  

求兩個索引 i, j 的最大距離差。其中 nums[i], nums[j] 都是質數，且 i, j 可以相同。  

## 解法

為了使距離最大化，nums[i] 的索引越小越好，而 nums[j] 索引越大越好。  

找出所有質數的索引，答案就是最後一個減第一個。  

時間複雜度 O(N \* sqrt(MX))，其中 MX = max(nums)。  
空間複雜度 O(N)。  

```python
class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        a = [i for i, x in enumerate(nums) if is_prime(x)]
        return a[-1] - a[0]
        
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
```
