---
layout      : single
title       : LeetCode 2932. Maximum Strong Pair XOR I
tags        : LeetCode Easy Array Simulation BitManipulation Trie TwoPointers SlidingWindow
---
周賽371。同時是Q1也是Q4。  
其實我感覺這題有點微妙，怎麼會有將近700人通過。  
畢竟中國站在11/4號的每日題就是這次的原題，答案稍微改一下就可以了。  

更扯的是js和C#能用O(N^2)過Q4，真的是很鳥。  

## 題目

輸入整數陣列nums。一個整數數對x和y若滿足以下條件，則稱為**強壯的**：  

- |x - y| <= min(x, y)  

你必須從nums中選擇兩個整數組成**強壯的數對**，且他們的XOR值是所有**強壯數對**中的最大值。  
求所有強壯數對中的XOR最大值。  

注意：你可以選擇同一個整數兩次來組成數對。  

## 解法

一樣先來個暴力解。  
時間複雜度O(N^2)。  
空間複雜度O(1)。  

```python
class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        ans=0
        for x in nums:
            for y in nums:
                if abs(x-y)<=min(x,y):
                    ans=max(ans,x^y)
                    
        return ans
```
