---
layout      : single
title       : LeetCode 3495. Minimum Operations to Make Array Elements Zero
tags        : LeetCode Hard Math
---
weekly contes 442。  
滿經典的題，算是近來較簡單的 Q4。  
大概可以猜出答案，證明反而比較難想。  

## 題目

<https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/description/>

## 解法

每次查詢，對於區間 [l..r] 中的所有整數，每次操作可以選兩個分別**除 4**，最少需要幾次操作才能把全部變 0。  

---

先手玩看看，每個數需要除幾次才能變成 0：
> [1..3] 內，需要 1 次  
> [4..15] 內，需要 2 次  
> [16..63] 內，需要 3 次  
> ...

按照所需次數相同分組後，發現左右端點都和 4 的次方有關係。  
從 i = 0 起算，第 i 組的最小值為 4^i，最大值為 4^(i+1)-1。  

所需除法次數後，呈**遞增**，且任意兩個相鄰值的至多為 1。  
例如：  
> 整數區間 [l..r] = [2,3,4..,15,16]  
> 對應操作次數 need([l..r]) = [1,1,2,..,2,3]  

設 f(n) 為 [1..n] 的操作次數。  
根據**排容原理**，[l..r] 所需操作次數為 f(r) - f(l-1)。  

---

最後要從 need([l..r]) 中，每次選兩個一起操作。  

敏銳的同學大概能猜到結論：  
只要每次選剩餘次數最大和次大，就保證所有剩餘次數的差保持連續。  
sum(need[l..r]) 為偶數剛好配完；奇數會剩下 [0,..,0,1]，需要再除一次。  

因此單次查詢答案 ceil(sum(need[l..r]) / 2)。  
將所有查詢答案加總即可。  

時間複雜度 O(Q log MX)，其中 MX = max(R)。  
空間複雜度 O(1)。  

```python
def f(n):
    # sum of need([1..n])
    tot = 0
    ops = 1
    p0, p = 1, 4  # [p0..p-1] divide for "ops" times
    while p0 <= n:
        p1 = min(n, p-1)
        need = (p1 - p0 + 1) * ops
        tot += need
        # next group
        p0, p = p, p*4
        ops += 1
    return tot


class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        ans = 0
        for l, r in queries:
            ops = f(r) - f(l-1)
            # make pair
            # ceil up
            ans += (ops+1) // 2

        return ans
```
