--- 
layout      : single
title       : LeetCode 2535. Difference Between Element Sum and Digit Sum of an Array
tags        : LeetCode Easy Array
---
周賽328。

# 題目
輸入正整數陣列nums：  
- **元素和**為nums中所有元素的總和   
- **數字和**為nums中出現的所有數字的和(可以重複)  

求nums中**元素和**與**數字和**的**絕對差**。  

# 解法
雖然說是絕對差，但其實元素和不可能小於數字和，所以只要拿元素和去扣掉每個數字就好。  

```python
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        ans=0
        
        for n in nums:
            ans+=n
            while n:
                ans-=n%10
                n//=10
                
        return ans
```
