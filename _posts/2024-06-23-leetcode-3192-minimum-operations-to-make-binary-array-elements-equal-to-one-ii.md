---
layout      : single
title       : LeetCode 3192. Minimum Operations to Make Binary Array Elements Equal to One II
tags        : LeetCode Medium Array Greedy PrefixSum
---
雙周賽 133。大概是史上最搞笑 Q3，丟給 GPT 馬上解決，將近兩萬人通過。  

## 題目

輸入二進位整數陣列 nums。  

你可以執行以下操作任意次：  

- 選擇索引 i，並將 i 到陣列末端的所有元素反轉  

反轉指把 0 變成 1，或是把 1 變成 0。  

求**最少**需要幾次操作，才能使得所有元素變成 1。  

## 解法

一樣從左往右遍歷每個 nums[i]，每次反轉都會使得後方所有元素也被反轉一次。  
因此維護總反轉次數的前綴和，就知道當前元素總共被反轉幾次。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        f = 0
        ans = 0
        for x in nums:
            if x ^ f == 0:
                ans += 1
                f ^= 1
                
        return ans
```
