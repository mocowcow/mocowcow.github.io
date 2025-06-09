---
layout      : single
title       : LeetCode 3577. Count the Number of Computer Unlocking Permutations
tags        : LeetCode Medium Math
---
weekly contest 453。  
不知道是腦筋急轉彎，轉不太動。  

## 題目

<https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/description/>

## 解法

只有**編號更小**且**複雜度更小**的電腦才能解鎖其他電腦。  

講一大堆東西誤導，什麼以 0 當作 root，害我以為是樹狀結構，其實根本不是。  
根本**不用管是誰解鎖的**，只要 0 的複雜度比其餘電腦更低就可以完全解鎖。  
而且沒有解鎖順序限制，所以答案就是 0 以外的電腦**全排列**。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
MOD = 10 ** 9 + 7

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        N = len(complexity)
        for i in range(1, N):
            if complexity[0] >= complexity[i]:
                return 0

        return factorial(N-1) % MOD
```
