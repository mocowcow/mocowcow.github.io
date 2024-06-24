---
layout      : single
title       : LeetCode 3194. Minimum Average of Smallest and Largest Elements
tags        : LeetCode Easy Array Sorting Simulation
---
周賽 403。

## 題目

你有一個浮點數陣列 averages，初始值為空。  
輸入長度 n 的整數陣列 nums，且保證 n 是偶數。  

你必須執行以下操作 n / 2 次：  

- 刪除 nums 中最小的元素 minElement，還有最大的元素 maxElement  
- 將 (minElement + maxElement) / 2 加入 averages  

回傳 averages 的最小值。  

## 解法

按照題意模擬。  
為了方便取最大 / 最小值，把 nums 排序後放入雙向隊列中，重複操作直到隊列為空。  

時間複雜度 O(n log n)。  
空間複雜度 O(n)。  

```python
class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        q = deque(sorted(nums))
        avgs = []
        while q:
            a = q.popleft()
            b = q.pop()
            avgs.append((a + b) / 2)
            
        return min(avgs)
```

nums 原地排序後，直接枚舉可以節省額外空間。  

時間複雜度 O(n log n)。  
空間複雜度 O(1)。  

```python
class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        N = len(nums)
        nums.sort()
        ans = inf
        for i in range(N // 2):
            a = nums[i]
            b = nums[N - 1 - i]
            ans = min(ans, (a + b) / 2)
            
        return ans
```
