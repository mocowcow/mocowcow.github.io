---
layout      : single
title       : LeetCode 10032. Minimum Number of Operations to Make Array XOR Equal to K
tags        : LeetCode Array BitManipulation
---
雙周賽121。

## 題目

輸入整數陣列nums，以及正整數k。  

你可以執行以下操作任意次：  

- 選擇nums中的任一元素，並將其中一個**二進位位元**反轉。反轉指的是將0變1，或是反過來  

求**最少**需要幾次操作，才能使得nums中**所有**元素XOR後的結果等於k。  

注意：你也可以反轉前導零。例如0b101可以翻轉第四位，得到0b1101。  

## 解法

複習一下，XOR的特性是兩個1會相消變成0。  

先考慮只有一個位元的情形：  

- nums中有奇數個1，XOR結果=1  
- nums中有偶數個1，XOR結果=0  

因此，若k的對應位元與XOR結果不同，則需要一次反轉。  
同理套用到所有位元上。  

時間複雜度O(N)。  
空間複雜度O(1)。  

```python
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor=0
        for x in nums:
            xor^=x
            
        ans=0
        for i in range(20):
            b1=(xor>>i)&1
            b2=(k>>i)&1
            if b1!=b2:
                ans+=1
                
        return ans
```
