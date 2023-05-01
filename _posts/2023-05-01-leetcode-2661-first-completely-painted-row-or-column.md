--- 
layout      : single
title       : LeetCode 2661. First Completely Painted Row or Column
tags        : LeetCode Medium Array Matrix HashTable Simulation Counting
---
周賽343。題目讀起來有點繞口，要翻譯還真不太好翻。  

# 題目
輸入整數陣列array，還有m\*n的整數矩陣mat。  
兩者都正好由[1, m\*n]之間的整數所組成。  

從arr的索引0開始，逐一將mat中編號為arr[i]的格子上色。  

求最小的索引i，滿足arr[i]對應的格子上色後，使某行或列的所有格子都被上色。  

# 解法
由於mat中的元素都是唯一的，可以直接以mat[r][c]的值為鍵，映射到(r,c)上。  
兩個陣列row和col紀錄個行列的上色次數。遍歷arr[i]，將對應到的行列次數加1，若使得某列達到N、或某行達到M次上色，則答案為i。  

時間複雜度O(MN)。  
空間複雜度O(MN)。  

```python
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        M,N=len(mat),len(mat[0])
        mp={}
        
        for r in range(M):
            for c in range(N):
                mp[mat[r][c]]=[r,c]
                
        row=[0]*M
        col=[0]*N
        
        for i,x in enumerate(arr):
            r,c=mp[x]
            row[r]+=1
            col[c]+=1
            if row[r]==N or col[c]==M:
                return i
```
