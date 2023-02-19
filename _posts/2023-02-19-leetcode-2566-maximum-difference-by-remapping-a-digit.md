--- 
layout      : single
title       : LeetCode 2566. Maximum Difference by Remapping a Digit
tags        : LeetCode Easy String Greedy
---
雙周賽98。本來想說題目裡面有個Danny Mittal到底是什麼鬼？原來是某次周賽的獎勵：前幾名參賽者ID可以出現在題目中。  

# 題目
輸入整數num。你可以將0\~9中任意一種數字替換成另一個數字。  

求替換後的可能**最大值**與**最小值**之間的差。  

注意：  
- 如果你將d1換成d2，則所有的d1都會變成d2  
- 數字可以被替換成相同的數字，也就是不變  
- 替換後的數字可能有前導零  

# 解法
測資範圍不大，直接依照題意，窮舉被新、舊數字，一邊更新最大、最小值。  

時間複雜度O(log N)，其中N為num的值。空間複雜度O(log N)。  

```python
class Solution:
    def minMaxDifference(self, num: int) -> int:
        mx=-inf
        mn=inf
        s=str(num)
        
        for old in "0123456789":
            for new in "0123456789":
                t=s.replace(old,new)
                n=int(t)
                mx=max(mx,n)
                mn=min(mn,n)
                
        return mx-mn
```

再來仔細想想，最大值只有可能是某個數字換成9，而最小值是某個數換成0。  
所以新的數字只會是0或9而已，壓縮到一個迴圈完成。  

```python
class Solution:
    def minMaxDifference(self, num: int) -> int:
        mx=-inf
        mn=inf
        s=str(num)
        
        for old in "0123456789":
            t=s.replace(old,"9")
            mx=max(mx,int(t))
            t=s.replace(old,"0")
            mn=min(mn,int(t))
                
        return mx-mn
```