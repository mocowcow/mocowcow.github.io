---
layout      : single
title       : LeetCode 3411. Maximum Subarray With Equal Products
tags        : LeetCode Easy Math
---
weekly contest 431。  
有點猛的 Q1，應該很多人不會算 lcm 就掛掉。  

## 題目

輸入正整數陣列 nums。  

若陣列 arr 滿足 prod(arr) == lcm(arr) * gcd(arr)，則稱為**乘積等價**的。  
其中：  

- prod(arr) 是 arr 所有元素的乘積。  
- gcd(arr) 是 arr 所有元素的最大公因數 (GCD)。  
- lcm(arr) 是 arr 所有元素的最小公倍數 (LCM)。  

求 nums **最長**的**乘積等價**子陣列。  

## 解法

python 真的是爽翻天，不只 gcd, lcm 有內建，竟然還有連乘 prod。  
暴力枚舉所有子陣列，比較三者的值即可。  

時間複雜度 O(N^3 log N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        N = len(nums)
        ans = 0
        for i in range(N):
            for j in range(i, N):
                sub = nums[i:j+1]
                if prod(sub) == gcd(*sub) * lcm(*sub):
                    ans = max(ans, j-i+1)

        return ans
```

注意到 gcd, lcm, prod 三種值都延續之前的計算結果。  
因此不需要每次都重算，只要在子陣列擴展右端點時與新元素計算。  

時間複雜度 O(N^2 log N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        N = len(nums)
        ans = 0
        for i in range(N):
            prod = _lcm = 1
            _gcd = 0
            for j in range(i, N):
                prod *= nums[j]
                _gcd = gcd(_gcd, nums[j])
                _lcm = lcm(_lcm, nums[j])
                if prod == _gcd * _lcm:
                    ans = max(ans, j-i+1)

        return ans
```
