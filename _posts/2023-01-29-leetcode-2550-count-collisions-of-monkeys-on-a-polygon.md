--- 
layout      : single
title       : LeetCode 2550. Count Collisions of Monkeys on a Polygon
tags        : LeetCode Medium Math
---
周賽330。雖然我有做出來，但這題放在Q2是真的過分，而且描述/答案似乎也有點問題，不知道會不會rejudge。  

# 題目
有一個擁有n個頂點的多邊形，頂點由順時鐘方向分別記為為0\~n-1，且每個頂點上都有**正好一隻猴子**。  

下為6頂點的示意圖：  
![示意圖](https://assets.leetcode.com/uploads/2023/01/22/hexagon.jpg)  

每個猴子會同時向相鄰的頂點移動，對於頂點i來說，其相鄰頂點可以是：  
- (i + 1) % n，也就是順時鐘方向  
- 或是(i - 1 + n) % n，也就是逆時鐘方向  

移動之後，如果有至少兩隻猴子停在同一個頂點上，則代表發生**衝突**。  

求有多少移動方式擁有**至少一次衝突**。答案很大，模10^9+7後回傳。  

注意：每個猴子只能移動一次。  

# 解法
看了好幾次大神講題解，最受用的一句話叫做：**正難則反**。  

猴子有10^9隻，要窮舉出全部的移動方式總共是2^(10^9)，根本不可能。但是不會衝突的方式只有兩種：**全順時鐘**或是**全逆時鐘**。  
所有移動方式 = 有衝突 + 沒衝突，那麼只要求出總數扣掉2後再求一次餘數就是答案。  

第二個考點在於如何計算2^(10^9)？使用快速冪將次方運算降低到log n。  

時間複雜度O(log n)。空間複雜度O(1)。  

```python
class Solution:
    def monkeyMove(self, n: int) -> int:
        MOD=10**9+7
        tot=pow(2,n,MOD)
        return (tot-2)%MOD
```

自己手寫快速冪。  

```python
class Solution:
    def monkeyMove(self, n: int) -> int:
        MOD=10**9+7
        
        tot=1
        base=2
        exp=n
        while exp>0:
            if exp&1:
                tot=(tot*base)%MOD
            exp//=2
            base=(base*base)%MOD

        return (tot-2)%MOD
```