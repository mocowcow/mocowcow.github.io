---
layout      : single
title       : LeetCode 2870. Minimum Number of Operations to Make Array Empty
tags        : LeetCode Medium Array Math Greedy HashTable
---
雙周賽114。總記得有寫過幾乎一樣的題，但是想不起來。  

## 題目

輸入正整數陣列nums。  

有兩種操作，你可以各執行**任意**次：  

- 選擇兩個**相同**的元素，並將其從陣列中刪除  
- 選擇三個**相同**的元素，並將其從陣列中刪除  

求使得陣列為空的**最少操作次數**，若不可能為空，則回傳-1。  

## 解法

首先統計每個元素的出現次數。  
分類討論元素x的出現次數：  

- 只出現1次，刪不掉，回傳-1  
- 出現2或3次，只需要一次操作  
- 4次以上，需要數次操作  

為使操作數最小，一次刪掉3個是較好的選擇。  
每次刪3個，最後餘數只可能有三種情形：  

- 餘0，剛好刪完
- 餘1，把其中一次刪3個改成刪2個，餘數會變成2  
- 餘2，再一次操作刪2個  

可以發現，只要不是餘0，都只需要在多一次操作。  
遍歷所有出現次數v，刪除這個元素共需要ceil(v/3)次操作。  

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        d=Counter(nums)
        ans=0
        for v in d.values():
            if v==1:
                return -1
            ans+=(v+3-1)//3

        return ans
```
