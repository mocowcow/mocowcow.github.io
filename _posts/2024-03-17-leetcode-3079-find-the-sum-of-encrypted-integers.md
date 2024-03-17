---
layout      : single
title       : LeetCode 3079. Find the Sum of Encrypted Integers
tags        : LeetCode Easy Array String Simulation
---
雙周賽 126。

## 題目

輸入正整數陣列 nums。  
定義加密函數 encrypt(x)：將 x 中的所有數位都替換成 x 中的最大數位。  
例如：encrypt(523) = 555, encrypt(213) = 333。  

求 nums 中所有元素加密後的總和。  

## 解法

按照題意模擬。  
把元素轉成字串後，找到最大的字元，生成等長的字串後轉回整數即可。  

時間複雜度 O(N log L)，其中 L = max(len(nums[i]))。  
空間複雜度 O(log L)。  

```python
class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        
        def f(x):
            s = str(x)
            mx = max(s)
            s = mx * len(s)
            return int(s)
            
        return sum(f(x) for x in nums)
```

也可以個別拆出每個數位，這樣就不需要額外空間。  

時間複雜度 O(N log L)，其中 L = max(len(nums[i]))。  
空間複雜度 O(1)。

```python
class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        
        def f(x):
            size = 0
            mx = 0
            while x > 0:
                size += 1
                mx = max(mx, x % 10)
                x //= 10
            for _ in range(size):
                x = x * 10 + mx
            return x
            
        return sum(f(x) for x in nums)
```
