--- 
layout      : single
title       : LeetCode 2579. Count Total Number of Colored Cells
tags        : LeetCode Medium Math
---
雙周賽99。拿小畫家畫一畫答案就出來了，頭一次這麼感謝小畫家。  

# 題目
有個無限大的二維網格，起初都是未著色的。 
輸入正整數n，接下來的n分鐘你必須執行以下動作：  
- 第1分鐘，將**任一**格子染成藍色  
- 之後的每分鐘，將與藍色格子相鄰的**所有**格子染成藍色  

![示意圖](https://assets.leetcode.com/uploads/2023/01/10/example-copy-2.png)  

求經過n分鐘後有多少**被染色的格子**。  

# 解法
第一分鐘是1，二分是5，三分是13，發現差值從4變成8，大膽假設第四分鐘的差值是12，也就是總數25。  
拿小畫家把第四圈點出來，還真的是12。直接暴力法算出來。  

時間複雜度O(n)。空間複雜度O(1)。  

```python
class Solution:
    def coloredCells(self, n: int) -> int:
        inc=4
        ans=1
        for i in range(n-1):
            ans+=inc
            inc+=4
            
        return ans
```
