--- 
layout      : single
title       : LeetCode 2718. Sum of Matrix After Queries
tags        : LeetCode Medium Array Matrix HashTable
---
周賽348。

# 題目
輸入整數n，和二維陣列queries，其中queries[i] = [type<sub>i</sub>, index<sub>i</sub>, val<sub>i</sub>]。  

有個初始值全部為0的n\*n矩陣。對於每次查詢，你必須按照以下規則：  
- 如果type<sub>i</sub>為0，則將第index<sub>i</sub>**列**全部設為val<sub>i</sub>  
- 如果type<sub>i</sub>為1，則將第index<sub>i</sub>**行**全部設為val<sub>i</sub>  

求執行完所有查詢後，矩陣的總和為多少。  

# 解法
同個位置可以被修改好幾次，我們只在乎最後一次被改的值是多少，所以倒序處理查詢。  

每次操作都是都是一整列或是整行，只要不是整行列都被蓋掉，那麼就有位置會被修改到。  
假設修改某列時，之後還會有x行被修改，則這次更新的值只有n-x個位置有效。  

因此在倒序處理的過程中，維護那些行列已經被處理過，記算出當次更新有多少位置被更新到，並加入答案。  

時間複雜度O(q)，其中q為查詢次數。  
空間複雜度O(n)。  

```python
class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        row=[False]*n
        col=[False]*n
        rcnt=ccnt=0
        ans=0
        
        for tp,idx,val in reversed(queries):
            if tp==0: # row
                if row[idx]:continue
                row[idx]=True
                rcnt+=1
                x=n-ccnt
                ans+=val*x
            else: # col
                if col[idx]:continue
                col[idx]=True
                ccnt+=1
                x=n-rcnt
                ans+=val*x
        
        return ans
```

可以直接使用集合來維護已經處理過的行列，還可以直接取得個數，一舉兩得。  
查詢type的0和1也剛好對應到列和行，把type XOR 1就可以行列互換。  

時間複雜度O(q)，其中q為查詢次數。  
查詢夠少的話，集合有時候裝沒多少東西，空間複雜度O(min(n,q))。  

```python
class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        vis=[set(),set()] # vis[0] for row, vis[1] for col
        ans=0
        
        for tp,idx,val in reversed(queries):
            if idx not in vis[tp]:
                vis[tp].add(idx)
                ans+=(n-len(vis[tp^1]))*val
        
        return ans
```