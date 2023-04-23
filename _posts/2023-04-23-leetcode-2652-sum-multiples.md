--- 
layout      : single
title       : LeetCode 2652. Sum Multiples
tags        : LeetCode Easy Array
---
周賽342。

# 題目
輸入正整數n，找到閉區間[1,n]之間有哪些整數可以被3,5或7整除。  

回傳所有可被整除整數的**總和**。  


# 解法
遍歷所有數i，暴力嘗試是否能被3,5,7任一整除。若可整除則將i加入答案。  

時間複雜度O(N)。空間複雜度O(1)。  

```python
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        
        def ok(x):
            for div in [3,5,7]:
                if x%div==0:
                    return True
            return False
            
        ans=0
        for i in range(1,n+1):
            if ok(i):
                ans+=i
                
        return ans
```

歡樂一行版本。  

```python
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        return sum(i for i in range(1,n+1) if any(i%div==0 for div in [3,5,7]))
```