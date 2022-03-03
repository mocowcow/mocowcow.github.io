---
layout      : single
title       : LeetCode 1822. Sign of the Product of an Array
tags 		: LeetCode Easy Array Math
---
Study Plan - Programming Skills。  

# 題目
整數陣列nums，求nums中所有數相乘後結果為正負數或是0。  
正數回傳1，負數回傳-1，0則回傳0。

# 解法
只要管正負號就好，數值大小不重要。  
連續乘法中只要出現一次0，就永遠是0了，碰到0直接回傳0。  
若碰到負數則將目前符號反轉，正數就不管他。

```python
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sign = 1
        for n in nums:
            if n == 0:
                return 0
            if n < 0:
                sign *= -1

        return sign

```
