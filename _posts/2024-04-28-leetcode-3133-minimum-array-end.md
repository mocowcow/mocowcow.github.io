---
layout      : single
title       : LeetCode 3133. Minimum Array End
tags        : LeetCode Medium BitManipulation Greedy
---
周賽395。

## 題目

輸入兩個整數 n 和 x。  
你必須構造一個大小 n 的整數陣列 nums，對於每個 0 <= i < n - 1，滿足 nums[i + 1] 大於 nums[i]。  
且 nums 中所有元素做 AND 運算後的結果為 x。  

求 nums[n - 1] 可能的**最小值**。  

## 解法

首先複習 AND 運算的特性：**只少不多**。做越多次運算，越可能使結果值變小。  
題目要求 AND 的結果要是 x，所以 nums 中每個元素都必須擁有**和 x 同樣的位元**。  

同時，題目又要求 nums 呈**嚴格遞增**，又要求 nums 最後一個數越小越好。  
為使得最後一個數盡可能小，則每次**增量要盡可能小**。  

但考慮到 AND 的限制，有時候進位反而會把要保留的 1 位元弄不見，所以每次增量可能不同。  
例如：  
> n = 3, x = 2  
> nums = [2, 3, 6]  
  
---

先不管 AND 對於 1 位元的限制，考慮 x = 0 應該如何增量：  
> x = 0 = 0b000  
> 增量 1 得到 0b001  
> 增量 1 得到 0b010  
> 增量 1 得到 0b011  
> 增量 1 得到 0b100  

這時回到剛才的例子，被固定的 1 位元就以井號 # 代替，考慮如何增量：  
> x = 2 = 0b010 = 0b00_0  
> 增量 得到 0b00#1  
> 增量 得到 0b01#0  
> 增量 得到 0b01#1  
> 增量 得到 0b10#0  

發現只要忽略底線，實際上兩個例子變化順序是相同的。  

---

我們要求 x 開始的第 n 個數字，就需要從 x 開始增量 need = n - 1 次。  
以 need 的二進制表示，便是增量 n - 1 次的最終結果。  
將 need 二進制的各位元**從右到左**填入 x 二進制中為 0 的位置即可。  

例如：  
> n = 20, x = 10  
> x = 0b0000110
> 先忽略 x 中不可以修改的位置，x = 0b0000##0  
> need = n - 1 = 19 = 0b10011  
> 從右到左填入 need 的二進位位元  
> 0b1001##1  
> 答案 0b1001111 = 79

時間複雜度 O(log n + log x)。  
空間複雜度 O(1)。  

```python
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        need = n - 1
        i = 0
        ans = x
        while need > 0:
            # find next 0 bit from x
            while ans & (1 << i):
                i += 1
            # fill bit from bin(need)
            bit = need & 1
            if bit == 1:
                ans |= (1 << i)
            # next bit
            i += 1
            need >>= 1
            
        return ans
```
