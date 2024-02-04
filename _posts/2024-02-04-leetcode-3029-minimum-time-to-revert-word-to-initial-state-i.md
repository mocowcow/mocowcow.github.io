---
layout      : single
title       : LeetCode 3029. Minimum Time to Revert Word to Initial State I
tags        : LeetCode Medium String
---
周賽383。

## 題目

輸入字串 word 和整數 k。  

每秒鐘，你必須執行以下操作：  

- 將 word 的前 k 個字元移除  
- 在 word 後方加入任意 k 個字元  

加入的字元和被刪除的字元不一定要相同。但是每秒鐘都得執行這兩個操作。  

求使得 word 回到**最初狀態**所需的**最小**時間，且時間不可為 0。  

## 解法

後方加入的可以是任意字元，以下以井字號 # 來表示。  

先從最簡單的情形 k = 1 來考慮，每次把左邊的一個字元刪掉：  
> word = "abcd"  
> 第一次操作 word = "bcd#"  
> 第二次操作 word = "cd##"  
> 第三次操作 word = "d###"  
> 第四次操作 word = "####"  

記得 # 可以填上任意字元，相當於萬用字元，若整個字串都變成 # 一定可以滿足要求。  
在上例中，也只能在第四字操作後才能滿足。  

既然 # 和其他字元匹配一定成功，那麼可以直接忽略他，只要匹配還沒被改變過的字元就好。  
相當於求**剩下的字串**是否為 word 的**前綴**。  

直接從 1 開始數，只要剩餘字串是前綴，答案就是當前操作次數。  
每次操作都會移除掉前方的 k 個字元，所以第 i 次操作，所剩下的字串相當於 word[i*k:]。  
空字串也是任何字串的前綴，保證一定有答案。  

時間複雜度 O(N^2)。  
空間複雜度 O(N)。  

```python
class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        for i in count(1):
            sub = word[k*i:]
            if sub == word[:len(sub)]:
                return i
```
