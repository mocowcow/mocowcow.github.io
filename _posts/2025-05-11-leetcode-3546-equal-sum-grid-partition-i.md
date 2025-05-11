---
layout      : single
title       : LeetCode 3546. Equal Sum Grid Partition I
tags        : LeetCode Medium
---
weekly contest 449。  
是個考察對稱性的好題。  
可惜我第一時間沒想到，但代碼也不長，無所謂。  

## 題目

<https://leetcode.com/problems/equal-sum-grid-partition-i/description/>

## 解法

水平 / 垂直切一刀，劃分成兩個**非空**的子矩陣。  

先討論水平切的情況：  
先遍歷一次，維護整個矩陣的和 down。  
由上至下將每列加入上半段的和 up，並同時減少下半段的和 down。  
若 up 等於 down 則找到答案。  

---

再來討論垂直切的情況：  
分割作法有**對稱性**，垂直切等價於**先將矩陣旋轉 90 度**後水平切。  
因此將分割邏輯封裝成函數 solve()，將矩陣旋轉後再次判斷即可。  

時間複雜度 O(MN)。  
空間複雜度 O(MN)。  

備註：下面實現比較偷懶，使用**轉置**。相當於右轉 90 度、再水平翻轉。  
但水平翻轉不影響答案，不翻回去也可以。  

```python
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        trans = [list(row) for row in zip(*grid)]
        return solve(grid) or solve(trans)


def solve(a):
    M, N = len(a), len(a[0])

    down = 0
    for row in a:
        for x in row:
            down += x

    up = 0
    for i in range(M-1):
        for j in range(N):
            x = a[i][j]
            up += x
            down -= x
        if up == down:
            return True
    return False
```
