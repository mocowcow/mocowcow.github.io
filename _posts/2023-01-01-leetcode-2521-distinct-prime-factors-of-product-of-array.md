--- 
layout      : single
title       : LeetCode 2521. Distinct Prime Factors of Product of Array
tags        : LeetCode Medium Array Math
---
周賽326。又是質因數分解，跟前幾次周賽的東西差不多。  

# 題目
輸入正整數陣列nums，回傳nums所有元素乘積中共有多少**不同的質因數**。  

# 解法
雖說求整個陣列乘積的質因數，但其實拆開來算也是一樣的。  
直接對每個nums[i]做質因數分解，並將分解出的質因數加入集合中去重複。  

質因數分解為O(sqrt(num[i]))，整體時間複雜度O(N \* sqrt(max(nums)))。空間複雜度不會算，可能要去問數學大神。  

```python
class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        ans=set()
        for n in nums:
            x=n
            div=2
            while div*div<=x:
                while x%div==0:
                    ans.add(div)
                    x//=div
                div+=1
            if x>1:
                ans.add(x)

        return len(ans)
```
