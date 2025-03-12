---
layout      : single
title       : LeetCode 3470. Permutations IV
tags        : LeetCode Hard Math
---
biweekly contest 151。  
過了好久才來補題。挺奇怪的構造題。  
大概也算是 python 優勢場吧。  

## 題目

<https://leetcode.com/problems/permutations-iv/submissions/1571381333/>

## 解法

數字 [1..n] ，其中有 odd 個奇數，even 個偶數。  
規定相鄰數字的奇偶性不同，必須要交替著放。  
決定第一個數的奇偶後，其餘位置的奇偶性也固定了。  

分類討論第一個數的奇偶性：  

- n 是奇數，奇數比偶數多，只能選奇數。  
- n 是偶數，奇數和偶數一樣多，奇偶都能。  

第一個數奇偶性確定後，奇數位有 odd! 種排列，偶數位有 even! 種排列。  

- n 是奇數，共有 odd! \* even! 種選法。
- n 是偶數，共有 2 \* odd! \* even! 種選法。  

維護 get_ways(n) 函數求 odd! \* even!。  

先算出總排列數 tot。  
若 k > tot ，沒有答案，直接回傳空陣列。  

---

n 個數原有 get_ways(n) 種選法，填完 1 個數後，剩下 get_ways(n-1) 種選法。  

先看簡單的範例二：  
> n = 3, k = 2  
> n 是奇數，所以 i = 0 只能填 1,3  
> 總排列有 get_ways(3) = 2!1! = 2 種  
> i = 0 填 1，剩下選法 get_ways(2) = 1!1! = 1 種  
> i = 0 填 3，剩下選法也有 get_ways(2) = 1!1! = 1 種  

再看看範例一：  
> n = 4, k = 6  
> n 是偶數，所以 i = 0 可以填 1,2,3,4  
> i = 0 不管填什麼，剩下選法都有 get_ways(3) = 2!1! = 2 種  

可以視作每 ways = get_ways(n-1-i) 個連續的選法隸屬於同個數字 j。  
從小枚舉可填的數 j，若剩餘組數 k 小於等於 ways，代表答案屬於 j 這組裡面。填入 j 並交替奇偶性；  
否則 k 大於 ways，代表答案不屬於 j 這組。從 k 裡面排除 ways 種選法。  

時間複雜度 O(n^2)。  
空間複雜度 O(n)。  

```python
MX = 100
f = [1] * (MX + 1)
for i in range(1, MX + 1):
    f[i] = f[i-1] * i

def get_ways(n):
    return f[n//2] * f[(n+1) // 2]

class Solution:
    def permute(self, n: int, k: int) -> List[int]:
        tot = get_ways(n)
        if n % 2 == 0:
            tot *= 2

        if k > tot:
            return []

        used = set()
        ans = []
        parity = 1
        for i in range(n):
            ways = get_ways(n-i-1)
            for j in range(1, n+1):
                if j in used:
                    continue
                if (i == 0 and n % 2 == 0) or (j % 2 == parity):
                    if k <= ways:
                        ans.append(j)
                        used.add(j)
                        parity = (j % 2) ^ 1
                        break
                    k -= ways

        return ans
```
