---
layout      : single
title       : LeetCode 1291. Sequential Digits
tags 		: LeetCode Medium
---
一下子不知道這算什麼類型的題目。

# 題目
一個整數，其每個數字都比前個多1的稱為連續數字，例：123,2345等。
求介於low和high之間的所有連續數字。

# 解法
分別算low和high的位數，先確認位數範圍，再分別生成所有的連續數。  
以2位數為例，起始為[1,2]，依序遞增為[2,3]、[3,4]直到最後位超過9為止。

```python
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        least = len(str(low))
        most = len(str(high))
        seq = []

        for i in range(least, most+1):
            # generate i-digits seq
            a = list(range(1, i+1))
            while a[-1] <= 9:
                n = int(''.join([str(x) for x in a]))
                if low <= n <= high:
                    seq.append(n)
                for j in range(i):
                    a[j] += 1

        return seq

```
