---
layout      : single
title       : LeetCode 2829. Determine the Minimum Sum of a k-avoiding Array
tags        : LeetCode Medium Math HashTable
---
周賽359。這個k-avoiding還真不好翻譯，中文站也沒翻。  

## 題目

輸入整數n和k。  

如果一個由**不同**正整數組成的陣列，不存在任何數對總和為k，則稱為**免k**陣列。  

求長度n的免k陣列的**最小總和**。  

## 解法

k只能由兩個正整數組成，那這兩個數i, j一定小於k。  

假設k=5，有兩種解法：  
> 1 + 4
> 2 + 3  

為了避免k，只能選擇其中一個。而為了想要總和小，則應當選擇較小者、拋棄較大者。  
我們由大到小遍歷整數，並檢查i=k-t是否已經選過。  

時間複雜度O(n)。  
空間複雜度O(n)。  

```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        s=set()
        i=1
        while len(s)<n:
            if k-i not in s:
                s.add(i)
            i+=1
            
        return sum(s)
```

應該還有數學公式解，過幾天再來補。  
