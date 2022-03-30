---
layout      : single
title       : LeetCode 74. Search a 2D Matrix
tags 		: LeetCode Medium BinarySearch Matrix Array
---
每日題。普通二分搜的小變化題，要把矩陣攤平或是直接搜都很好玩。

# 題目
輸入M*N的矩陣matrix，每列的數由小到大排序，且每列的第一個數字小於上一列的最後一個數字。

# 解法
python偷懶解法可以直接用sum函數把矩陣攤平成一維。  

M\*N的矩陣可以看成長度為M\*N的一維陣列，第一個元素索引0，最後一個元素索引M*N-1，可以透過index/N和index%N計算出對應的行列，就將問題化簡為普通的二分搜了。

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M,N=len(matrix),len(matrix[0])
        lo=0
        hi=M*N-1
        while lo<=hi:
            mid=(lo+hi)//2
            n=matrix[mid//N][mid%N]
            if n==target:
                return True
            elif n>target:
                hi=mid-1
            else:
                lo=mid+1
                
        return False
```

