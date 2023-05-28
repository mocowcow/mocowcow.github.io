--- 
layout      : single
title       : LeetCode 2710. Remove Trailing Zeros From a String
tags        : LeetCode Easy String Stack
---
周賽347。最近Q1就很良心，總算是沒有一些妖魔鬼怪。  

# 題目
輸入字串num，代表一個**正整數**。  
刪掉所有的尾隨零後回傳。  

# 解法
將字串轉成堆疊，只要頂端是"0"就不斷彈出。  

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        st=list(num)
        while st[-1]=="0":
            st.pop()
            
        return "".join(st)
```

python歡樂一行版本。  

```python
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return num.rstrip("0")
```