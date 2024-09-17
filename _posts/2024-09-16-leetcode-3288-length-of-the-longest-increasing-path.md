---
layout      : single
title       : LeetCode 3288. Length of the Longest Increasing Path
tags        : LeetCode Hard DP BinarySearch Sorting
---
biweekly contest 139。  
這題就有點坐牢，沒做過原題大概想不出來，做過直接秒殺。  

## 題目

輸入長度 n 的二維整數陣列 coordinates，還有整數 k。其中 0 <= k < n。  
coordinates[i] = [x<sub>i</sub>, y<sub>i</sub>] 代表二維平面中的一個點。  

一條長度 m 的遞增路徑由點 (x1, y1), (x2, y2), (x3, y3), ..., (xm, ym) 組成，滿足：  

- 對於所有滿足 1 <= i < m 的 i 都有 x<sub>i</sub> < x<sub>i+1</sub> 且 y<sub>i</sub> < y<sub>i+1</sub>。  
- 對於所有 1 <= i <= m 的點 i 的座標 (x<sub>i</sub>, y<sub>i</sub>) 都在 coordinates 中。  

求包含座標 coordinates[k] 的**最長上升路徑**。  

## 解法

相似題 [354. russian doll envelopes]({% post_url 2022-05-25-leetcode-354-russian-doll-envelopes %})。  
相似題 [300. longest increasing subsequence]({% post_url 2022-04-19-leetcode-300-longest-increasing-subsequence %})。  

必選的 coordinates[k] 座標記做 (kx, ky)。  
為了保持遞增，能選的點必需在**左下**或是**右上**方。  
然後就變成左右兩邊各求一次**最長上升子序列 (LIS)** 了。  

時間複雜度 O(N log N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def maxPathLength(self, coordinates: List[List[int]], k: int) -> int:
        kx, ky = coordinates[k]
        left = [(x, y) for x, y in coordinates if x < kx and y < ky]
        right = [(x, y) for x, y in coordinates if x > kx and y > ky]

        return LIS(left) + 1 + LIS(right)

def LIS(nums):
    nums.sort(key=lambda x:(x[0], -x[1]))
    dp = []
    for _, y in nums:
        i = bisect_left(dp, y)
        if i == len(dp):
            dp.append(y)
        else: 
            dp[i] = y
    return len(dp)
```
