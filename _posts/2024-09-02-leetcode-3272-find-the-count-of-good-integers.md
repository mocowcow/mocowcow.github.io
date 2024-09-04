---
layout      : single
title       : LeetCode 3272. Find the Count of Good Integers
tags        : LeetCode Hard String Math HashTable
---
biweekly contest 138。有高手打出 10\*9 的表，直接 O(1) 回答，太強了。  

## 題目

輸入兩個正整數 n 和 k。  

一個 **k 回文**整數 x 滿足：

- x 是回文數。  
- x 可被 k 整除。  

若一個整數重排列後，可以變成 **k 回文**，則稱為**好的**。  
例如 k = 2 時，整數 2020 可以被重排列成 2002；但 1010 沒有辦法重排成任何 **k 回文**。  

求有多少個 **n 位**整數是**好的**。  

注意：整數在**重排前**或**重排後**都不可以有前導零。  
例如 1010 不可被重排成 101。  

## 解法

前陣子也有一個 **k 回文**題，但做法不太相關。  
比較類似 [2967. minimum cost to make array equalindromic]({% post_url 2023-12-17-leetcode-2967-minimum-cost-to-make-array-equalindromic %})。  

---

如果想確認一個數是不是**好的**，需要先確定是否能構成回文，然後再枚舉他的所有排列，直到找到能被 k 整除的排法。  
在 n = 10 時，枚舉一個數的全排列就需要 10!，光想想就超時。  

換個角度思考，我們可以先找到 n 位數的**回文數**，再利用**組合數學**算出有幾種排法。  
而且基於回文**對稱**特性，只需要枚舉一半的數位，在 n = 10 時也只需要枚舉區間 [10^4, 10^5-1]，看起來合理不少。  

---

問題在於：兩個不同的回文數，有可能是由**相同數量的數字**組成。  
例如：1221 和 2112，這兩個數的全排列完全相同。  

為了避免重複計算，需要統計回文數中每個**數字的出現頻率**，重複出現就跳過。  
此處選擇將回文轉成字串後**排序**。  

---

第二個問題是老朋友：**前導零**。  

在 n 個數字中，有 cnt0 個 0。  
則第一個數可以選 **0 以外的數字**，有 (n - cnt0) 種選法。  
之後剩下 n-1 個數字，反正已經確定沒有前導零了，所以隨便填什麼都可以，有 (n-1)! 種選法。  

每個數字可能出現多次，是**不盡相異物**。所以每種數字的出現次數 freq 都要除 freq!。  

時間複雜度 O(10^m + n log n)，其中 m = ceil(n/2)。  
空間複雜度 O(10^m \* n)。  

```python
factorial = cache(factorial)
class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        vis = set()
        ans = 0
        for x in get_pal(n):
            if x % k != 0:
                continue

            s = "".join(sorted(str(x)))
            if s in vis:
                continue

            vis.add(s)
            d = Counter(s)
            cnt0 = d["0"]
            res = (n - cnt0) * factorial(n - 1)
            for freq in d.values():
                res //= factorial(freq)

            # update ans
            ans += res

        return ans


def get_pal(n):
    m = (n + 1) // 2
    pa = []
    start, end = 10 ** (m - 1), 10**m
    for x in range(start, end):
        left = right = x
        if n % 2 == 1:  # odd mid
            right //= 10
        while right > 0:
            right, r = divmod(right, 10)
            left = left * 10 + r
        pa.append(left)
    return pa
```
