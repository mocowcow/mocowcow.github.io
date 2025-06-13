---
layout      : single
title       : LeetCode 3579. Minimum Steps to Convert String with Operations
tags        : LeetCode Hard DP Greedy
---
weekly contest 453。  

## 題目

<https://leetcode.com/problems/minimum-steps-to-convert-string-with-operations/>

## 解法

可把 word1 劃分成若干個子字串，並進行操作使得 word1 變成 word2。  
不同的劃分方式可能剩下相同的子字串，有**重疊的子問題**，考慮 dp。  

定義 dp(i)：將 word1[i..] 變成 word2 的最小操作次數。  

---

劃分後，考慮子陣列 sub1 怎麼操作才能變成對應的 sub2。  
子陣列中的每個索引 i 可參與以下操作各**至多一次**：  

1. 把 sub1[i] 修改成任意字元  
2. 交換 sub1[i] 和 sub1[j]  
3. 把 sub1 反轉  

最差情況下直接把全部字元都修改，肯定可以變成 sub2。  
但如果 sub1 和 sub2 有正好相反的字元組，可以透過交換節省一次操作。例如：  
> sub1 = "ab", sub2 = "ba"  
> pair[0] = ("a", "b")  
> pair[1] = ("b", "a")  
> 交換 sub1[0], sub1[1] 後  
> sub1 = "ba", sub2 = "ba"  
> pair[0] = ("b", "a")  
> pair[1] = ("b", "a")  

求 sub1 和 sub2 產生的字元組個數，優先進行交換；無法交換的字元組再單獨修改。  

至於該怎麼反轉？  
反轉只能轉整個子陣列，所以只有**轉或不轉**兩種選擇。  
剛才已經講過不轉的情形，要轉的話就把 sub1 翻轉後，再用同樣邏輯先交換後修改即可。  

時間複雜度 O(N^3)。  
空間複雜度 O(N)。  

```python
class Solution:
    def minOperations(self, word1: str, word2: str) -> int:
        N = len(word1)

        @cache
        def dp(i):
            if i == N:
                return 0
            res = inf
            # 枚舉子陣列 [i..j]
            for j in range(i, N):
                # 不反轉
                sub1 = word1[i:j+1]
                sub2 = word2[i:j+1]
                op = swap_and_modify(sub1, sub2)
                res = min(res, op + dp(j+1))

                # 反轉
                sub1 = sub1[::-1]
                op = swap_and_modify(sub1, sub2) + 1
                res = min(res, op + dp(j+1))
            return res

        return dp(0)


def swap_and_modify(sub1, sub2):
    op = 0
    d = Counter()
    for a, b in zip(sub1, sub2):
        if a == b:
            continue
        if d[(b, a)] > 0:  # 可交換
            op += 1
            d[(b, a)] -= 1
        else:
            d[(a, b)] += 1
    for v in d.values():  # 沒得交換的單獨改
        op += v
    return op
```
