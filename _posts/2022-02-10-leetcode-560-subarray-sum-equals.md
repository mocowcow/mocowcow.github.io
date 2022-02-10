---
layout      : single
title       : LeetCode 560. Subarray Sum Equals
tags 		: LeetCode Medium HashTable PrefixSum
---
[相似題目Contiguous Array](https://leetcode.com/problems/contiguous-array/)。

# 題目
輸入一個整數陣列nums，及整數k，找出有幾個子陣列合為k。

# 解法
只求數量不求位置，直接使用雜湊表以子陣列長度紀錄數量。  
初始化長度0的子陣列為一個，維護一個變數psum做前綴和，一路往右加總。每次檢查左側是否有psum-k值的子陣列，若有則加入答案，最後將psum長度計數+1。

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ctr = Counter()
        ctr[0] += 1
        ans = psum = 0
        for n in nums:
            psum += n
            if psum-k in ctr:
                ans += ctr[psum-k]
            ctr[psum] += 1

        return ans
```
