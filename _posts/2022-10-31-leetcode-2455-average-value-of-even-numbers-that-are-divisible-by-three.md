--- 
layout      : single
title       : LeetCode 2455. Average Value of Even Numbers That Are Divisible by Three
tags        : LeetCode Easy Array
---
周賽317。範例是真的佛心，如果沒有特別給出0的狀況，我就要拿WA了。  

# 題目
輸入一個正整數陣列nums，回傳所有能被3整除的偶數的平均值。  

注意，平均值向下取整。  

# 解法
如果某數字模2餘0，則為偶數；模3餘0，可被3整除。同時滿足兩者就是模6於0。  

一次遍歷，時間複雜度O(N)，空間複雜度O(1)。  

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
