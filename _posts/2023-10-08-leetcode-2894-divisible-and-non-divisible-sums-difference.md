---
layout      : single
title       : LeetCode 2894. Divisible and Non-divisible Sums Difference
tags        : LeetCode Easy Math Simulation
---
周賽366。

## 題目

輸入正整數n和m。  

兩個整數num1和num2定義如下：  

- nums1：[1, n]中所有**不可**被m整除的元素總和  
- nums1：[1, n]中所有**可以**被m整除的元素總和  

求num2 - num2的值。  

## 解法

按照題意模擬。  

時間複雜度O(n)。  
空間複雜度O(1)。  

```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        n1=n2=0
        for x in range(1,n+1):
            if x%m!=0:
                n1+=x
            else:
                n2+=x
                
        return n1-n2
```

既然知道n的範圍，其實可以直接公式找答案。  
n裡面共有q = floor(n/m)個數可以被m整除，這個數列是：  
> 1m, 2m, ...,   qm  
> 把m提出來，就是sum(1, ..., q)\*m  
> num2的部分就是1\~q總和乘上m  
> num1的部分就是1\~n總和扣掉num2  

```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        q=n//m
        tot=n*(n+1)//2
        n2=q*(q+1)//2*m
        n1=tot-n2
        
        return n1-n2
```
