---
layout      : single
title       : LeetCode 169. Majority Element
tags 		: LeetCode Easy Counting Sorting HashTable
---
每日題。解法非常多元。

# 題目
輸入長度N的整數陣列nums，找到裡面的**主要元素**。  
主要元素指的是出現超過n/2次的數字。

# 解法
主要是follow up想考的O(N)時間且O(1)解法，叫做Boyer-Moore algorithm。  
設立一個候選人cand，票數cnt初始為0，遍歷每個數字n。若cnt=0，cand更新為n。若n=candi，則cnt+1；否則cnt-1。

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand = None
        cnt = 0
        for n in nums:
            if cnt == 0:
                cand = n
            if cand == n:
                cnt += 1
            else:
                cnt -= 1

        return cand

```

另外也可以使用雜湊表計數，出現最多的就是答案；或是排序數列，最中間的元素也是答案。程式碼就不附上了。