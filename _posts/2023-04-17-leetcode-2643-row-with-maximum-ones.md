--- 
layout      : single
title       : LeetCode 2643. Row With Maximum Ones
tags        : LeetCode Easy Array Matrix Simulation
---
周賽341。答案初始值設錯吃一個WA，連自己都覺得很瞎。  

# 題目
輸入m\*n的二進位矩陣mat，找到出現**最多1**的列號，以及出現次數。  

如果有多個列出現1的次數相同，則選擇列號較小的。  

# 解法
依照題意，算每列的1有幾個，如果比之前還多就更新答案的列號和1出現次數。  

時間複雜度O(MN)。空間複雜度O(1)。  

```python
class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        mx_row=0
        mx_cnt=0
        
        for i,row in enumerate(mat):
            cnt=sum(row)
            if cnt>mx_cnt:
                mx_cnt=cnt
                mx_row=i
                
        return [mx_row,mx_cnt]
```
