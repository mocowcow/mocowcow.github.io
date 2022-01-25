---
layout      : single
title       : LeetCode 941. Valid Mountain Array
tags 		: LeetCode Easy Array
---
看見以前提交紀錄刷出整排紅字，這題可能還是滿值得做的。

# 題目
檢查陣列值是否形成一座山，必須符合：
1.  長度>=3
2.  起點至山頂每格值+1
3.  山頂至終點每格值-1

# 解法
分成兩個迴圈，一個向上爬，一個向下走。  
往上爬停止時，山頂一定不會是起點或是中間；向下走停止時，一定會在終點。

```python
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        N = len(arr)
        if N < 3:
            return
        idx = 1
        # going up
        while idx < N:
            if arr[idx] <= arr[idx-1]:
                break
            idx += 1
        if idx == 1 or idx == N:
            return False
        # goin down
        while idx < N:
            if arr[idx] >= arr[idx-1]:
                break
            idx += 1
        return idx == N
```
