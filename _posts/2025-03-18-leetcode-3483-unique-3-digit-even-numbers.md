---
layout      : single
title       : LeetCode 3483. Unique 3-Digit Even Numbers
tags        : LeetCode Easy Simulation Backtracking
---
biweekly contest 152。
有點囉嗦的暴力題。  

## 題目

<https://leetcode.com/problems/unique-3-digit-even-numbers/>

## 解法

從 digits 選三個數字，求能組能幾個**三位數的偶數**。  
且不可有前導零。  

直接暴力三層迴圈，枚舉三個不同索引 i, j, k 組成數字 val。  
判斷 val 是否為三位數 (至少 100) 且為偶數後，加入集合去重。  

時間複雜度 O(N^3)。  
空間複雜度 O(N^3)。  

```python
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        N = len(digits)
        s = set()
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                for k in range(N):
                    if i == k or j == k:
                        continue
                    val = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if val >= 100 and val % 2 == 0:
                        s.add(val)

        return len(s)
```

也可以用內建的排列函數枚舉。  

```python
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        s = set()
        for x, y, z in permutations(digits, 3):
            val = x * 100 + y * 10 + z
            if val >= 100 and val % 2 == 0:
                s.add(val)

        return len(s)
```

如果題目改成 k 位數的偶數，就需要使用到回溯。  
枚舉第 i 位數要選哪個，選完所有數字後判斷是否滿足條件。  

時間複雜度 O(N^k)。  
空間複雜度 O(N^k)。  

```python
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        N = len(digits)
        used = [False] * N
        s = set()

        k = 3

        def dfs(i, val):
            if i == k:
                if val % 2 == 0:
                    s.add(val)
                return
            for j in range(N):
                if i == 0 and digits[j] == 0:
                    continue
                if not used[j]:
                    used[j] = True
                    dfs(i+1, val * 10 + digits[j])
                    used[j] = False

        dfs(0, 0)

        return len(s)
```
