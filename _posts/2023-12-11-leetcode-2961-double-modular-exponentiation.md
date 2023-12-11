---
layout      : single
title       : LeetCode 2961. Double Modular Exponentiation
tags        : LeetCode Medium Array Simulation
---
周賽375。

## 題目

輸入二維整數陣列variables，其中variables[i] = [a<sub>i</sub>, b<sub>i</sub>, c<sub>i</sub>, m<sub>i</sub>]。  
還有整數target。  

如果索引i滿足以下條件，則稱為**好的**：  

- 0 <= i < variables.length
- ((aibi % 10)ci) % mi == target  

回傳一個陣列，依序包含所有**好的索引**。  

## 解法

一樣模擬題意，就算不用快速冪也能過。  

時間複雜度O(N \* (b+c))。  
空間複雜度O(1)。  

```python
class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        ans=[]
        for i,(a,b,c,m) in enumerate(variables):
            # ab = (a^b) % 10
            ab=1
            for _ in range(b):
                ab=ab*a%10
                
            # x = (ab^c) % m
            x=1
            for _ in range(c):
                x=x*ab%m
            
            if x==target:
                ans.append(i)
                
        return ans
```

python自帶的快速冪是真的方便。  

時間複雜度O(N \* log (b+c))。  
空間複雜度O(1)。  

```python
class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        ans=[]
        for i,(a,b,c,m) in enumerate(variables):
            # ab = (a^b) % 10
            ab=pow(a,b,10)
                
            # x = (ab^c) % m
            x=pow(ab,c,m)
            
            if x==target:
                ans.append(i)
                
        return ans
```
