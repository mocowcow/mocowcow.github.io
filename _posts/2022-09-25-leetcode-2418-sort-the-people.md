--- 
layout      : single
title       : LeetCode 2418. Sort the People
tags        : LeetCode Easy Array Sorting HashTable
---
周賽312。

# 題目
輸入兩個長度為n的陣列names和heights，分別代表第i個人的姓名和身高，且每個人的身高是獨一無二的。  
將所有人以身高遞減順序排序後回傳。  

# 解法
先來個通用解法，將名字與身高編成配對後排序，再單獨拆出姓名。  

時空間複雜度O(n log n)。  

```python
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        a=sorted(zip(names,heights),key=lambda x:x[1],reverse=1)
        return [x[0] for x in a]
```

這題有個小提示，給還不會自訂排序的朋友一點幫助：身高是獨一無二的。  
這意味著可以用身高作為key值，映射到某個人身上。  
先以雜湊表建立身高對姓名的映射，將身高排序後，找回對應的姓名。  

時空間複雜度一樣O(n log n)。  

```python
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        N=len(names)
        mp={}
        for i in range(N):
            mp[heights[i]]=names[i]
            
        heights.sort(reverse=True)
        return [mp[x] for x in heights]
```
