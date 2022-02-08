---
layout      : single
title       : LeetCode 258. Add Digits
tags 		: LeetCode Easy Simulation Math
--- 
能第一眼找出數學解的人是真的強。

# 題目
輸入一個整數num，將所有位的數字加總，直到變成一位數為止，並回傳該數。

# 解法
剛開始沒想太多就直接照著描述做。第一個迴圈判斷位數，第二個迴圈加總。

```python
class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            t = 0
            while num > 0:
                t += num % 10
                num //= 10
            num = t

        return num
```

底下有個follow up，問說能不能在O(1)時間內完成？這就有趣了。  
提示要我把所有結果列出來，那就暴力法從0開始列出結果，發現答案除了0以外
都是1~9循環。那就知道num=0時回傳0，num被9整除時回傳9，其他情況回傳num%9。

```python
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9
```