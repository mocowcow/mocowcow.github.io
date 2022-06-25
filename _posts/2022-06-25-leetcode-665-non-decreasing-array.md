--- 
layout      : single
title       : LeetCode 665. Non-decreasing Array
tags        : LeetCode Medium Array
---
每日題。好久好久以前做過，但是沒真正搞懂。今天還是錯了一模一樣的測資，但是好在馬上就能想通錯在哪，也是一種進步。

# 題目
輸入一個包含n個整數的陣列nums，判斷是否能透過修改**最多一個**元素使nums成為非遞減數列。  

# 解法
可能很多朋友都和我一樣，馬上想到檢查有多少個**下降**的元素，若某元素比前一元素還小，即為下降。  

```python
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        N=len(nums)
        modify=0
        for i in range(1,N):
            if nums[i]<nums[i-1]:
                if modify==1:
                    return False
                nums[i-1]=nums[i]
                modify=1
                
        return True
```

但是碰上[3,4,2,3]就錯了，上述程式碼會將陣列變成[3,**2**,2,3]，解決一個下降，結果在前方製造出新的下降。  

這下我們知道，改變上一個元素之前，要先檢查上上一個元素會不會造成下降，否則將當前元素修改成前一個元素。  
這樣至少不會在前方產生下降，至於後方有沒有新的下降，那就是之後檢查的事情了。

```python
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        N=len(nums)
        modify=0
        for i in range(1,N):
            if nums[i]<nums[i-1]:
                if modify==1:
                    return False
                if i>1 and nums[i-2]>nums[i]:
                    nums[i]=nums[i-1]
                else:
                    nums[i-1]=nums[i]
                modify=1
                
        return True
```