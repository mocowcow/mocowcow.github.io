---
layout      : single
title       : LeetCode 3467. Transform Array by Parity
tags        : LeetCode Easy Simulation
---
biweekly contest-151。

## 題目

<https://leetcode.com/problems/transform-array-by-parity/description/>

## 解法

按照題意模擬。  
把每個元素 x 對 2 取餘數，偶數會變成 0、奇數會變成 1，然後排序即可。  

時間複雜度 O(N log N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        return sorted([x % 2 for x in nums])
```

轉換後的元素只有 0 和 1，根本不需要排序。  
直接把所有 0 擺到前面，剩下的 1 擺到後面就好。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        cnt = Counter(x % 2 for x in nums)
        return [0] * cnt[0] + [1] * cnt[1]
```
