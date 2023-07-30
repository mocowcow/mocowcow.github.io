--- 
layout      : single
title       : LeetCode 2798. Number of Employees Who Met the Target
tags        : LeetCode Easy Array Simulation
---
周賽356。佛心送分題。  

## 題目

公司有n個員工，編號分別從0\~n-1。每個員工i的工時為hours[i]。  

公司要求每個員工至少工作target小時。  

輸入長度n的非負整數陣列hours，以及整數target。  

求有多少員工至少工作target小時。  

## 解法

按照題意模擬。  

時間複雜度O(N)。  
空間複雜度O(1)。  

```python
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        ans=0
        for x in hours:
            if x>=target:
                ans+=1
                
        return ans
```

python一行版本。  

```python
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return sum(x>=target for x in hours)
```
