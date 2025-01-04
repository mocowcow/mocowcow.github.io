---
layout      : single
title       : LeetCode 3405. Count the Number of Arrays with K Matching Adjacent Elements
tags        : LeetCode Hard Math
---
weekly contest 430。  
純數學題，個人覺得這題很爛。  

## 題目

輸入整數 n, m, k。  
一個長度 n 的**好的陣列** arr 定義為：  

- arr 中所有元素都在 [1, m] 之間。  
- 有正好 k 個索引 i 滿足 arr[i-1] == arr[i]，其中 1 <= i < n。  

求有多少種**好陣列**。  
答案可能很大，先模 10^9 + 7 後回傳。  

## 解法

跟寫程式沒什麼太大的關係，就是組合數學。  

真的硬要說的話難點在於**乘法逆元**，如何在模數下做除法運算。  
但只要用 python 就可以直接忽略。  

---

題目求的是所有相鄰的元素對中，有 k 對**相同**。  
一個長度 n 的陣列，有 n-1 的相鄰對，所以求 n-1 選 k 的方案數，即 comb(n-1, k)。  

---

有 k 對相同，就有 n-1-k 對**不同**。  
所以陣列會被分割成 (n-1-k)+1 段由相同元素組成的區間。例如：  
> n = 4, m = 2, k = 2  
> 有 n-k = 2 段連續區間  
> 陣列會像是 a..b..  

第一段可選 [1, m] 之間任意元素，但是從第二段開始就不能和前段相同，只有 m-1 種選擇。  
第一段有 m 種選法，剩下 n-k-1 段各有 m-1 種選法。  
所以要再乘上 m \* (m-1)^(n-k-1)。  

答案即 comb(n-1, k) \* m \* (m-1)^(n-k-1)。  

時間複雜度 O(log n)。  
空間複雜度 O(1)。  

```python
MOD = 10 ** 9 + 7
class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        return comb(n-1, k) * m * pow(m-1, n-k-1, MOD) % MOD
```

正規寫法還得計算乘法逆元，才能正確處理模運算下的除法。  

```python
# precompute all factorial and modular multiplicative inverse for factorial
# O(MX log EXP) where EXP = MOD-2
MOD = 10**9 + 7
MX = 10**5 + 5
f = [0]*(MX+1)
finv = [0]*(MX+1)
f[0] = finv[0] = 1
f[1] = finv[1] = 1
for i in range(2, MX+1):
    f[i] = (f[i-1]*i) % MOD
    finv[i] = pow(f[i], -1, MOD)


class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        return comb(n-1, k) * m * pow(m-1, n-k-1, MOD) % MOD


def comb(n, k):
    res = f[n] * finv[k] * finv[n-k]
    return res
```
