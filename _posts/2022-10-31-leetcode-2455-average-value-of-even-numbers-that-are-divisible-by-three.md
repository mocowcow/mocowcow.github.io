--- 
layout      : single
title       : LeetCode 2455. Average Value of Even Numbers That Are Divisible by Three
tags        : LeetCode Easy Array
---
周賽317。

# 題目
輸入一個正整數陣列nums，回傳所有能被3整除的偶數的平均值。  

注意，平均值向下取整。  

# 解法
如果某數字模2餘0，則為偶數；模3餘0，可被3整除。同時滿足兩者就是模6於0。  

```python
class Solution:
    def averageValue(self, nums: List[int]) -> int:
        cnt=0
        tt=0
        for n in nums:
            if n%6==0:
                cnt+=1
                tt+=n
                
        if cnt==0:
            return 0
        return tt//cnt
```
