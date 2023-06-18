--- 
layout      : single
title       : LeetCode 2739. Total Distance Traveled
tags        : LeetCode Easy Simulation Math
---
周賽350。

# 題目
有一台雙油箱的卡車。  
輸入整數mainTank和additionalTank，分別代表主副油箱的油量。  

每單位的油可以讓卡車跑10公里。每當主油箱消耗了5單位油，且副油箱至少還有1單位油，則副油箱會將1單位的油加入主油箱。  

求卡車最多可以行駛多遠。  

# 解法
直接按照題目模擬，消耗滿5就試著從副油箱加油。  

時間複雜度O(N)。  
空間複雜度O(1)。  

```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        used=0
        while mainTank>0:
            mainTank-=1
            used+=1
            if additionalTank>0 and used%5==0:
                additionalTank-=1
                mainTank+=1
                
        return ans*10
```

還是數學解比較厲害，可能很多人都想公式就BUG了。  

每加5油會退1，實際上就是每加4油可以從副油箱加1。  
但如果mainTank剛好是4個倍數，則最後一次會湊不到5，根本沒辦法退錢。  
所以可以從副油箱得到的油量=(mainTank-1)/4。  

時間複雜度O(1)。  
空間複雜度O(1)。  

```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        add=min(additionalTank,(mainTank-1)//4)
        return (mainTank+add)*10
```