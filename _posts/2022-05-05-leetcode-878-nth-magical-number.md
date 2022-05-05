--- 
layout      : single
title       : LeetCode 878. Nth Magical Number
tags        : LeetCode Hard Math BinarySearch
---
二分搜的經典題，等到最後一天才驚覺沒有被收錄，只好自己來寫一次。

# 題目
**魔法數字**指的是某個能被a,b整除的整數。  
輸入整數n,a,b，求第n個魔法數字。

# 解法
寫一個函數countMagic(x)，計算到x為止有幾個魔法數字，用來二分搜。  
數字最小從1開始，下界定為1。上界應該是b和a較小者乘上N最大值，反正不會超過10^14。如果mid不足n個魔法數字，則更新下界為mid+1；否則更新上界為mid。  

countMagic(x)要使用排容原理計算，x之中，有(x/a)個可以產生一堆由a產生的魔法數字，還有(x/b)個由b產生的魔法數字。但有些魔法數字可以同時被a和b整除，會重複計算到，所以要扣掉(x/a和b的最小公倍數)。    

![示意圖](/assets/img/878-1.jpg)

```python
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        # precompute
        gcd=math.gcd(a,b)
        lcm=a*b//gcd
        
        def countMagic(x):
            return x//a+x//b-x//lcm
        
        lo=1
        hi=10**14
        while lo<hi:
            mid=(lo+hi)//2
            if countMagic(mid)<n:
                lo=mid+1
            else:
                hi=mid
                
        return lo%(10**9+7)
```
