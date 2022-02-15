---
layout      : single
title       : LeetCode 136. Single Number
tags 		: LeetCode Easy Array BitManipulation
---
每日題。連續兩天都是簡單題，真稀奇。

# 題目
輸入一個不為空的陣列整數nums，裡面除了只有一個數只出現一次外，其他都出現兩次，求只出現一次的數是多少。  
你必須使用空間O(1)的演算法。

# 解法
既然都說只能用常數空間，那就是指定XOR運算了。  
XOR有個特性，對同樣的數字做兩次運算會抵消，因此把整個nums的數相互做XOR就可以得到答案。  

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = 0
        for n in nums:
            x ^= n

        return x
```

寫成pythonic的風格。

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(operator.xor, nums)

```
