--- 
layout      : single
title       : LeetCode 2451. Odd String Difference
tags        : LeetCode Easy Array String HashTable
---
雙周賽90。提交的時候本來要用ctrl+/快捷鍵註解掉測試用的輸出，結果ctrl鬆掉只打出一個斜線，得到RE。  

# 題目
輸入字串陣列words，其中每個字串的長度都為n。  

每個字串words[i]可以轉換成一個長度為n-1的**整數差分陣列**difference，其中difference[i] = words[i][j+1] - words[i][j]，且0 <= j <= n-2。  
注意，兩個字母之間的差分指的是在字母表中位置之間的距離，例如"a"的位置為0，"b"的位置為1，"z"的位置為 25。  
例如，字串"acb"，其**差分陣列**為[2-0, 1-2] = [2, -1]。  

words只有一個字串的**差分陣列**和其他字串不同，求該字串為何。  

# 解法
想半天也沒什麼好方法，只能暴力解，將每個單字轉成對應的差分陣列，用雜湊表分配。  
因為題目保證只有兩種差分陣列，而其中一種只有一個單字，所以長度為1的就是答案。  

字串長度為N，陣列長度為M，時間複雜度為O(NM)。保存每個字串的差分陣列，空間複雜度O(M)。  

```python
class Solution:
    def oddString(self, words: List[str]) -> str:
        
        def f(s):
            return tuple(ord(a)-ord(b) for a,b in pairwise(s))
        
        d=defaultdict(list)
        for w in words:
            d[f(w)].append(w)
            
        for k,v in d.items():
            if len(v)==1:
                return v[0]
```
