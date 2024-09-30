---
layout      : single
title       : LeetCode 3304. Find the K-th Character in String Game I
tags        : LeetCode Easy Simulation
---
weekly contest 417。  

## 題目

Alice 和 Bob 在玩遊戲。最初 Alice 有一個字串 word = "a"。  

輸入正整數 k。  
Bob 要求 Alice 不斷執行以下操作：  

- 將 word 的每個字元**替換**成英文字母表中**下一個**來生成新字串，並將其**附加**至原始的 word。  

例如："c" 操作後得到 "cd"；zb" 操作後得到 "zbac"。  
注意：字元 'z' 替換後會變成 'a'。  

在執行足夠次的操作使得 word 擁有**至少** k 個字元，回傳 word 中第 k 個字元。  

## 解法

本題至多 k = 500，暴力生成字串即可。  
直接把字元轉來轉去很麻煩，先用整數 [0, 25] 對應字母，最後生成答案時再轉回字元。  

注意：題目指的第 k 個是從 1 開始數，轉換成索引需要減 1。  

時間複雜度 O(k)。  
空間複雜度 O(k)。  

```python
class Solution:
    def kthCharacter(self, k: int) -> str:
        a = [0]
        while len(a) < k:
            t = [(x+1)%26 for x in a]
            a += t

        return chr(97 + a[k-1])
```
