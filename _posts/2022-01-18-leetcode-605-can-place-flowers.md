---
layout      : single
title       : "LeetCode 605. Can Place Flowers" 
tags 		: LeetCode Easy
---
好多做過的題目經過一段時間就忘記了，回顧提交紀錄還搞不懂自己怎麼寫出來的解法，希望以此加強印象，也分享給需要的朋友。
# 題目
輸入一維陣列，1表示有種花而0表示空盆栽，有種花的盆栽不得相鄰，求是否有辦法再加種n個盆栽。

# 解法
padding真是處理edge case的好朋友，在頭尾加上[0]避免出錯，之後只需在i, i-1, i+1同時為0時更新將i值更新為1、待種盆栽n-1即可。
```python
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        bed = [0]+flowerbed+[0]
        for i in range(1, len(bed)-1):
            if 0 == bed[i] == bed[i-1] == bed[i+1]:
                bed[i] = 1
                n -= 1

        return n <= 0
```
