---
layout      : single
title       : LeetCode 165. Compare Version Numbers
tags 		: LeetCode Medium String TwoPointers
---
每日題。挺單純的字串比對，可能難度被高估所以一堆人按爛。

# 題目
輸入字串version1和version2代表兩個版本號，若version1較舊版則回傳-1；version1較新則回傳1；版本相同則回傳0。  
版本號由一個或多個整數組成，中間由"."分隔。須由左至右依序比對，且整數可能帶有前導0，可以無視，即001和1為相同的版本。

# 解法
先使用split以"."將兩字串切開，得到長度分別為M和N的陣列。從0開始比對至min(M,N)，將其中子字串轉型成整數，直接比較大小即可。  
但是有可能出現0.0.1和0.0這種測資，多出來的部分沒有處理到，必須另外寫兩串處理多餘長度的子字串。若v1較長，其中出現不為0的整數代表v1較新，回傳1；若v2較長，出現不為0的整數代表v1較舊，回傳-1。順利執行到最後沒有中斷代表兩版本相等，回傳0。

```python
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        s1 = version1.split('.')
        s2 = version2.split('.')
        M, N = len(s1), len(s2)
        idx = 0
        while idx < M and idx < N:  
            v1 = int(s1[idx])
            v2 = int(s2[idx])
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
            else:
                idx += 1

        while idx < M:  
            if int(s1[idx]) != 0:
                return 1
            idx += 1

        while idx < N: 
            if int(s2[idx]) != 0:
                return -1
            idx += 1

        return 0

```
