---
layout      : single
title       : LeetCode 13. Roman to Integer
tags 		: LeetCode Easy String HashTable Math
---
看到有人說某公司面試考這題，就來玩玩看。

# 題目
輸入字串s，表示一個羅馬數字，將其轉換成阿拉伯數字。  

| 符號 | 值   |
| ---- | ---- |
| I    | 1    |
| V    | 5    |
| X    | 10   |
| L    | 50   |
| C    | 100  |
| D    | 500  |
| M    | 1000 |

羅馬數字通常由左往右寫，但有一些例外，如：IV代表4，IX，代表9。這種情況總共有六種。

# 解法
題目既然都說了只有六種特例，直接列舉用暴力取代法，之後簡單的加總就可以了。

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I": 1,
             "V": 5,
             "X": 10,
             "L": 50,
             "C": 100,
             "D": 500,
             "M": 1000}
        s = s.replace('IV', 'IIII')
        s = s.replace('IX', 'VIIII')
        s = s.replace('XL', 'XXXX')
        s = s.replace('XC', 'LXXXX')
        s = s.replace('CD', 'CCCC')
        s = s.replace('CM', 'DCCCC')
        ans = 0
        for c in s:
            ans += d[c]
        return ans
```

再看看其他人解法，這種其實也不錯。  
特例的符號有個共通點，就是本身小於右邊的符號。從此可推論最後一位的符號一定不是特例。  
遍歷第0~N-1個符號，每次檢查是否小於右邊符號，若是則表示特例，需要減去當前符號值，否則加上當前符號值。最後再加上末位符號即可。   

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I": 1,
             "V": 5,
             "X": 10,
             "L": 50,
             "C": 100,
             "D": 500,
             "M": 1000}
        ans = 0
        for i in range(len(s)-1):
            if d[s[i]] < d[s[i+1]]:
                ans -= d[s[i]]
            else:
                ans += d[s[i]]

        return ans+d[s[-1]]
```