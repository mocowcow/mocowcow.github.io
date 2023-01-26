--- 
layout      : single
title       : LeetCode 2545. Sort the Students by Their Kth Score
tags        : LeetCode Medium Array Matrix Sorting
---
周賽329。

# 題目
一個班級裡面有m個學生，每個學生有n個科目考試。輸入m\*n的整數矩陣score，其中score[i][j]代表第i個學生考第j個科目的分數。  

另外還有整數k。你必須根據第k個科目的分數，由高到低來將矩陣排序。  

回傳排序後的矩陣。  

# 解法
很單純的排序題，只要會自訂排序就能過。  

將m個score[i]以score[i][k]遞減排序即可。  

時間複雜度O(m log m)。空間複雜度O(1)。  

```python
class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        score.sort(key=itemgetter(k),reverse=True)
        return score
```
