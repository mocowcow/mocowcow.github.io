--- 
layout      : single
title       : LeetCode 2536. Increment Submatrices by One
tags        : LeetCode Medium Array Matrix PrefixSum
---
周賽328。這題有點微妙，以前在Q2用了2D前綴和，後來才發現只需要暴力法，總覺得這次也要暴力。  
結果看到測資範圍發現不對，但又想不到什麼太好的方法，無法確定會不會TLE。  

# 題目
輸入正整數n，代表有一個n\*n的空矩陣mat。  

另外有個二維整數陣列qeury，對於每個query[i] = [row1<sub>i</sub>, col1<sub>i</sub>, row2<sub>i</sub>, col2<sub>i</sub>]，你必須：  
- 以(row1<sub>i</sub>, col1<sub>i</sub>)為左上角，(row2<sub>i</sub>, col2<sub>i</sub>)為右下角，將範圍內的**所有元素**加一。  

執行所有query後，回傳mat。  

# 解法
可以把矩陣看成n個列，每次query[i]分別處理row1<sub>i</sub>\~row2<sub>i</sub>，將(col1<sub>i</sub>, col2<sub>i</sub>)紀錄差分為1。  

執行完查詢之後，再對每個列分別做一次前綴和，得到正確的數值。  

```python
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat=[[0]*(n) for _ in range(n)]
        
        for r1,c1,r2,c2 in queries:
            for r in range(r1,r2+1):
                mat[r][c1]+=1
                if c2+1<n:
                    mat[r][c2+1]-=1
                    
        for r in range(n):
            for c in range(1,n):
                mat[r][c]+=mat[r][c-1]
                
        return mat
```
