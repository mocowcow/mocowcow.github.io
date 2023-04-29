--- 
layout      : single
title       : LeetCode 2309. Greatest English Letter in Upper and Lower Case
tags        : LeetCode Easy HashTable String BitManipulation
---
周賽298。python真的是字串處理的神，直接秒殺有夠方便。倒是我後來用java寫卡了超過五分鐘。

# 題目
輸入字串s，找出大、小寫都有在s裡面出現的字母，並回傳最大者。若不存在則回傳空字串。

# 解法
把s中所有字元都裝入集合中，從開始Z往前遍歷到A，若大小寫都有出現過便回傳。最後沒找到就回傳空字串。  

```python
class Solution:
    def greatestLetter(self, s: str) -> str:
        s=set(s)
        for c in string.ascii_uppercase[::-1]:
            if c in s and c.lower() in s:
                return c
        
        return ''
```

竟然有人用位元操作來做這題，似乎是有點大材小用，執行起來也沒比較快就是了。  

```python
class Solution:
    def greatestLetter(self, s: str) -> str:
        n=0
        for c in s:
            i=ord(c)-65
            n|=(1<<i)
        
        for i in range(26,-1,-1):
            if n&(1<<i) and n&(1<<(i+32)):
                return chr(65+i)
        
        return ''
```