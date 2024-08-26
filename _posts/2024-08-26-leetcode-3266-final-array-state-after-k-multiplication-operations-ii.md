---
layout      : single
title       : LeetCode 3266. Final Array State After K Multiplication Operations II
tags        : LeetCode Hard Simulation Heap
---
weekly contest 412。  

## 題目

輸入整數陣列 nums，還整數 k 和 multiplier。  

你需對 nums 執行 k 次操作。每次操作：  

- 找到 nums 中的最小值 x。若存在多個，則選最先出現者。  
- 將 x 替換成 x \* multiplier。  

執行完 k 次操作後，將 nums 中每個元素模 10^9 + 7 後回傳。  

## 解法

Q1 加強版，k 高達 1e9，暴力模擬肯定會超時。  
這也暗示著應該存在某種規律，可以求出每個 nums[i] 需要操作幾次。  

---

以下簡稱 multiplier 為 mult。  
首先過濾掉最特殊的例子：k=1，不管操作幾次都沒差，直接回傳 nums。  

先考慮最簡單的情況，nums 只由一種元素組成：  
> nums = [1,1,1], k = 8, mult = 10  
> 第 1\~3 次操作 i = 0,1,2  
> 變成 nums = [10,10,10]  
> 第 4\~6 次操作 i = 0,1,2  
> 變成 nums = [100,100,100]  
> 第 7,8 次操作 i = 0,1  
> 變成 nums = [1000,1000,100]  

不難看出會由左到右**循環**，每個位置都會操作 k/N 次。無法整除時，前 k%N 個會多操作一次。  
若元素不同呢？  
> nums = [1,11,111], k = 8, mult = 10  
> 第 1 次操作 i = 0  
> 變成 nums = [10,11,111]  
> 第 2\~3 次操作 i = 0,1  
> 變成 nums = [100,110,111]  
> 第 4\~6 次操作 i = 0,1,2  
> 變成 nums = [1000,1100,1110]  
> 第 7\~8 次操作 i = 0,1  
> 變成 nums = [10000,11000,1110]  

前面幾次會先按照最小的開始操作，直到 nums 的**最小元素操作後**會大於**最大元素**為止。  
剩餘操作都按照固定順序**循環**。  

---

綜上，我們需要找到 nums 的初始最大值 mx，並把所有 nums[i] 調整到非常接近 mx、但不超過的狀態。  
最後平分給每個位置即可。  

```python
MOD = 10 ** 9 + 7
class Solution:
    def getFinalState(self, nums: List[int], k: int, mult: int) -> List[int]:
        if mult == 1:
            return nums

        N = len(nums)
        mx = max(nums)
        h = []
        for i, x in enumerate(nums):
            heappush(h, [x, i])

        while k > 0 and h[0][0] * mult <= mx:
            k -= 1
            t = heappop(h)
            t[0] *= mult
            heappush(h, t)

        h.sort()
        q, r = divmod(k, N)
        for cnt, (val, i) in enumerate(h):
            if cnt < r: # one more operation
                val *= mult
            val *= pow(mult, q, MOD)
            nums[i] = val % MOD

        return nums
```
