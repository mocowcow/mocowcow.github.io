---
layout      : single
title       : LeetCode 168. Excel Sheet Column Title
tags 		: LeetCode Easy Math String
---
今天每日題的兄弟。

# 題目
輸入整數columnNumber，求在EXCEL中第columnNumber欄的標題會是多少。

# 解法
一樣照著26進位的方法傳換就行。需要注意的是，因為A\~Z對應1\~26，所以每次計算都要先扣掉1才正確對應到0\~25。  
每次對columnNumber-1後模26取餘數，得到對應的字母，加到ans後面，再將columnNumber除26，重覆到columnNumber=0為止。最後將ans反轉就是答案。

```python
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        while columnNumber > 0:
            ans.append((columnNumber-1) % 26)
            columnNumber = (columnNumber-1)//26

        return ''.join(chr(x+65) for x in reversed(ans))

```
