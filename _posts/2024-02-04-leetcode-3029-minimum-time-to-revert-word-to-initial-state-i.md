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

接下來 Q4 有更大的數據範圍，word 長度高達 N = 10^5，暴力法肯定不能過。  
才怪！O(N^2) 丟出去直接過。難怪這麼偏門的題有幾千人通過，原來是多虧了爛測資。

正確方法應該是 z-function，很久以前碰過一次，當時也花了不少時間理解。  
相似題 [2223. sum of scores of built strings]({% post_url 2022-04-05-leetcode-2223-sum-of-scores-of-built-strings %})。  

簡單講，這演算法會對字串 s 算出相同長度的陣列 z。  
其中 z[i] 代表 s 和子字串 s[i:] 的**最長共通前綴兼後綴 (LPS)**。  
而對於本題來說，如果 z[i] 的值等於 word[i:] 的長度，即代表**剩下的字串**等於 word 的**前綴**，也就是滿足題目的要求。  

同樣從 1 開始枚舉操作次數，計算出剩下的字串起點 i = i*k，以及其長度 N - i。
如果 word 整個被改變過或是找到前綴，則回傳答案。  

```python
class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        N = len(word)
        z = z_function(word)
        for ops in count(1):
            i  = k * ops
            size = N - i
            if size <= 0 or z[i] == size:  # remain empty string or fully matched
                return ops

def z_function(s):
    N = len(s)
    z = [0]*N
    z[0] = N
    L = R = 0  # right most z-box

    for i in range(1, N):
        if i > R:  # not covered by z-box
            pass  # z[i] = 0
        else:
            j = i-L
            if j+z[j] < z[L]:  # fully covered
                z[i] = z[j]
            else:  # partial covered
                z[i] = R-i+1

        while i+z[i] < N and s[z[i]] == s[i+z[i]]:  # remaining substring
            z[i] += 1
        if i+z[i]-1 > R:  # R out of prev z-box, update R
            L = i
            R = i+z[i]-1
    return z
```
