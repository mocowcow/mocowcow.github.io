---
layout      : single
title       : LeetCode 171. Excel Sheet Column Number
tags 		: LeetCode Easy Math String
---
每日題。這題還有個兄弟，等等一起更新。

# 題目
輸入字串columnTitle，代表EXCEL中的欄位名稱，計算他是第幾欄。  
> A=1  
> B=2  
> ...  
> Z=26  
> AA=27  

# 解法
當作是26進位就行了，例如BA可以看成2\*(26^1)+1\*(26^0)=53。ans初始化為0，從左開始遍歷每個字元c，每次把ans\*26再加上c的值。

```python
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for c in columnTitle:
            ans = ans*26+ord(c)-64

        return ans

```
