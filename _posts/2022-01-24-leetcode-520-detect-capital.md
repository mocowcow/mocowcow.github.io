---
layout      : single
title       : LeetCode 520. Detect Capital
tags 		: LeetCode Easy String
---
日檢N1合格，開心開心。

# 題目
檢查字串是否符合以下規則：
1. 全大寫
2. 全小寫
3. 字首大寫其他小寫

# 解法
字串長度N，計算大寫字元數cnt：
1. cnt==N
2. cnt==0
3. cnt==1且字首大寫

```python
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        cnt = sum(['A' <= c <= 'Z' for c in word])
        return cnt == 0 or cnt == len(word) or cnt == 1 and 'A' <= word[0] <= 'Z'

```
