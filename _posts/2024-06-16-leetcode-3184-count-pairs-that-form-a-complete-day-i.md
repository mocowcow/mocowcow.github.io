---
layout      : single
title       : LeetCode 3184. Count Pairs That Form a Complete Day I
tags        : LeetCode Easy HashTable
---
周賽 402。two sum 的變形題。  

## 題目

輸入整數陣列 hours，代表以**小時**為單位的時間。  
回傳一個整數，代表滿足 i < j 且 hours[i] + hours[j] 可構成**整天**的數對數目。  

**整天**指的是 24 小時的整數倍數。  
例如一天 24 小時、兩天 48小時、三天 72小時，以此類推。  

## 解法

我們要找兩個數 x, y 滿足 x + y 是 24 的倍數。  

假設 x + y = 24，則 (x + 24) + y 或 (x + 48) + y 肯定也是 24 的倍數。  
滿 24 的部分不影響答案，先對 x 對 24 求餘數，之後求 y = 24 - x，找先前出現過幾個 y。  

注意：若 x 本身就是 24 的倍數，則餘數會是 0，使得 y = 24 - 0 = 24。所以得對 y 再取一次餘數才不會越界。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        cnt = [0] * 24
        ans = 0
        for x in hours:
            y = (24 - x) % 24
            ans += cnt[y]
            cnt[x % 24] += 1
            
        return ans
```
