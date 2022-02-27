---
layout      : single
title       : LeetCode 2185. Counting Words With a Given Prefix
tags 		: LeetCode Easy String
---
周賽282。送分題。

# 題目
輸入字串陣列words和字串pref，求words中有多少字串是由pref開頭所組成的。

# 解法
直接對所有字串w暴力比對，pref長度為N，若w長度不足N則無視；對w從左方開始取長度N的子字串，若等於pref則答案計數+1。

```python
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        N = len(pref)
        cnt = 0
        for w in words:
            if len(w) < N:
                continue
            if w[0:N] == pref:
                cnt += 1

        return cnt

```
