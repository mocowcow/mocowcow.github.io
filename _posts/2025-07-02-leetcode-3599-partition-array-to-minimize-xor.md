---
layout      : single
title       : LeetCode 3599. Partition Array to Minimize XOR
tags        : LeetCode Medium BitManipulation DP
---
weekly contest 456。
又又是複雜度妙妙屋，這次還突破運行時間紀錄。  

## 題目

<https://leetcode.com/problems/partition-array-to-minimize-xor/description/>

## 解法

題目本身很單純，枚舉子陣列劃分成 k 段的方式。  
不同的劃分方式可能剩餘相同的部分，有重疊的子問題，考慮 dp。  

定義 dp(i, rem)：把 nums[i..] 劃分成 rem 個子陣列的**最大**的 **子陣列 xor 最小值**。  
枚舉子陣列右端點 j，以 nums[i..j] 的 xor 和 dp(j+1, rem-1) 更新答案。  

時間複雜度 O(N^2 \* k)。  
空間複雜度 O(Nk)。  

N 和 k 上限高達 250，粗估計算輛 1e7 左右，而且還一堆 max/min，感覺很容易超時。  
反正交出去是過了，但是整整跑了 22000 ms，還為我網路炸了。  

---

備註：python 遞推反而變慢會超時；  
但是記憶化搭配手寫 min/max 大概可以降到 18000 ms 左右。  

然後 go 遞推只要 200 ms。  

```python
class Solution:
    def minXor(self, nums: List[int], k: int) -> int:
        N = len(nums)

        @cache
        def dp(i, rem):
            if i == N and rem == 0:
                return 0 
            if i == N or rem == 0:
                return inf
            res = inf
            xor = 0
            for j in range(i, N):
                xor ^= nums[j]
                res = min(res, max(xor, dp(j+1, rem-1)))
            return res

        return dp(0, k)
```
