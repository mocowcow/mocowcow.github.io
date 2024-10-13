---
layout      : single
title       : LeetCode 3318. Find X-Sum of All K-Long Subarrays I
tags        : LeetCode Easy Sorting HashTable Simulation
---
weekly contest 419。  

## 題目

輸入長度 n 的整數陣列 nums，還有兩個整數 k 和 x。  

陣列的 x-sum 計算方式如下：  

- 統計陣列中所有元素的出現頻率。  
- 只保留頻率最高的前 x 種元素。若兩元素頻率相同，則保留**數值較大**者。  
- 求結果陣列的和。  

注意：若陣列中不同的元素少於 x 種，則 x-sum 等於陣列元素和。  

回傳長度為 n - k + 1 的陣列 answer，其中 answer[i] 代表子陣列 nums[i..i+k-1] 的 x-sum。  

## 解法

暴力法，枚舉子字串，並將出現的元素按照頻率、數值排序，只保留頻率前 x 大的元素。  

時間複雜度 O(N \* k log k)。  
空間複雜度 O(k)。  

```python
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        N = len(nums)
        ans = []
        left = 0
        for i in range(N-k+1):
            res = 0
            d = Counter(nums[i:i+k])
            items = sorted(d.items(), key=lambda x:(-x[1], -x[0]))
            for key, val in items[:x]:
                res += key * val
            ans.append(res)

        return ans
```
