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
問題轉換成：  
> 每個元素有不同操作次數，每次選不同的兩個元素一起操作  

相似題 [1953. Maximum Number of Weeks for Which You Can Work](https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/description/)。  

敏銳的同學大概能猜到結論：  
設 S = sum(needs)，MX = max(needs)。  
因 needs 遞增，所以必定滿足 MX <= ceil(S / 2)，故肯定可以配對到另一個不同元素。  
共需操作 ceil(S / 2) 次。  

因此單次查詢答案 ceil(sum(need[l..r]) / 2)。  
將所有查詢答案加總即可。  

時間複雜度 O(Q log MX)，其中 MX = max(R)。  
空間複雜度 O(1)。  

```python
def f(n):
    # sum of need([1..n])
    tot = 0
    ops = 1
    p0, p = 1, 4  # [p0..p-1] divide "ops" times
    while p0 <= n:
        cnt = min(n, p-1) - p0 + 1
        tot += cnt * ops
        # next group
        p0, p = p, p*4
        ops += 1
    return tot


class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        ans = 0
        for l, r in queries:
            tot = f(r) - f(l-1)
            # make pair
            # ceil(tot / 2)
            ans += (tot+1) // 2

        return ans
```

最後加碼一個擴展思考題：  
測資原本保證 L < R，所以至少會有兩個不同的元素需要操作。  
所以 ceil(tot / 2) 是對的。  

那如果允許 L = R，且允許只選一個元素操作怎麼辦？  
例如 need([8..8]) = [3]，只會有一個元素。  
需要特判答案，答案即為所需操作次數。  
