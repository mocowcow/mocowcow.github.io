--- 
layout      : single
title       : LeetCode 2447. Number of Subarrays With GCD Equal to K
tags        : LeetCode Medium Array Math Greedy
---
周賽316。滑動窗口寫錯拿個WA，真的畫蛇添足。  

# 題目
輸入整數陣列nums和整數k，回傳nums子陣列中有幾個陣列gcd為k。  

# 解法
陣列長度才1000而已，直接暴力法窮舉每個子陣列，當gcd正好為k時答案加一；gcg小於k，之後不可能合法，直接跳出迴圈。  

時間複雜度O(N^2)，空間複雜度O(1)。  

```python
class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        N=len(nums)
        ans=0
        
        for i in range(N):
            x=0
            for j in range(i,N):
                x=gcd(x,nums[j])
                if x==k:
                    ans+=1
                elif x<k:
                    break
            
        return ans
```
