---
layout      : single
title       : LeetCode 1790. Check if One String Swap Can Make Strings Equal
tags 		: LeetCode Easy String Counting
---
Study Plan - Programming Skills。  

# 題目
字串s1和s2，求是否能夠在最多1次換位使兩字串相等。  
每次換位可以在任一字串中，任兩個位置(可相同位置)的字元交換。

# 解法
沒有規定一定要換，所以s1==s2也算是true。  
把兩字串並排同時檢查字元c1和c2，若不相同則加入swap串列中。  
若swap為空代表兩字串相等；最多只能換一次，所以需要2個相反的字元對，swap不為2則不可能交換成功。  
最後只要檢查swap[0]和倒轉後的swap[1]是否相等。

```python
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        swap = []
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                swap.append((c1, c2))

        if not swap:
            return True

        if len(swap) != 2:
            return False

        return swap[0] == swap[1][::-1]

```
