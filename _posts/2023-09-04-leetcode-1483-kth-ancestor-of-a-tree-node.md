---
layout      : single
title       : LeetCode 1483. Kth Ancestor of a Tree Node
tags        : LeetCode LeetCode Hard Array Tree BitManipulation BinaryLifting
---
最近很流行倍增，順便做一做。  

## 題目

輸入一個n節點的樹，節點編號分別為0到n-1，其中parent[i]代表節點i的父節點。  
根節點為0，找到給定節點node的第k個祖先。  

node的第k個祖先指的是node朝根節點走k步後的節點。  

實作以下類別：  

- TreeAncestor(int n, int[] parent)：建構樹的初始值  
- int getKthAncestor(int node, int k)：找到node的第k個祖先，若不存在則回傳-1  

## 解法

總共n個節點，最多只需要log n = m次跳躍就可以抵達目標節點。  

f[i][j]代表從節點i往上跳2^j步後的位置，先以parent初始化f[i][0]的值，然後從遍歷計算f[i][j]的值，其中1 <= j < m。  

每次查詢將k拆成數個2^j，從node開始逐次往上跳，若中途跳到-1則代表超出根節點，直接回傳。  

時間複雜度O(n log n + Q log n)。  
空間複雜度O(n log n)。  

```python
class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        global f,m
        m=n.bit_length()
        f=[[-1]*m for _ in range(n)]
        for i in range(1,n):
            f[i][0]=parent[i]
            
        for j in range(1,m):
            for i in range(n):
                fa=f[i][j-1]
                if fa!=-1:
                    f[i][j]=f[fa][j-1]
        
    def getKthAncestor(self, node: int, k: int) -> int:
        curr=node
        for j in range(m):
            if k&(1<<j):
                curr=f[curr][j]
            if curr==-1:
                return -1
        return curr
```
