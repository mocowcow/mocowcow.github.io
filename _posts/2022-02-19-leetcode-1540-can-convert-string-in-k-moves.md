---
layout      : single
title       : LeetCode 1540. Can Convert String in K Moves
tags 		: LeetCode Medium HashTable String Math
---
隨便抽到的。可能測資有點太不夠意思才一堆人給爛。

# 題目
輸入長度分別為M、N的字串s、t以及整數k，求是否有辦法轉換s為t。  
你可以進行k次轉換，在第i次轉換時可以不執行轉換，或選擇任意s中任意位置字元，將其轉換成後i個字元。例如i=2時，可以把a轉換成c，或是把z轉換成b。  
s中每個位置的字母最多只能被轉換一次。  
例：  
> s = "aab", t = "bbb", k = 27
> 第一個a轉換1次，變成b  
> 第二個a轉換27次，變成b  
> 成功轉換，答案為true

# 解法
s和t長度不一定會一樣，記得要先過濾此情形。  
因為走1步和27步其實是等價的，我直接對1~k的數字模26，計算移動距離各有幾次機會，然後逐一比對s和t中的字元，若不相同則計算需要移動多少距離need。若need步無可用次數代表兩字串不可能相等，回傳false；否則need可用次數-1。

```python
class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False

        move = Counter([x % 26 for x in range(1, k+1)])
        for a, b in zip(s, t):
            if a != b:
                need = (ord(b)-ord(a)) % 26
                if not move[need]:
                    return False
                move[need] -= 1

        return True

```

但是來了個測資k=100000000直接超時，我真是服了。只好改成數學計算可用次數，這才順利通過。

```python
class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False

        move = Counter()
        for i in range(1, 26):
            move[i] = k//26+(k % 26 >= i)
        for a, b in zip(s, t):
            if a != b:
                need = (ord(b)-ord(a)) % 26
                if not move[need]:
                    return False
                move[need] -= 1

        return True
```