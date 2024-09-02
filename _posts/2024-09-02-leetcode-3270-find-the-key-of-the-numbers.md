---
layout      : single
title       : LeetCode 3270. Find the Key of the Numbers
tags        : LeetCode Easy String Simulation
---
biweekly contest 138。  

## 題目

輸入三個正整數 num1, num2 和 num3。  

num1, num2 和 num3 的**金鑰**是一個四位數：  

- 若任何數不滿四位，則添加前導零。  
- **金鑰**的第 i 位數字 (i <= i <= 4) 是 num1, num2 和 num3 中第 i 位數的最小值。  

求三個數的**金鑰**，不包含前導零。  

## 解法

看到討厭的前導零，先把三個數轉成字串再補零比較方便。  
字串中的第 i 位同樣能夠比較大小。找出答案轉回整數後回傳。  

時間複雜度 O(1)。  
空間複雜度 O(1)。  

```python
class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        a = [num1, num2, num3]
        a = [str(x).zfill(4) for x in a]
        ans = []
        for i in range(4):
            t = min(x[i] for x in a)
            ans.append(t)

        return int("".join(ans))
```

也可以不轉成字串，直接操作整數，達到真正意義上的 O(1) 空間。  

時間複雜度 O(1)。  
空間複雜度 O(1)。  

```python
class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        a = [num1, num2, num3]
        mult = 1
        ans = 0
        for _ in range(4):
            t = min(x // mult % 10 for x in a)
            ans += t * mult
            mult *= 10

        return ans
```
