---
layout      : single
title       : LeetCode 3024. Type of Triangle II
tags        : LeetCode Easy Array Sorting HashTable
---
雙周賽123。很基本的題，但是我手殘貢獻了三個 WA，慚愧。  

## 題目

輸入長度為三的整數陣列 nums，試著組成三角形：  

- 若有三個邊等長，稱為 "equilateral"  
- 若有兩個邊等長，稱為 "isosceles"  
- 若三個邊都不等長，稱為 "scalene"  

判斷 nums 可以組成何種三角形。若無法組成三角形則回傳 "none"。  

## 解法

首先判斷三個邊是否能組成三角形：兩短邊長度和大於長邊。  
剩下的依照描述判斷即可。  

小技巧：像這種有夠長的字串千萬不要自己手打，直接複製題目比較安全。  

時間複雜度 O(1)。  
空間複雜度 O(1)。  

```python
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        a, b, c = nums
        if not (a + b > c):
            return "none"
        
        s = set(nums)
        if len(s) == 1:
            return "equilateral"
        
        if len(s) == 2:
            return "isosceles"
        
        # len(s) == 3
        return "scalene"
```

也可以不用集合，直接判斷邊長。  

```python
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        a, b, c = nums
        if not (a + b > c):
            return "none"
        
        if a == c:
            return "equilateral"
        
        if a == b or b == c:
            return "isosceles"
        
        # a != b and b != c
        return "scalene"
```
