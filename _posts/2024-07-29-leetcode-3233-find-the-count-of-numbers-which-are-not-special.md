---
layout      : single
title       : LeetCode 3233. Find the Count of Numbers Which Are Not Special
tags        : LeetCode Medium Math BinarySearch PrefixSum
---
weekly contest 408。  

## 題目

輸入兩個正整數 l, r。  
對於一個整數 x 來說，其除了 x 本身以外的正數因子都稱為**真因子**。  

若一個數只有正好 2 個**真因子**，則稱為**特別的**。例如：  

- 4 只有 1, 2 兩個真因子，是特別的  
- 6 有 1, 2, 3 三個真因子，不是特別的  

求區間 [l, r] 內有多少數**不是特別的**。  

## 解法

首先發現 r 的範圍高達 10^9，不可能逐一檢查是否特別。  
但**特別數**的條件十分嚴苛，所以找 [l, r] 間有多少特別數，以差集的方式求答案。  

若一個數 x 只有兩個真因子，其中一個必定是 1，另一個是 i = sqrt(x)。可見 x 是**完全平方數**。  
但完全平方數不一定是特別的，i 可能由其他因子組成，所以 i 必須要是質數。  

因此枚舉所有滿足 i^2 <= r 的因子 i，並判斷 i 是否為質數，若是則代表 i^2 是特別的。  

---

枚舉因數 i 共有 sqrt(r) 個，同時 i 的最大值也是 sqrt(r)。  
判斷一個數 n 的複雜度是 sqrt(n)，而此處 n = sqrt(r)。  
代入 r = 10^9 之後大約是 5e6 的計算量，還算可以接受。  

時間複雜度 O(sqrt(r) \* sqrt(sqrt(r)))。  
空間複雜度 O(1)。  

```python
class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        cnt = 0
        i = 2
        while i * i <= r:
            if i * i >= l and is_prime(i):
                cnt += 1
            i += 1

        return r - l + 1 - cnt

# check is prime or not
# O(sqrt(n))
def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n >= 2
```

對於不同組測資來說，都要用到同樣的質數。  
不妨先預處理所有小於 sqrt(10^9) 的質數，並生成對應的**特別數**。  

之後每次查詢只需要二分找到 l, r 的範圍即可。  

時間複雜度 O(log r)，預處理時間不計入。  
空間複雜度 O(1)，預處理空間不計入。  

```python
MX = isqrt(10 ** 9)
special = []
sieve = [True] * (MX + 1)
for i in range(2, MX + 1):
    if sieve[i]:
        special.append(i * i)
        for j in range(i * i, MX + 1, i):
            sieve[j] = False

class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        first = bisect_left(special, l)
        last = bisect_right(special, r)
        cnt = last - first
        return r - l + 1 - cnt
```

又或者可以統計**因子最大為 i** 時對應的**特別數個數**。  

對於區間 [l, r]，等價於 [0, r] 扣掉 [0, l - 1]。  
以前綴和的概念相同，扣除不需要的部分即可。  

時間複雜度 O(1)，預處理時間不計入。  
空間複雜度 O(1)，預處理空間不計入。  

```python
MX = isqrt(10 ** 9)
ps = [0] * (MX + 1)
sieve = [True] * (MX + 1)
for i in range(2, MX + 1):
    ps[i] = ps[i - 1]
    if sieve[i]:
        ps[i] += 1
        for j in range(i * i, MX + 1, i):
            sieve[j] = False

class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        cnt = ps[isqrt(r)] - ps[isqrt(l - 1)]
        return r - l + 1 - cnt
```
