---
layout      : single
title       : LeetCode 3307. Find the K-th Character in String Game II
tags        : LeetCode Hard
---
weekly contest 417。  
體感不太難，但是被 Q3 浪費太久，早知道先做這題。  

## 題目

Alice 和 Bob 在玩遊戲。最初 Alice 有一個字串 word = "a"。  

輸入正整數 k，還有整數陣列 operations，其中 operations[i] 代表第 i 次操作的種類。

Bob 要求 Alice 依序執行所有操作：  

- 若 operations[i] = 0，將 word 的**副本**附加至原始的 word。  
- 若 operations[i] = 1，將 word 的每個字元**替換**成英文字母表中**下一個**來生成新字串，並將其**附加**至原始的 word。  

例如："c" 操作後得到 "cd"；zb" 操作後得到 "zbac"。  
注意：第二種操作中，字元 'z' 替換後會變成 'a'。  

在執行操作後，回傳 word 中第 k 個字元。  

## 解法

本題上限 k = 1e14，不可能暴力生成字串了，肯定有什麼規律可循。  

兩種操作都會讓 word 長度變兩倍，而操作後的字串可以分成左右兩半。  
操作 x 次之後，word 長度為 2^x，左右兩邊各有 half = 2^(x-1) 個字元。  
分類討論 k 的位置：  

- k 位於左半邊，操作前就存在，可以無視本次操作。  
- k 位於右半邊，是由位於 k - half 的字元 c 衍生而來：  
  - 若是第一種操作，則等於 c  
  - 若是第二種操作，則等於 c 的下一個字母  

不斷重複計算**相似的子問題**，因此可以使用**遞迴**。  
注意：子問題只有一種可能性、沒有分支重疊，因此並非 dp (不需要記憶化)。  

---

定義 f(k, i)：執行 operations[i] 後的第 k 個字母。  
轉移：  

- 若 k <= half，則 f(k, i) = f(k, i-1)。  
- 若 k > half：  
  - operations[i] = 0，則 f(k, i) = f(k-half, i-1)。  
  - operations[i] = 1，則 f(k, i) = f(k-half, i-1) 的下一個字母。  

base：當 k=1 時，必定是 "a"。  

答案入口為 f(k, N-1)。  
注意：f 定義的 i 是代表最後一次操作是 operations[i]，而非執行了 i 次操作。  
注意二：為方便處理字元，以 [0, 25] 的整數代替，輸出答案才轉回字元。  

時間複雜度 O(min(N, log k))，其中 N = len(operations)。  
空間複雜度 O(min(N, log k))，遞迴 call stack。  

```python
class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        N = len(operations)
        
        def f(k, i):
            # base case "a"
            if k == 1:
                return 0

            # after (i+1) ops
            # len(word) = 2^(i+1)
            half = 1 << i # 2^i
        
            # k in left side
            if k <= half: 
                return f(k, i-1)

            # k in right side
            res = f(k-half, i-1)
            if operations[i] == 1: # next char
                res = (res + 1) % 26
            return res

        ans = f(k, N-1)
        return chr(97 + ans)
```
