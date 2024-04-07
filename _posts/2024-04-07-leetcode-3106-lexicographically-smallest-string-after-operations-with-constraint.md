---
layout      : single
title       : LeetCode 3106. Lexicographically Smallest String After Operations With Constraint
tags        : LeetCode Medium Array String Greedy
---
周賽 392。

## 題目

輸入字串 s 還有整數 k。  

s1 和 s2 是兩個長度為 n 的字串，定義函數 distance(s1, s2)：  

- 字元 'a' 到 'z' 在**循環**排列下，在區間 [0, n - 1] 之中，所有 s1[i] 和 s2[i] 的**最小距離和**。  

例如：distance("ab", "cd") == 4，而 distance("a", "z") == 1。  

你可以改變 s 中的**任意**字元**任意**次。  

求任意次操作後，滿足 distance(s, t) <= k，且**字典順序最小**的字串 t。  

## 解法

為了使字典序變小，優先把靠左的字元調整成更小的元素，最理想當然就是 'a'。  
但是受限於 k，不一定每次都能改成 'a'；如果無法改成 'a'，那能多小就多小，之後的也沒辦法繼續改了。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        a = [ord(c) - 97 for c in s]
        for i, x in enumerate(a):
            # to 'a'
            dist = min(26 - x, x)
            if dist <= k:
                k -= dist
                a[i] =0
                continue

            # to some else
            a[i] -= k
            break
        
        ans = [chr(x + 97) for x in a]

        return "".join(ans)
```
