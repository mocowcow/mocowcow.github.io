--- 
layout      : single
title       : LeetCode 2554. Maximum Number of Integers to Choose From a Range I
tags        : LeetCode Medium Array HashTable Greedy
---
雙周賽97。

# 題目
輸入整數陣列**banned**，還有整數n和**maxSum**。你必須依據下列規則來選出幾個整數：  
- 選擇的整數必須介於**1\~n**之間  
- 每個整數只能被選擇一次  
- 在**banned**裡面的整數不能選  
- 被選擇的整數總合不可超過**maxSum**  

求遵循以上規則，**最多**可以選擇幾個整數。  

# 解法
優先選擇較小的數，可以最大化選擇數量。  

直接將banned放入集合供O(1)查詢。從1開始遍歷到n，若i在banned之中則跳過，一直放到即將超過maxSum為止。  

```python
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ban=set(banned)
        ans=0
        sm=0
        for i in range(1,n+1):
            if i in ban:continue
            if sm+i>maxSum:break
            sm+=i
            ans+=1
            
        return ans
```
