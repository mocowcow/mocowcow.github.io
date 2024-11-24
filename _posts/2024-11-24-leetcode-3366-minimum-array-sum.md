---
layout      : single
title       : LeetCode 3366. Minimum Array Sum
tags        : LeetCode Medium DP
---
weekly contes 425。  

## 題目

輸入整數陣列 nums 還有三個整數 k, op1, op2。  

你可以對 nums 做以下操作：  

- 操作 1：選擇索引 i，將 nums[i] 除 2 向上取整。  
    總共至多只能做 op1 次，且每個索引至多 1 次。  
- 操作 2：選擇索引 i，將 nums[i] 減 k，但 nums[i] 必須大於等於 k。  
    總共至多只能做 op2 次，且每個索引至多 1 次。  

注意：同一個索引可以套用兩種操作，但只能至多各一次。  

求任意次操作後的**最小**元素和。  

## 解法

枚舉索引可以選擇要不要操作、做幾個。  
選擇不同，也可能會剩餘相同的索引以及操作次數，有**重疊的子問題**，考慮 dp。  

在剩餘操作次數足夠時，每個索引有以下方案：  

- 不操作。  
- 只操作 1。  
- 只操作 2。  
- 操作先 1 後 2。  
- 操作先 2 後 1。  

---

定義 dp(i, op1, op2)：nums[i..] 的元素中，在至多 op1 次操作 1、至多 op2 次操作 2 下，可能的最小元素和。  
轉移：dp(i, op1, op2) = min(五種方案)。  
base：當 op1 或 op2 小於 0，代表超過操作次數限制，不合法回傳 inf。當 i = N 時無剩餘元素，回傳 0。  

時間複雜度 O(N \* op1 \* op2)。  
空間複雜度 O(N \* op1 \* op2)。  

記憶化比較好寫，多加一個遞迴終止條件就好，不需要每次都檢查一堆條件。  

```python
class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        N = len(nums)

        @cache
        def dp(i, op1, op2):
            if op1 < 0 or op2 < 0: # invalid op
                return inf

            if i == N:
                return 0

            # no op
            x = nums[i]
            res = dp(i+1, op1, op2) + x

            # op1
            res = min(res, dp(i+1, op1-1, op2) + (x+1) // 2)

            # op2
            if x >= k:
                res = min(res, dp(i+1, op1, op2-1) + (x-k))

            # op1+2
            t = (x+1) // 2
            if t >= k:
                res = min(res, dp(i+1, op1-1, op2-1) + (t-k))

            # op2+1
            if x >= k:
                t = x-k
                res = min(res, dp(i+1, op1-1, op2-1) + (t+1) // 2)
            return res
        
        return dp(0, op1, op2)
```

寫成遞推，執行速度差不多，個人感覺可讀性變低。  

```python
class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        N = len(nums)

        # f[i][op1][op2]
        f = [[[0] * (op2+1) for _ in range(op1+1)] for _ in range(N+1)]

        for i in reversed(range(N)):
            x = nums[i]
            x2 = (x+1) // 2
            x2k = x2-k
            xk = x-k
            xk2 = (xk+1) // 2
            for o1 in range(op1+1):
                for o2 in range(op2+1):
                    res = f[i+1][o1][o2] + x
                    if o1 > 0:
                        res = min(res, f[i+1][o1-1][o2] + x2)
                    if o2 > 0 and xk >= 0:
                        res = min(res, f[i+1][o1][o2-1] + xk)
                    if o1 > 0 and o2 > 0:
                        if x2k >= 0:
                            res = min(res, f[i+1][o1-1][o2-1] + x2k)
                        if xk >= 0:
                            res = min(res, f[i+1][o1-1][o2-1] + xk2)
                    f[i][o1][o2] = res

        return f[0][op1][op2]
```
