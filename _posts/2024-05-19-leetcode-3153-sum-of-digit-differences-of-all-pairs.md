---
layout      : single
title       : LeetCode 3153. Sum of Digit Differences of All Pairs
tags        : LeetCode Medium Array String HashTable
---
周賽 398。大概是近來最簡單的 Q3。  

## 題目

輸入**正整數**陣列 nums，其中所有整數的**位數都相同**。  

**位數差**指的是兩個整數之間，**相同位置**擁有**不同數字**的個數。  

求 nums 中**所有數對**的**位數差**的**總和**。  

## 解法

仔細看看，數對中的數字都是相互獨立的，並不會互相影響。  
問題轉換成：求陣列中，由**不同元素**組成的數對有幾個。如果是 M 位數，就分別計算 M 次。  

先將 nums 中的元素成字串，並枚舉字串中第 pos 位的字元。  
對於索引 i 的字元 c 來說，可以與左方 i 個字元組成數對。若那 i 個中有 cnt 個字元是 c，則有 i - cnt 個不是 c。  

時間複雜度 O(MN)，其中 M = log nums[0]。  
空間複雜度 O(N)。  

```python
class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        a = [str(x) for x in nums]
        M = len(a[0])
        ans = 0
        for pos in range(M):
            d = Counter()
            for i, s in enumerate(a):
                c = s[pos]
                ans += i - d[c]
                d[c] += 1
                
        return ans
```
