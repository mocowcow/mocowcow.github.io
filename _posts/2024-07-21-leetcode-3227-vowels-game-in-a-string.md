---
layout      : single
title       : LeetCode 3227. Vowels Game in a String
tags        : LeetCode Medium String
---
weekly contest 407。其實比較像腦筋急轉彎。  

## 題目

Alice 和 Bob 在玩字串遊戲。  

輸入字串 s。從 **Alice 先手**，兩人輪流按照以下規則行動：  

- Alice 必須從 s 中刪除一個包含**奇數**個母音的子字串  
- Bob 必須從 s 中刪除一個包含**偶數**個母音的子字串  

當某一方無法行動就算敗北。  

在兩人都做出最優行動的前提之下，若 Alice 能獲勝則回傳 true，否則回傳 false。  

## 解法

其實刪除子陣列還是子序列根本無所謂，重點只在於剩下**幾個母音**。  

分類討論母音個數 cnt 的兩種情況：  

- cnt 是奇數，Alice 可以全拿，下一回 Bob 就輸了  
- cnt 是偶數，Alice 可以拿到剩 1 個，下一回 Bob 也輸了  

好像 Alice 優勢很大，隨便玩都贏。  
但別忘記最初可能半個母音都沒有，那 Alice 開場直接輸。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return sum(c in "aeiou" for c in s) > 0
```
