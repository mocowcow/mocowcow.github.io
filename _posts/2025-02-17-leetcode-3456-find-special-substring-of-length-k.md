---
layout      : single
title       : LeetCode 3456. Find Special Substring of Length K
tags        : LeetCode Easy Simulation
---
weekly contest 437。

## 題目

<https://leetcode.com/problems/find-special-substring-of-length-k/description/>

## 解法

暴力枚舉長度 k 的子字串，然後檢查子字串內是只有一種字元。  

時間複雜度 O(N^2)。  
空間複雜度 O(1)。  

```python
class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        N = len(s)
        for i in range(N-k+1):
            j = i + k - 1
            if len(set(s[i:j+1])) != 1:
                continue
                
            if i > 0 and s[i-1] == s[i]:
                continue

            if j + 1 < N and s[j+1] == s[i]:
                continue

            return True

        return False
```

要求子字串中只有一種字元，可以先分割子字串，將相同的字元視作同一組 (分組循環)。  
檢查是否有長度為 k 的組。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        N = len(s)
        i = 0
        while i < N:
            j = i
            while j+1 < N and s[j] == s[j+1]:
                j += 1
            if j-i+1 == k:
                return True
            i = j+1 

        return False
```

python 一行版本。  

```python
return any(len(list(g)) == k for _, g in groupby(s))
```
