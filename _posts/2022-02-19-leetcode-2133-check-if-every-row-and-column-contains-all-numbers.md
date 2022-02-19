---
layout      : single
title       : LeetCode 2133. Check if Every Row and Column Contains All Numbers
tags 		: LeetCode Easy Array HashTable Matrix
---
模擬周賽275。

# 題目
輸入N*N的矩陣matrix。檢查是否每行每列都有出現所有1~N的整數。

# 解法
循規蹈矩的解。  
對每行每列分別建立set，遍歷matrix中元素同時加入各行列set，最後檢查所有set大小是否為N，否則回傳false。

```python
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        N = len(matrix)
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]

        for r in range(N):
            for c in range(N):
                rows[r].add(matrix[r][c])
                cols[c].add(matrix[r][c])

        for i in range(N):
            if len(rows[i]) != N:
                return False
            if len(cols[i]) != N:
                return False

        return True
```

之後才想到利用python內建的zip解法。  
zip函數可以把M個物件打包成一個長度M的陣列，使用zip(*obj)則可以將其解包還原。  
若對一個矩陣解包，則會等價於向右旋轉90度。

```python
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        N = len(matrix)
        for r in matrix:
            if len(set(r)) != N:
                return False

        for r in zip(*matrix):
            if len(set(r)) != N:
                return False

        return True
```