---
layout      : single
title       : LeetCode 3289. The Two Sneaky Numbers of Digitville
tags        : LeetCode Easy Simulation HashTable
---
weekly contest 415。  
讀題目本身比解題還難。  

## 題目

輸入長度 n 的陣列 nums，由 0 \~ n-1 的整數組成。  
每個整數都*只該出現一次，但有**某兩個整數出現兩次**。  

以任意順序回傳這兩個整數。  

## 解法

按照題意模擬。  
維護出現次數，出兩第二次就加入答案。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        s = set()
        ans = []
        for x in nums:
            if x in s:
                ans.append(x)
            else:
                s.add(x)

        return ans
```

歡樂一行版本。  

```python
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        return [k for k, v in Counter(nums).items() if v == 2]
```
