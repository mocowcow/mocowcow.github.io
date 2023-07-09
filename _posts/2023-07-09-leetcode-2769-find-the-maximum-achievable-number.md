--- 
layout      : single
title       : LeetCode 2769. Find the Maximum Achievable Number
tags        : LeetCode Easy Math
---
周賽353。這應該真的是全站最簡單的題目了。  
老實說我還想不太到第二種解法。  

# 題目
輸入兩個整數num和t。  

如果某個整數x，在經過t次操作後，可以變得和num相同，則稱為**可達的**。  
每次操作會：  
- 將x增加或減少1，然後也將num增加或減少1  

回傳最大的**可達的整數**。測資保證至少存在一個可達的整數。  

# 解法
既然要求x越大越好，那x一定是要大於num。  

每次操作，x要減1，num要加1，會在t次後相逢。  
也就是x - t = num + t，移項得到x = num + 2\*t。  

時間複雜度O(1)。  
空間複雜度O(1)。  

```python
class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num+t*2
```
