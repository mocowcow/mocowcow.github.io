---
layout      : single
title       : LeetCode 3561. Resulting String After Adjacent Removals
tags        : LeetCode Medium Simulation Stack
---
weekly contest 451。  
感覺有點像是為 Q4 做鋪陳。  

## 題目

<https://leetcode.com/problems/resulting-string-after-adjacent-removals/description/>

## 解法

循環字母表中的 26 字母對應到 [0, 25] 中的整數。  
任意兩個字母絕對差為 1 或是 25 則稱為**連續**。  
例如：'a' 連續 'b'，然後 'a' 和 'z' 也連續。  

只要字串中存在**相鄰**的**連續**字元，則不斷消除**最左方**的相鄰對。  
這種操作令我聯想到經典的**消除括號**，可用堆疊模擬。  
相似題 [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)。  

判斷 '(' 與 ')' 改成判斷連續即可。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
def is_consecutive(x, y):
    diff = abs(ord(x) - ord(y))
    return diff == 1 or diff == 25


class Solution:
    def resultingString(self, s: str) -> str:
        st = []
        for c in s:
            if st and is_consecutive(c, st[-1]):
                st.pop()
            else:
                st.append(c)

        return "".join(st)
```
