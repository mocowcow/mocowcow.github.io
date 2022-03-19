---
layout      : single
title       : LeetCode 48. Rotate Image
tags 		: LeetCode Medium Matrix Math
---
學習計畫裡面的。翻來翻去超麻煩。

# 題目
輸入N*N矩陣matrix，將其向右旋轉90度。必須使用原地演算法直接在輸入中修改，不須回傳。

# 解法
要直接實現向右轉太麻煩了，把它拆成兩步驟吧。  
向右轉90度 等價於 (轉置+水平翻轉)。  

順帶一題：向左轉90度 等價於 (水平翻轉+轉置)。

數學真偉大。

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N=len(matrix)
        
        #transpose
        for i in range(N):
            for j in range(i,N):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        
        #reverse
        for i in range(N):
            l=0
            r=N-1
            while l<r:
                matrix[i][l],matrix[i][r]=matrix[i][r],matrix[i][l]
                l+=1
                r-=1
```

