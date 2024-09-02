---
layout      : single
title       : LeetCode 3273. Minimum Amount of Damage Dealt to Bob
tags        : LeetCode Hard Greedy Sorting
---
biweekly contest 138。非常妙的題，答案很好猜，但卻不好證明。  

## 題目

輸入整數 power 和兩個長度 n 的整數陣列 damage 和 health。  

Bob 有 n 個敵人，其中敵人 i 若存活 (health[i] > 0)，則每秒對 Bob 造成 damage[i] 傷害。  
在每秒敵人攻擊 Bob **後**，Bob 可以選擇其中**一個**活著的敵人，並對他造成 power 傷害。  

求 Bob 擊敗**所有**敵人時，**最少**需要承受幾點傷害。  

## 解法

對於多個敵人，必需連續**打同一個敵人**直到擊殺為止。因為分散攻擊只會使敵人的存活時間更長。  
敵人的實際存活時間是 ceil(health[i] / power)。  

再看測資範圍很大，光是維護存活的狀態就很麻煩，也不可能是 dp。  
那肯定有一種規則可以排序。  

---

若有兩個敵人，存活時間和攻擊分別是 t1, d1 和 t2, d2。  

- 方案一：先殺 1，受到的總傷害是 t1d1 + t1d2 + t2d2  
- 方案二：先殺 2，受到的總傷害是 t2d1 + t2d2 + t1d1  

若方案一優於方案二，則有：  
> t1d1 + t1d2 + t2d2 < t2d1 + t2d2 + t1d1  

整理後得到：  
> t1d2 < t2d1  

按照此公式可以決定兩者先殺誰好。  

---

假設還有第三個敵人 t3, d3。  
在先殺 1 最優的前提下，要決定再來殺誰。  

- 方案一：先 1 再 2 再 3，總傷害 t1d1 + t1d2 + t1d3 + t2d2 + t2d3 + t3d3  
- 方案二：先 1 再 3 再 2，總傷害 t1d1 + t1d2 + t1d3 + t3d2 + t3d3 + t2d2  

若方案一優於方案二，則有：  
> t1d1 + t1d2 + t1d3 + t2d2 + t2d3 + t3d3 < t1d1 + t1d2 + t1d3 + t3d2 + t3d3 + t2d2  

整理後得到：  
> t2d3 < t3d2  

發現只需要套相同公式比較敵人 2, 3，本質上就是**對所有敵人一起排序**。  

---

對於 python3 來說，sort 常用的 key function 只能接收單一元素，無法自定義比較兩個元素。  
因此需要額外維護排序函數，並透過 functools.cmp_to_key(func) 轉換成 key function。  

排序後，模擬受到的傷害值即可。  

時間複雜度 O(N log N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        a = []
        for d, h in zip(damage, health):
            t = (h + power - 1) // power
            a.append([t, d])

        def cmp(a, b):
            t1, d1 = a
            t2, d2 = b
            return t1 * d2 - t2 * d1  # t1 * d2 <  t2 * d1

        a.sort(key=cmp_to_key(cmp))
        tot = sum(damage)
        ans = 0
        for t, d in a:
            ans += tot * t
            tot -= d

        return ans
```

有些大膽的朋友會發現，比較公式可以移項：  
> t1d2 < t2d1  
> t1/d1 < d2/d2  

這樣不就可以使用 d/t 作為 key function？沒錯！  
正好本題測資範圍不夠大，不會有浮點數精度誤差。  

d/t 越大，代表著**傷害高、血又少**，應當優先處理。  

```python
class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        a = []
        for d, h in zip(damage, health):
            t = (h + power - 1) // power
            a.append([t, d])

        a.sort(key=lambda x:-x[1]/x[0])
        tot = sum(damage)
        ans = 0
        for t, d in a:
            ans += tot * t
            tot -= d

        return ans
```
