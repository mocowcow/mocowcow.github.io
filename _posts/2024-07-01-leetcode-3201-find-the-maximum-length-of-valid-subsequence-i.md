---
layout      : single
title       : LeetCode 3201. Find the Maximum Length of Valid Subsequence I
tags        : LeetCode Medium Array DP
---
周賽 404。

## 題目

輸入整數陣列 nums。  

nums 的長度為 x 的**有效**子序列 sub 滿足：  

- (sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2  

求 nums 的**最長的有效子序列**。  

## 解法

觀察子序列中元素的關係：  
> (sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2  
> (sub[1] + sub[2]) % 2 == (sub[2] + sub[3]) % 2  

在模 2 的前提下，左右兩邊的 sub[1] 可以相消：  
> sub[0] % 2 == sub[2] % 2  
> sub[1] % 2 == sub[3] % 2  

也就是子序列中的偶數項必須同餘、奇數向也必須同餘。有兩種可能：  

- 0,1,0,1  
- 1,0,1,0  

但奇偶項的餘數也可以相同：  

- 0,0,0,0  
- 1,1,1,1  

分別處理以上四種情況即可。  

```python
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        nums = [x % 2 for x in nums]
        
        def f(parity):
            res = 0
            for x in nums:
                if x % 2 == parity:
                    res += 1
                    parity ^= 1
            return res
        
        
        return max(
            nums.count(0),
            nums.count(1),
            f(0),
            f(1)
        )
```
