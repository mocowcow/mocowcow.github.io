---
layout      : single
title       : LeetCode 2980. Check if Bitwise OR Has Trailing Zeros
tags        : LeetCode Easy Array BitManipulation
---
周賽378。

## 題目

輸入正整數陣列nums。  

檢查是否能夠選擇**兩個或多個**元素做OR運算，並且運算結果的二進位表示中擁有**至少**一個尾隨零。  

例如數字5的二進位是"101"，沒有尾隨零；而數字4的二進位是"100"，有兩個尾隨零。  

若可以找到合法的組合則回傳true，否則回傳false。  

## 解法

OR的特性是1位元只增不減，選的元素越多，越有可能使1位元增加。  

只要選到一個奇數的元素，那個結果一定也會是奇數。  
反過來說，在只選偶數的情況下結果才會是偶數(有尾隨零)。  

題目要求至少兩個元素，直接檢查nums中的偶數是否有兩個以上即可。  

時間複雜度O(N)。  
空間複雜度O(1)。  

```python
class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        even=0
        for x in nums:
            if x%2==0:
                even+=1
                
        return even>=2
```
